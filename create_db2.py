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
cur.execute("INSERT INTO livres (titre, auteur, annee, genre, stock) VALUES (?, ?, ?, ?, ?)", ('Orgueil et Préjugés', 'Jane Austen', 1813, 'Roman', 8))
cur.execute("INSERT INTO livres (titre, auteur, annee, genre, stock) VALUES (?, ?, ?, ?, ?)", ('Moby Dick', 'Herman Melville', 1851, 'Aventure', 5))
cur.execute("INSERT INTO livres (titre, auteur, annee, genre, stock) VALUES (?, ?, ?, ?, ?)", ('Don Quichotte', 'Miguel de Cervantes', 1605, 'Roman', 4))
cur.execute("INSERT INTO livres (titre, auteur, annee, genre, stock) VALUES (?, ?, ?, ?, ?)", ('La Métamorphose', 'Franz Kafka', 1915, 'Fantastique', 6))
cur.execute("INSERT INTO livres (titre, auteur, annee, genre, stock) VALUES (?, ?, ?, ?, ?)", ('Les Fleurs du mal', 'Charles Baudelaire', 1857, 'Poésie', 7))
cur.execute("INSERT INTO livres (titre, auteur, annee, genre, stock) VALUES (?, ?, ?, ?, ?)", ('Le Comte de Monte-Cristo', 'Alexandre Dumas', 1844, 'Aventure', 5))
cur.execute("INSERT INTO livres (titre, auteur, annee, genre, stock) VALUES (?, ?, ?, ?, ?)", ('Ulysse', 'James Joyce', 1922, 'Modernisme', 3))
cur.execute("INSERT INTO livres (titre, auteur, annee, genre, stock) VALUES (?, ?, ?, ?, ?)", ('Madame Bovary', 'Gustave Flaubert', 1857, 'Réalisme', 6))
cur.execute("INSERT INTO livres (titre, auteur, annee, genre, stock) VALUES (?, ?, ?, ?, ?)", ('Guerre et Paix', 'Léon Tolstoï', 1869, 'Historique', 4))
cur.execute("INSERT INTO livres (titre, auteur, annee, genre, stock) VALUES (?, ?, ?, ?, ?)", ('L’Odyssée', 'Homère', -800, 'Épopée', 5))

# Insertion des utilisateurs et administrateurs (avec un mot de passe simple)
cur.execute("INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe, role) VALUES (?, ?, ?, ?, ?)", 
            ('Dupont', 'Jean', 'jean.dupont@example.com', 'userpass', 'utilisateur'))
cur.execute("INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe, role) VALUES (?, ?, ?, ?, ?)", 
            ('Admin', 'Marie', 'admin@example.com', 'adminpass', 'administrateur'))

# Validation des modifications
connection.commit()

# Fermeture de la connexion
connection.close()

print("Livres et utilisateurs ajoutés avec succès.")
