import sqlite3

# Connexion à la base de données SQLite (elle sera créée si elle n'existe pas)
connection = sqlite3.connect('database.db')

# Lecture et exécution du script SQL pour créer les tables
with open('schema2.sql') as f:
    connection.executescript(f.read())

# Création d'un curseur pour effectuer des opérations sur la base de données
cur = connection.cursor()

# Insertion de quelques livres avec l'année incluse
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('Les Misérables', 'Victor Hugo', 1862))
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('1984', 'George Orwell', 1949))
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('Le Petit Prince', 'Antoine de Saint-Exupéry', 1943))
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('L’Étranger', 'Albert Camus', 1942))
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('Crime et Châtiment', 'Fiodor Dostoïevski', 1866))

# Insertion de quelques utilisateurs
cur.execute("INSERT INTO utilisateurs (nom, prenom, email, role) VALUES (?, ?, ?, ?)", 
            ('DUPONT', 'Emilie', 'emilie.dupont@example.com', 'administrateur'))
cur.execute("INSERT INTO utilisateurs (nom, prenom, email, role) VALUES (?, ?, ?, ?)", 
            ('LEROUX', 'Lucas', 'lucas.leroux@example.com', 'utilisateur'))

# Validation des modifications
connection.commit()

# Fermeture de la connexion
connection.close()
