from flask import Flask, render_template, request
import sqlite3

# Initialiser l'application Flask
app = Flask(__name__)

@app.route('/index')
def consigne():
    return render_template('index.html') #Comm

# Route pour afficher et gérer l'enregistrement/suppression des livres
@app.route('/enregistrement_livre', methods=['GET', 'POST'])
def enregistrement_livre():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

# Ajouter un livre si méthode POST
    if request.method == 'POST' and 'titre' in request.form and 'nom' in request.form:
        titre = request.form['titre']
        auteur = request.form['nom']
        cursor.execute('INSERT INTO livres (titre, auteur) VALUES (?, ?)', (titre, auteur))
        conn.commit()

    # Récupérer tous les livres existants
    cursor.execute('SELECT * FROM livres')
    livres = cursor.fetchall()
    conn.close()

    return render_template('enregistrement_livre.html', livres=livres)
# Route pour supprimer un livre
@app.route('/supprimer_livre/<int:livre_id>', methods=['POST'])
def supprimer_livre(livre_id):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Vérifier si le livre existe avant de supprimer
        cursor.execute('SELECT * FROM livres WHERE id = ?', (livre_id,))
        livre = cursor.fetchone()

        if livre:
            # Supprimer le livre
            cursor.execute('DELETE FROM livres WHERE id = ?', (livre_id,))
            conn.commit()

        conn.close()
    except Exception as e:
        print(f"Erreur lors de la suppression : {e}")  # Log pour débogage
    finally:
        # Rediriger vers la page d'enregistrement après suppression
        return redirect(url_for('enregistrement_livre'))

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
