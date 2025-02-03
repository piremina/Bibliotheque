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

    # Récupérer la liste des emprunts avec les utilisateurs
    cur.execute("""
        SELECT emprunts.id, livres.titre, utilisateurs.nom, utilisateurs.prenom, emprunts.date_emprunt, emprunts.date_retour_prevue 
        FROM emprunts 
        JOIN livres ON emprunts.livre_id = livres.id
        JOIN utilisateurs ON emprunts.utilisateur_id = utilisateurs.id
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

# Route pour emprunter un livre
@app.route('/emprunter/<int:livre_id>', methods=['POST'])
def emprunter_livre(livre_id):
    utilisateur_id = request.form['utilisateur_id']
    date_emprunt = request.form['date_emprunt']
    date_retour_prevue = request.form['date_retour_prevue']

    connection = sqlite3.connect('database.db')
    cur = connection.cursor()

    # Vérifier le stock
    cur.execute("SELECT stock FROM livres WHERE id = ?", (livre_id,))
    stock = cur.fetchone()[0]

    if stock > 0:
        # Enregistrer l'emprunt
        cur.execute("INSERT INTO emprunts (utilisateur_id, livre_id, date_emprunt, date_retour_prevue) VALUES (?, ?, ?, ?)",
                    (utilisateur_id, livre_id, date_emprunt, date_retour_prevue))
        
        # Réduire le stock du livre
        cur.execute("UPDATE livres SET stock = stock - 1 WHERE id = ?", (livre_id,))
        
        connection.commit()
    connection.close()
    return redirect(url_for('consigne'))

# Route pour retourner un livre
@app.route('/retourner/<int:emprunt_id>', methods=['POST'])
def retourner_livre(emprunt_id):
    date_retour_effective = request.form['date_retour_effective']

    connection = sqlite3.connect('database.db')
    cur = connection.cursor()

    # Mettre à jour la date de retour
    cur.execute("UPDATE emprunts SET date_retour_effective = ? WHERE id = ?", (date_retour_effective, emprunt_id))
    
    # Récupérer le livre_id pour réajuster le stock
    cur.execute("SELECT livre_id FROM emprunts WHERE id = ?", (emprunt_id,))
    livre_id = cur.fetchone()[0]
    cur.execute("UPDATE livres SET stock = stock + 1 WHERE id = ?", (livre_id,))
    
    connection.commit()
    connection.close()
    return redirect(url_for('consigne'))

if __name__ == "__main__":
    app.run(debug=True)
