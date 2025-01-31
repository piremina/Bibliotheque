import sqlite3

# Connexion à la base de données SQLite (elle sera créée si elle n'existe pas)
connection = sqlite3.connect('database.db')

# Lecture et exécution du script SQL pour créer les tables
with open('schema2.sql') as f:
    connection.executescript(f.read())

# Création d'un curseur pour effectuer des opérations sur la base de données
cur = connection.cursor()

# Insertion de quelques livres avec l'année incluse
cur.execute("INSERT INTO livres (titre, auteur, annee, genre, stock) VALUES (?, ?, ?, ?, ?)", ('Les Misérables', 'Victor Hugo', 1862, 'Roman', 5))
cur.execute("INSERT INTO livres (titre, auteur, annee, genre, stock) VALUES (?, ?, ?, ?, ?)", ('1984', 'George Orwell', 1949, 'Dystopie', 3))
cur.execute("INSERT INTO livres (titre, auteur, annee, genre, stock) VALUES (?, ?, ?, ?, ?)", ('Le Petit Prince', 'Antoine de Saint-Exupéry', 1943, 'Conte', 7))
cur.execute("INSERT INTO livres (titre, auteur, annee, genre, stock) VALUES (?, ?, ?, ?, ?)", ('L’Étranger', 'Albert Camus', 1942, 'Philosophique', 4))
cur.execute("INSERT INTO livres (titre, auteur, annee, genre, stock) VALUES (?, ?, ?, ?, ?)", ('Crime et Châtiment', 'Fiodor Dostoïevski', 1866, 'Psychologique', 6))

# Ajout de nombreux autres livres
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

# Insertion des livres supplémentaires dans la table
cur.executemany("INSERT INTO livres (titre, auteur, annee, genre, stock) VALUES (?, ?, ?, ?, ?)", livres)

# Insertion de quelques utilisateurs
cur.execute("INSERT INTO utilisateurs (nom, prenom, email, role) VALUES (?, ?, ?, ?)", 
            ('DUPONT', 'Emilie', 'emilie.dupont@example.com', 'administrateur'))
cur.execute("INSERT INTO utilisateurs (nom, prenom, email, role) VALUES (?, ?, ?, ?)", 
            ('LEROUX', 'Lucas', 'lucas.leroux@example.com', 'utilisateur'))

# Validation des modifications
connection.commit()

# Fermeture de la connexion
connection.close()

print("Livres et utilisateurs ajoutés avec succès.")
