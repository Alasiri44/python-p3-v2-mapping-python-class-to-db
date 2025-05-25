from __init__ import CURSOR, CONN

class Department:

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"

    @classmethod
    def create_table(cls):
        """Create a table to persist the attributes of department instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS departments(
                id INTEGER PRIMARY KEY,
                name TEXT,
                location TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def drop_table(cls):
        """Drop table that persists department instances """
        sql = """
            DROP TABLE IF EXISTS departments;
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    def save(self):
        """Persist the instances to the database table. Update object attribute using the primary key"""
        sql = """
            INSERT INTO departments(name, location) 
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()
        
        self.id = CURSOR.lastrowid
        
    @classmethod
    def create(cls, name, location):
        """Initialize a new Department instance and save the object to the database """
        department = cls(name, location)
        department.save()
        return department
    
    def update(self):
        """Update an object's corresponding table row"""
        sql = """
            UPDATE departments
            SET name = ?, location = ?
            WHERE id = ?
        """
        
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()
        
    def delete(self):
        """Delete the table row for the specified object"""
        sql = """
            DELETE FROM departments 
            WHERE id = ?    
        """
        
        CURSOR.execute(sql, (self.id,))
        CONN.commit()