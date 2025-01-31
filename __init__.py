from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)

# Fonction pour récupérer les livres depuis la base de données
def get_all_books():
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()
    cur.execute("SELECT titre, auteur, annee, genre, stock FROM livres")
    livres = cur.fetchall()
    connection.close()
    return livres

@app.route('/')
def consigne():
    livres = get_all_books()  # Récupérer la liste de tous les livres
    return render_template('accueil.html', livres=livres)  # Passer les livres au template

# Démarrer l'application Flask
if __name__ == "__main__":
    app.run(debug=True)
