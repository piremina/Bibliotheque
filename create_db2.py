import sqlite3

# Connexion à la base de données SQLite (elle sera créée si elle n'existe pas)
connection = sqlite3.connect('database.db')

# Lecture et exécution du script SQL pour créer les tables
with open('schema2.sql') as f:
    connection.executescript(f.read())

# Création d'un curseur pour effectuer des opérations sur la base de données
cur = connection.cursor()

# Insertion de quelques livres avec l'année incluse
cur.execute("INSERT INTO livres (titre, auteur, annee, genre, stock) VALUES (?, ?, ?, ?, ?)", ('Les Misérablesss', 'Victor Hugo', 1862, 'Roman', 5))
cur.execute("INSERT INTO livres (titre, auteur, annee, genre, stock) VALUES (?, ?, ?, ?, ?)", ('1984', 'George Orwell', 1949, 'Dystopie', 3))
cur.execute("INSERT INTO livres (titre, auteur, annee, genre, stock) VALUES (?, ?, ?, ?, ?)", ('Le Petit Prince', 'Antoine de Saint-Exupéry', 1943, 'Conte', 7))
cur.execute("INSERT INTO livres (titre, auteur, annee, genre, stock) VALUES (?, ?, ?, ?, ?)", ('L’Étranger', 'Albert Camus', 1942, 'Philosophique', 4))
cur.execute("INSERT INTO livres (titre, auteur, annee, genre, stock) VALUES (?, ?, ?, ?, ?)", ('Crime et Châtiment', 'Fiodor Dostoïevski', 1866, 'Psychologique', 6))


# Validation des modifications
connection.commit()

# Fermeture de la connexion
connection.close()

print("Livres et utilisateurs ajoutés avec succès.")
