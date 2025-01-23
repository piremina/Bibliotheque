import sqlite3 #Il s'agit d'une bibliothèque donc il ne faut pas la modifier

# Connexion à la base de données SQLite
connection = sqlite3.connect('bibliotheque.db')

# Lecture et exécution du script SQL pour créer les tables
with open('schema2.sql') as f:
    connection.executescript(f.read())

# Création d'un curseur pour effectuer des opérations sur la base de données
cur = connection.cursor()

# Insertion d'utilisateurs (administrateurs et utilisateurs)
cur.execute("INSERT INTO utilisateurs (nom, prenom, email, role) VALUES (?, ?, ?, ?)", 
            ('DUPONT', 'Emilie', 'emilie.dupont@example.com', 'administrateur'))
cur.execute("INSERT INTO utilisateurs (nom, prenom, email, role) VALUES (?, ?, ?, ?)", 
            ('LEROUX', 'Lucas', 'lucas.leroux@example.com', 'utilisateur'))
cur.execute("INSERT INTO utilisateurs (nom, prenom, email, role) VALUES (?, ?, ?, ?)", 
            ('MARTIN', 'Amandine', 'amandine.martin@example.com', 'utilisateur'))

# Insertion de livres
cur.execute("INSERT INTO livres (titre, auteur) VALUES (?, ?)", ('Les Misérables', 'Victor Hugo'))
cur.execute("INSERT INTO livres (titre, auteur) VALUES (?, ?)", ('1984', 'George Orwell'))
cur.execute("INSERT INTO livres (titre, auteur) VALUES (?, ?)", ('Le Petit Prince', 'Antoine de Saint-Exupéry'))

# Insertion des stocks (exemplaires des livres)
cur.execute("INSERT INTO stock (livre_id, exemplaire_id) VALUES (?, ?)", (1, 1))
cur.execute("INSERT INTO stock (livre_id, exemplaire_id) VALUES (?, ?)", (1, 2))
cur.execute("INSERT INTO stock (livre_id, exemplaire_id) VALUES (?, ?)", (2, 1))
cur.execute("INSERT INTO stock (livre_id, exemplaire_id) VALUES (?, ?)", (3, 1))
cur.execute("INSERT INTO stock (livre_id, exemplaire_id) VALUES (?, ?)", (3, 2))
cur.execute("INSERT INTO stock (livre_id, exemplaire_id) VALUES (?, ?)", (3, 3))

# Insertion d'emprunts
cur.execute("INSERT INTO emprunts (utilisateur_id, livre_id, date_retour_prevue) VALUES (?, ?, ?)", 
            (2, 1, '2025-02-01 12:00:00'))
cur.execute("INSERT INTO emprunts (utilisateur_id, livre_id, date_retour_prevue) VALUES (?, ?, ?)", 
            (3, 3, '2025-02-15 12:00:00'))

# Validation des modifications
connection.commit()

# Fermeture de la connexion
connection.close()
