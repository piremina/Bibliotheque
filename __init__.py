from flask import Flask, render_template, request
import sqlite3

# Initialiser l'application Flask
app = Flask(__name__)

@app.route('/index')
def consigne():
    return render_template('index.html') #Comm

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
