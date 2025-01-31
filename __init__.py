from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Route principale
@app.route('/', methods=['GET'])
def consigne():
    # Connexion à la base de données SQLite
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()

    search_query = request.args.get('search')  # Récupérer la recherche de l'utilisateur

    # Si une recherche est effectuée, on filtre les livres par titre
    if search_query:
        cur.execute("SELECT * FROM livres WHERE titre LIKE ?", ('%' + search_query + '%',))
    else:
        # Sinon, on affiche tous les livres
        cur.execute("SELECT * FROM livres")
    
    livres = cur.fetchall()  # Récupère la liste des livres depuis la base de données

    # Si la base de données est vide, on injecte une liste manuelle de livres
    if not livres:
        livres = [
            ('Harry Potter à l\'école des sorciers', 'J.K. Rowling', 1997, 'Fantasy', 8),
            ('Le Seigneur des anneaux', 'J.R.R. Tolkien', 1954, 'Fantasy', 9),
            ('Pride and Prejudice', 'Jane Austen', 1813, 'Roman', 10),
            ('The Catcher in the Rye', 'J.D. Salinger', 1951, 'Roman', 2),
            ('Moby Dick', 'Herman Melville', 1851, 'Aventure', 3),
            ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Roman', 6),
            ('Don Quixote', 'Miguel de Cervantes', 1605, 'Roman', 4),
            ('Les Fleurs du mal', 'Charles Baudelaire', 1857, 'Poésie', 5),
            ('War and Peace', 'Leo Tolstoy', 1869, 'Historique', 7),
            ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Roman', 6),
            ('The Hobbit', 'J.R.R. Tolkien', 1937, 'Fantasy', 8),
            ('Frankenstein', 'Mary Shelley', 1818, 'Horreur', 3),
            ('Brave New World', 'Aldous Huxley', 1932, 'Science-fiction', 4),
            ('The Picture of Dorian Gray', 'Oscar Wilde', 1890, 'Roman', 5),
            ('Dracula', 'Bram Stoker', 1897, 'Horreur', 6),
            ('The Odyssey', 'Homer', -800, 'Classique', 5),
            ('Anna Karenina', 'Leo Tolstoy', 1877, 'Roman', 3),
            ('Les Trois Mousquetaires', 'Alexandre Dumas', 1844, 'Aventure', 4),
            ('The Brothers Karamazov', 'Fiodor Dostoïevski', 1880, 'Philosophique', 5),
            ('The Grapes of Wrath', 'John Steinbeck', 1939, 'Historique', 7),
            ('Catch-22', 'Joseph Heller', 1961, 'Satire', 2),
            ('One Hundred Years of Solitude', 'Gabriel García Márquez', 1967, 'Magical realism', 8),
            ('The Divine Comedy', 'Dante Alighieri', 1320, 'Poésie', 4)
        ]

    # Fermer la connexion à la base de données
    connection.close()

    # Renvoyer la liste des livres vers le template HTML
    return render_template('accueil.html', livres=livres)

# Démarrer l'application Flask
if __name__ == "__main__":
    app.run(debug=True)
