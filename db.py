import sqlite3


def connect_to_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def initial_setup():
    conn = connect_to_db()
    conn.execute(
        """
        DROP TABLE IF EXISTS books;
        """
    )
    conn.execute(
        """
        CREATE TABLE books (
          id INTEGER PRIMARY KEY NOT NULL,
          title TEXT,
          author TEXT,
          price INTEGER,
          stock INTEGER
        );
        """
    )
    conn.commit()
    print("Table created successfully")

    books_seed_data = [
        ("The Silent Grove", "Ava Lockwood", 15, 6),
        ("Echoes of the Abyss", "Damian Cross", 18, 5),
        ("The Clockmaker's Secret", "Eleanor Finch", 12, 8),
        ("Moonlit Ashes", "Tobias Wren", 17, 12),
        ("Beneath the Iron Sky", "Julian Mercer", 20, 13)
    ]
    conn.executemany(
        """
        INSERT INTO books (title, author, price, stock)
        VALUES (?,?,?,?)
        """,
        books_seed_data,
    )
    conn.commit()
    print("Seed data created successfully")

    conn.close()


if __name__ == "__main__":
    initial_setup()