from flask import Flask, render_template, request
import sqlite3

# Initialiser l'application Flask
app = Flask(__name__)

@app.route('/index')
def consigne():
    return render_template('index.html') #Comm

# Route pour afficher et gérer l'enregistrement des livres
@app.route('/enregistrement_livre', methods=['GET'])
def enregistrement_livre():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Récupérer tous les livres existants
    cursor.execute('SELECT * FROM livres')
    livres = cursor.fetchall()
    conn.close()

    return render_template('partials/livres_list.html', livres=livres)

# Route pour ajouter un nouveau livre
@app.route('/ajouter_livre', methods=['POST'])
def ajouter_livre():
    titre = request.form['titre']
    auteur = request.form['auteur']
    annee = request.form['annee']
    genre = request.form['genre']
    stock = request.form['stock']
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Ajouter le livre à la base de données
    cursor.execute('INSERT INTO livres (titre, auteur, annee, genre, stock) VALUES (?, ?, ?, ?, ?)', 
                   (titre, auteur, annee, genre, stock))
    conn.commit()
    conn.close()

    return jsonify({"message": "Livre ajouté avec succès"}), 200

# Route pour supprimer un livre
@app.route('/supprimer_livre/<int:livre_id>', methods=['POST'])
def supprimer_livre(livre_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Supprimer le livre de la base de données
    cursor.execute('DELETE FROM livres WHERE id = ?', (livre_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Livre supprimé avec succès"}), 200

# Route pour afficher tous les livres et gérer la recherche
@app.route('/recherche_livre/', methods=['GET', 'POST'])
def recherche_livre():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Par défaut, on récupère tous les livres
    if request.method == 'POST':
        search_query = request.form['search_query']
        # Effectuer une recherche par titre ou auteur
        query = f"SELECT * FROM livres WHERE titre LIKE ? OR auteur LIKE ?"
        cursor.execute(query, ('%' + search_query + '%', '%' + search_query + '%'))
    else:
        # Si pas de recherche, on récupère tous les livres
        query = "SELECT * FROM livres"
        cursor.execute(query)

    livres = cursor.fetchall()
    conn.close()

    return render_template('recherche_livre.html', livres=livres, search_query=request.form.get('search_query', ''))

# Démarrer l'application Flask
if __name__ == "__main__":
    app.run(debug=True)
