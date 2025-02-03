from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Page principale avec affichage des livres et des emprunts
@app.route('/', methods=['GET'])
def consigne():
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()

    search_query = request.args.get('search')

    if search_query:
        cur.execute("SELECT * FROM livres WHERE titre LIKE ?", ('%' + search_query + '%',))
    else:
        cur.execute("SELECT * FROM livres;")
    
    livres = cur.fetchall()

    # Récupérer la liste des emprunts
    cur.execute("""
        SELECT emprunts.id, livres.titre, emprunts.nom_emprunteur 
        FROM emprunts 
        JOIN livres ON emprunts.livre_id = livres.id
    """)
    emprunts = cur.fetchall()

    connection.close()
    
    return render_template('accueil.html', livres=livres, emprunts=emprunts)

# Route pour ajouter un livre
@app.route('/ajouter', methods=['POST'])
def ajouter_livre():
    titre = request.form['titre']
    auteur = request.form['auteur']
    annee = request.form['annee']
    genre = request.form['genre']
    stock = request.form['stock']

    connection = sqlite3.connect('database.db')
    cur = connection.cursor()
    cur.execute("INSERT INTO livres (titre, auteur, annee, genre, stock) VALUES (?, ?, ?, ?, ?)", 
                (titre, auteur, annee, genre, stock))
    connection.commit()
    connection.close()

    return redirect(url_for('consigne'))

# Route pour supprimer un livre
@app.route('/supprimer/<int:id>', methods=['POST'])
def supprimer_livre(id):
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()
    cur.execute("DELETE FROM livres WHERE id = ?", (id,))
    connection.commit()
    connection.close()

    return redirect(url_for('consigne'))

# Route pour emprunter un livre
@app.route('/emprunter/<int:id>', methods=['POST'])
def emprunter_livre(id):
    nom_emprunteur = request.form['nom_emprunteur']

    connection = sqlite3.connect('database.db')
    cur = connection.cursor()

    # Vérifier si le livre est en stock
    cur.execute("SELECT stock FROM livres WHERE id = ?", (id,))
    stock = cur.fetchone()[0]

    if stock > 0:
        # Enregistrer l'emprunt
        cur.execute("INSERT INTO emprunts (livre_id, nom_emprunteur) VALUES (?, ?)", (id, nom_emprunteur))

        # Réduire le stock du livre
        cur.execute("UPDATE livres SET stock = stock - 1 WHERE id = ?", (id,))
        
        connection.commit()

    connection.close()
    return redirect(url_for('consigne'))

if __name__ == "__main__":
    app.run(debug=True)
