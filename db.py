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
        DROP TABLE IF EXISTS customers;
        """
    )
    conn.execute(
        """
        DROP TABLE IF EXISTS orders;
        """
    )
    # Add books column
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

    #Add customers column
    conn.execute(
        
        """
        CREATE TABLE customers (
        id INTEGER PRIMARY KEY NOT NULL,
        name TEXT,
        email TEXT,
        phone_number TEXT
        );
        """
    )

    customers_seed_data = [
        ("Nathaniel", "nathaniel@email.com", "444-444-4443"),
        ("Bobert", "bobert@email.com", "444-444-4442")
    ]

    conn.executemany(
        """
        INSERT INTO customers (name, email, phone_number)
        VALUES (?,?,?)
        """,
        customers_seed_data,
    )
    conn.commit()

    print("Seed data created successfully")

# adds orders column

    conn.execute(
     
        """
        CREATE TABLE orders (
        id INTEGER PRIMARY KEY NOT NULL,
        customer_id INTEGER,
        book_id INTEGER,
        quantity INTEGER,
        order_date TEXT,
        status TEXT
        );
        """
    )
    orders_seed_data = [
    (1, 1, 1, "3/4/2025", "ordered"),
    (1, 2, 1, "3/4/2025", "ordered"),
    (1, 4, 2, "3/4/2025", "ordered"),
    (2, 2, 1, None, "in basket"),
    (2, 5, 1, None, "in basket")
    ]

    conn.executemany(
        """
        INSERT INTO orders (customer_id, book_id, quantity, order_date, status)
        VALUES (?,?,?,?,?)
        """,
        orders_seed_data
    )
    conn.commit()
    print("Seed data created successfully")

    conn.close()


if __name__ == "__main__":
    initial_setup()

def books_all():
    conn = connect_to_db()
    rows = conn.execute(
        """
        SELECT * FROM books
        """
    ).fetchall()
    return [dict(row) for row in rows]