from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)                                                                                                                  

@app.route('/')
def consigne():
    return render_template('accueil.html') #Comm


# Démarrer l'application Flask
if __name__ == "__main__":
    app.run(debug=True)
