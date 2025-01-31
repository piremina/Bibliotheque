from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)                                                                                                                  
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Clé secrète pour les sessions

def est_authentifie():
    return session.get('authentifie')

@app.route('/')
def lecture():
    if not est_authentifie():
        # Rediriger vers la page d'authentification si l'utilisateur n'est pas authentifié
        return redirect(url_for('authentification'))
    return "<h2>Bravo, vous êtes authentifié</h2>"

@app.route('/authentification', methods=['GET', 'POST'])
def authentification():
    if request.method == 'POST':
        # Vérifier les identifiants
        if request.form['username'] == 'admin' and request.form['password'] == 'password':  # Remplacer avec des variables sécurisées
            session['authentifie'] = True
            return redirect(url_for('lecture'))
        else:
            return render_template('formulaire_authentification.html', error=True)
    return render_template('formulaire_authentification.html', error=False)

@app.route('/index')
def consigne():
    return render_template('index.html') #Comm

# Route pour afficher la page d'enregistrement et de gestion des livres
@app.route('/enregistrement_livre')
def enregistrement_livre():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livres")
    livres = cursor.fetchall()
    conn.close()
    return render_template('enregistrement_livre.html', livres=livres)

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
    cursor.execute("SELECT * FROM livres;")
    livres = cursor.fetchall()
    conn.close()

    return render_template('enregistrement_livre.html', livres=livres)

    
# Route pour afficher tous les livres et gérer la recherche
@app.route('/recherche_livre/', methods=['GET', 'POST'])
def recherche_livre():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Par défaut, on récupère tous les livres
    if request.method == 'POST':
        search_query = request.form['search_query']
        # Effectuer une recherche par titre ou auteur
        query = f"SELECT * FROM livres WHERE titre LIKE ? OR auteur LIKE ?;"
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
