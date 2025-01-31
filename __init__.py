from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET'])
def consigne():
    # Connexion à la base de données
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()

    search_query = request.args.get('search')  # Récupérer la recherche de l'utilisateur

    if search_query:
        # Si une recherche est faite, on filtre les livres par titre
        cur.execute("SELECT * FROM livres WHERE titre LIKE ?", ('%' + search_query + '%',))
    else:
        # Sinon, on affiche tous les livres
        cur.execute("SELECT * FROM livres")
    
    livres = cur.fetchall()  # On récupère la liste des livres

    # Fermer la connexion
    connection.close()

    # Afficher la liste des livres dans le template
    return render_template('accueil.html', livres=livres)

# Démarrer l'application Flask
if __name__ == "__main__":
    app.run(debug=True)
