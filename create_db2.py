import sqlite3

# Connexion à la base de données SQLite (elle sera créée si elle n'existe pas)
connection = sqlite3.connect('database.db')

# Lecture et exécution du script SQL pour créer les tables
with open('schema2.sql') as f:
    connection.executescript(f.read())

# Création d'un curseur pour effectuer des opérations sur la base de données
cur = connection.cursor()

# Insertion de 15 livres
livres = [
    ('Les Misérables', 'Victor Hugo', 1862, 'Roman historique', 5),
    ('1984', 'George Orwell', 1949, 'Dystopie', 3),
    ('Le Petit Prince', 'Antoine de Saint-Exupéry', 1943, 'Conte', 10),
    ('L’Étranger', 'Albert Camus', 1942, 'Philosophie', 4),
    ('Crime et Châtiment', 'Fiodor Dostoïevski', 1866, 'Roman', 2),
    ('À la recherche du temps perdu', 'Marcel Proust', 1913, 'Classique', 3),
    ('Don Quichotte', 'Miguel de Cervantes', 1605, 'Aventure', 4),
    ('Guerre et Paix', 'Léon Tolstoï', 1869, 'Roman historique', 3),
    ('Orgueil et Préjugés', 'Jane Austen', 1813, 'Romance', 6),
    ('Les Fleurs du Mal', 'Charles Baudelaire', 1857, 'Poésie', 5),
    ('Harry Potter à l\'École des Sorciers', 'J.K. Rowling', 1997, 'Fantastique', 8),
    ('L\'Odyssée', 'Homère', -800, 'Épopée', 7),
    ('Le Comte de Monte-Cristo', 'Alexandre Dumas', 1844, 'Aventure', 5),
    ('Ulysse', 'James Joyce', 1922, 'Modernisme', 2),
    ('Madame Bovary', 'Gustave Flaubert', 1857, 'Roman', 4)
]

cur.executemany(
    "INSERT INTO livres (titre, auteur, annee, genre, stock) VALUES (?, ?, ?, ?, ?)", livres
)

# Insertion de 7 utilisateurs
utilisateurs = [
    ('DUPONT', 'Emilie', 'emilie.dupont@example.com', 'password123', 'administrateur'),
    ('LEROUX', 'Lucas', 'lucas.leroux@example.com', 'password123', 'utilisateur'),
    ('MARTIN', 'Sophie', 'sophie.martin@example.com', 'password456', 'utilisateur'),
    ('MOREAU', 'Julien', 'julien.moreau@example.com', 'password789', 'utilisateur'),
    ('GARCIA', 'Clara', 'clara.garcia@example.com', 'password321', 'administrateur'),
    ('ROUX', 'Paul', 'paul.roux@example.com', 'password654', 'utilisateur'),
    ('LEGRAND', 'Marie', 'marie.legrand@example.com', 'password987', 'utilisateur')
]

cur.executemany(
    "INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe, role) VALUES (?, ?, ?, ?, ?)", utilisateurs
)

# Validation des modifications
connection.commit()

# Fermeture de la connexion
connection.close()
