import sqlite3

# Connexion à la base de données SQLite (elle sera créée si elle n'existe pas)
connection = sqlite3.connect('database.db')

# Lecture et exécution du script SQL pour créer les tables
with open('schema2.sql') as f:
    connection.executescript(f.read())

# Création d'un curseur pour effectuer des opérations sur la base de données
cur = connection.cursor()

# Insertion de plusieurs livres avec l'année incluse
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('Les Misérables', 'Victor Hugo', 1862))
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('1984', 'George Orwell', 1949))
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('Le Petit Prince', 'Antoine de Saint-Exupéry', 1943))
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('L’Étranger', 'Albert Camus', 1942))
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('Crime et Châtiment', 'Fiodor Dostoïevski', 1866))
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('À la recherche du temps perdu', 'Marcel Proust', 1913))
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('Don Quichotte', 'Miguel de Cervantes', 1605))
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('Guerre et Paix', 'Léon Tolstoï', 1869))
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('Orgueil et Préjugés', 'Jane Austen', 1813))
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('Les Fleurs du Mal', 'Charles Baudelaire', 1857))
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('Harry Potter à l\'École des Sorciers', 'J.K. Rowling', 1997))
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('L\'Odyssée', 'Homère', -800))
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('Le Comte de Monte-Cristo', 'Alexandre Dumas', 1844))
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('Ulysse', 'James Joyce', 1922))
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('Madame Bovary', 'Gustave Flaubert', 1857))
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('Le Rouge et le Noir', 'Stendhal', 1830))
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('Les Frères Karamazov', 'Fiodor Dostoïevski', 1880))
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('Le Meilleur des mondes', 'Aldous Huxley', 1932))
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('Candide', 'Voltaire', 1759))
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('La Métamorphose', 'Franz Kafka', 1915))
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('L\'Alchimiste', 'Paulo Coelho', 1988))
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('Le Seigneur des Anneaux', 'J.R.R. Tolkien', 1954))
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('Moby Dick', 'Herman Melville', 1851))
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('Les Hauts de Hurlevent', 'Emily Brontë', 1847))
cur.execute("INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)", ('Jane Eyre', 'Charlotte Brontë', 1847))

# Insertion de quelques utilisateurs
cur.execute("INSERT INTO utilisateurs (nom, prenom, email, role) VALUES (?, ?, ?, ?)", 
            ('DUPONT', 'Emilie', 'emilie.dupont@example.com', 'administrateur'))
cur.execute("INSERT INTO utilisateurs (nom, prenom, email, role) VALUES (?, ?, ?, ?)", 
            ('LEROUX', 'Lucas', 'lucas.leroux@example.com', 'utilisateur'))

# Validation des modifications
connection.commit()

# Fermeture de la connexion
connection.close()
