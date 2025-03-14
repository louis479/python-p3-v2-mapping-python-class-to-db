from lib import CONN, CURSOR  # Import database connection

class Department:
    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    @classmethod
    def create_table(cls):
        """Create departments table if it does not exist."""
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS departments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                location TEXT NOT NULL
            )
        ''')
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop departments table if it exists."""
        CURSOR.execute('DROP TABLE IF EXISTS departments')
        CONN.commit()

    def save(self):
        """Insert department instance into the database."""
        CURSOR.execute(
            'INSERT INTO departments (name, location) VALUES (?, ?)',
            (self.name, self.location)
        )
        self.id = CURSOR.lastrowid
        CONN.commit()

    @classmethod
    def create(cls, name, location):
        """Creates a new department record and returns an instance."""
        department = cls(name, location)
        department.save()  # Saves it to the database
        return department

    def update(self):
        """Updates the department record in the database."""
        if self.id is not None:
            CURSOR.execute(
                'UPDATE departments SET name = ?, location = ? WHERE id = ?',
                (self.name, self.location, self.id)
            )
            CONN.commit()

    def delete(self):
        """Deletes the department record from the database."""
        if self.id is not None:
            CURSOR.execute('DELETE FROM departments WHERE id = ?', (self.id,))
            CONN.commit()
            self.id = None  # Reset the ID since it's deleted
