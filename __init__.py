from flask import Flask, render_template

# Initialiser l'application Flask
app = Flask(__name__)

# Définir la route pour la page d'accueil
@app.route('/')
def hello_world():
    # Retourner un message simple
    return render_template('hello.html')

# Démarrer le serveur Flask
if __name__ == "__main__":
    app.run(debug=True)
