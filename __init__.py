from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'ton_secret_key'  # À changer

# Connexion à la base de données
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Route pour la page d'accueil et de recherche
@app.route('/')
def accueil():
    user_role = session.get('role', 'utilisateur')  # Récupère le rôle de l'utilisateur
    search_query = request.args.get('search')
    conn = get_db_connection()
    if search_query:
        livres = conn.execute("SELECT * FROM livres WHERE titre LIKE ?", ('%' + search_query + '%',)).fetchall()
    else:
        livres = conn.execute("SELECT * FROM livres").fetchall()
    conn.close()
    return render_template('accueil.html', livres=livres, user_role=user_role)

# Route pour la connexion
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        mot_de_passe = request.form['mot_de_passe']
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM utilisateurs WHERE email = ?', (email,)).fetchone()
        conn.close()
        if user and user['mot_de_passe'] == mot_de_passe:
            session['user_id'] = user['id']
            session['role'] = user['role']
            return redirect(url_for('accueil'))
        else:
            return "Identifiants incorrects", 401
    return render_template('login.html')

# Déconnexion
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('accueil'))

if __name__ == '__main__':
    app.run(debug=True)
