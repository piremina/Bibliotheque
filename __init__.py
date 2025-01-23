from flask import Flask, render_template

# Initialiser l'application Flask
app = Flask(__name__)

# Définir la route pour la page /welcome
@app.route('/index')
def index():
    return render_template('index.html')  # Rend le fichier HTML dans le dossier templates


# Définir la route pour afficher le formulaire d'enregistrement/suppression des livres
@app.route('/formulaire_livre', methods=['GET'])
def formulaire_livre():
    return render_template('formulaire_livre.html')  # afficher le formulaire

# Définir la route pour enregistrer un livre
@app.route('/formulaire_livre', methods=['POST'])
def enregistrer_livre():
    titre = request.form['titre']
    auteur = request.form['auteur']

@app.route('/recherche_livre/')
def ReadBDD():
    conn = sqlite2.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livres;')
    data = cursor.fetchall()
    conn.close()
    return render_template('data.html', data=data)

# Démarrer l'application Flask
if __name__ == "__main__":
    app.run(debug=True)
