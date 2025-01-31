from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Route principale
@app.route('/', methods=['GET'])
def consigne():
    # Connexion à la base de données SQLite
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()

    search_query = request.args.get('search')  # Récupérer la recherche de l'utilisateur

    # Si une recherche est effectuée, on filtre les livres par titre
    if search_query:
        cur.execute("SELECT * FROM livres WHERE titre LIKE ?", ('%' + search_query + '%',))
    else:
    # Récupérer tous les livres dans la base de données
        cur.execute("SELECT * FROM livres")
        livres = cur.fetchall()


    # Fermer la connexion à la base de données
    connection.close()

    # Renvoyer la liste des livres vers le template HTML
    return render_template('accueil.html', livres=livres)

# Démarrer l'application Flask
if __name__ == "__main__":
    app.run(debug=True)
