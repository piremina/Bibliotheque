from flask import Flask, render_template

# Initialiser l'application Flask
app = Flask(__name__)

# Définir la route pour la page /welcome
@app.route('/index')
def index():
    return render_template('index.html')  # Rend le fichier HTML dans le dossier templates

# Démarrer l'application Flask
if __name__ == "__main__":
    app.run(debug=True)
