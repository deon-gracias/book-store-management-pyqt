import sqlite3

class DatabaseConnection:
    def __init__(self, db_path="db/book_store.py"):
        self.connect_to_db(db_path)

        # Create Tables if they do not exist
        self.create_table("Books", [
            ["book_id", "INT", "PRIMARY KEY", "NOT NULL"],
            ["title", "TEXT", "NOT NULL"],
        ])

        print("Initialized Database")

    # Connect to SQLite Database
    # db_path : String with path to database location
    @classmethod
    def connect_to_db(cls, db_path):
        try:
            cls.conn = sqlite3.connect(db_path) # Connect to sqlite
            print("Database Connected ... ")
        except Exception as e:
            print("Database Connection Failed : " + str(e)) # Connection Failed

    def create_table(self, table_name, table_columns):
        try:
            self.conn.execute(f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
            {", ".join(
                map(lambda col: " ".join(col), table_columns)
            )}
            );
            ''')
        except Exception as e:
            print(f"Create table {table_name} Failed : " + str(e))