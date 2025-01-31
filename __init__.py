@app.route('/', methods=['GET'])
def consigne():
    # Connexion à la base de données
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()

    # Vérification du nombre de livres dans la base
    cur.execute("SELECT COUNT(*) FROM livres")
    total_livres = cur.fetchone()
    print(f"Total livres dans la base : {total_livres[0]}")  # Affiche le nombre de livres dans la base

    search_query = request.args.get('search')

    if search_query:
        cur.execute("SELECT * FROM livres WHERE titre LIKE ?", ('%' + search_query + '%',))
    else:
        cur.execute("SELECT * FROM livres")
    
    livres = cur.fetchall()

    # Fermer la connexion
    connection.close()

    return render_template('accueil.html', livres=livres)
