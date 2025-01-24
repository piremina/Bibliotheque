from flask import Flask, render_template, request
import sqlite3

# Initialiser l'application Flask
app = Flask(__name__)

@app.route('/index')
def consigne():
    return render_template('index.html') #Comm

# Route pour afficher la page d'enregistrement et de gestion des livres
@app.route('/enregistrement_livre', methods=['GET', 'POST'])
def enregistrement_livre():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        # Ajouter un nouveau livre
        titre = request.form['titre']
        auteur = request.form['auteur']
        annee = request.form['annee']
        genre = request.form['genre']

        # Insertion dans la base de données
        cursor.execute("INSERT INTO livres (titre, auteur, annee, genre) VALUES (?, ?, ?, ?)",
                       (titre, auteur, annee, genre))
        conn.commit()

    # Récupérer tous les livres pour les afficher
    cursor.execute("SELECT * FROM livres")
    livres = cursor.fetchall()
    conn.close()

    return render_template('enregistrement_livre.html', livres=livres)




@app.route('/recherche_livre', methods=['GET', 'POST'])
def recherche_livre():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Récupération de tous les livres dans la base de données
    query = "SELECT * FROM livres"
    all_livres = cursor.execute(query).fetchall()

    # Gérer la recherche si un formulaire POST est envoyé
    livres = []
    search_query = ""
    if request.method == 'POST':
        search_query = request.form.get('search_query', '')
        query = "SELECT * FROM livres WHERE titre LIKE ? OR auteur LIKE ?"
        livres = cursor.execute(query, ('%' + search_query + '%', '%' + search_query + '%')).fetchall()
    else:
        livres = all_livres  # Par défaut, afficher tous les livres

    conn.close()
    return render_template('recherche_livre.html', livres=livres, search_query=search_query)


# Démarrer l'application Flask
if __name__ == "__main__":
    app.run(debug=True)
