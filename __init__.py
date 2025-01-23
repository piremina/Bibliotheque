from flask import Flask, render_template, request, redirect
import sqlite3

# Initialiser l'application Flask
app = Flask(__name__)

# Définir la route pour la page d'accueil
@app.route('/index')
def index():
    return render_template('index.html')  # Rendu du fichier HTML

# Définir la route pour afficher le formulaire d'enregistrement/suppression des livres
@app.route('/formulaire_livre', methods=['GET'])
def formulaire_livre():
    return render_template('formulaire_livre.html')  # Afficher le formulaire

# Définir la route pour enregistrer un livre
@app.route('/formulaire_livre', methods=['POST'])
def enregistrer_livre():
    titre = request.form['titre']
    auteur = request.form['auteur']
    # Code pour enregistrer le livre dans la base de données (à ajouter)
    return redirect('/formulaire_livre')  # Rediriger après l'enregistrement

# Définir la route pour afficher les résultats de recherche
@app.route('/recherche_livre/', methods=['GET', 'POST'])
def recherche_livre():
    # Si la méthode est POST, effectuer la recherche
    if request.method == 'POST':
        search_query = request.form['search_query']
        
        # Se connecter à la base de données
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Effectuer une requête SQL pour rechercher par titre ou auteur
        query = f"SELECT * FROM livres WHERE titre LIKE ? OR auteur LIKE ?"
        cursor.execute(query, ('%' + search_query + '%', '%' + search_query + '%'))
        livres = cursor.fetchall()

        conn.close()  # Fermer la connexion à la base de données

        return render_template('recherche_livre.html', livres=livres, search_query=search_query)
    
    # Si la méthode est GET, juste afficher la page de recherche avec un formulaire vide
    return render_template('recherche_livre.html', livres=[], search_query='')

# Route pour afficher tous les livres (peut-être pour la page des résultats)
@app.route('/liste_livres')
def liste_livres():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livres;')  # Récupérer tous les livres
    livres = cursor.fetchall()
    conn.close()
    return render_template('data.html', livres=livres)

# Démarrer l'application Flask
if __name__ == "__main__":
    app.run(debug=True)
