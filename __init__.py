from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)                                                                                                                  

@app.route('/')
def consigne():
    return render_template('accueil.html') #Comm

@app.route('/recherche_livre', methods=['GET'])
def recherche_livre():
    recherche = request.args.get('recherche', '')
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()
    
    cur.execute("SELECT * FROM livres WHERE titre LIKE ? OR auteur LIKE ? OR genre LIKE ?", 
                ('%' + recherche + '%', '%' + recherche + '%', '%' + recherche + '%'))
    livres = cur.fetchall()
    
    connection.close()
    return render_template('accueil.html', livres=livres)


@app.route('/supprimer/<int:id>', methods=['GET'])
def supprimer_livre(id):
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()
    
    cur.execute("DELETE FROM livres WHERE id = ?", (id,))
    connection.commit()
    connection.close()
    
    return redirect(url_for('consigne'))


@app.route('/ajouter_livre', methods=['GET', 'POST'])
def ajouter_livre():
    if request.method == 'POST':
        titre = request.form['titre']
        auteur = request.form['auteur']
        annee = request.form['annee']
        genre = request.form['genre']
        
        connection = sqlite3.connect('database.db')
        cur = connection.cursor()
        
        cur.execute("INSERT INTO livres (titre, auteur, annee, genre) VALUES (?, ?, ?, ?)", 
                    (titre, auteur, annee, genre))
        connection.commit()
        connection.close()
        
        return redirect(url_for('consigne'))  # Retour à la page d'accueil après ajout
    return render_template('ajouter_livre.html')



# Démarrer l'application Flask
if __name__ == "__main__":
    app.run(debug=True)
