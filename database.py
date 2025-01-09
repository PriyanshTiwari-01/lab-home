import sqlite3
import hashlib

# Hashing the password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Create the database and users table
def create_db():
    # Use 'with' for better handling of the connection (automatically closes)
    with sqlite3.connect("users.db") as con:
        cursor = con.cursor()

        # Create users table if it doesn't already exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT NOT NULL,
                            password TEXT NOT NULL
                        )''')

        # Sample users to insert into the database
        sample_users = [
            ("john_doe", hash_password("password123")),
            ("alice_smith", hash_password("alicepassword")),
            ("bob_jones", hash_password("bobpassword")),
        ]

        # Insert sample users into the database
        cursor.executemany('''INSERT INTO users (username, password) VALUES (?, ?)''', sample_users)

        # Commit changes and close connection
        con.commit()

# Create the database and insert users
create_db()
