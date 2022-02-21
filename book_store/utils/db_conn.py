import sqlite3

class DatabaseConnection:
    def __init__(self, db_path):
        self.connect_to_db(db_path)

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

    def create_table(self, table_name, table_columns, if_not_exists=False):
        try:
            if if_not_exists:
                self.conn.execute(f'''
                CREATE TABLE IF NOT EXISTS {table_name} (
                {", ".join(
                    map(lambda col: " ".join(col), table_columns)
                )}
                );
                ''')
            else:
                self.conn.execute(f'''
                CREATE TABLE {table_name} (
                {", ".join(
                    map(lambda col: " ".join(col), table_columns)
                )}
                );
                ''')
        except Exception as e:
            print(f"Create table {table_name} Failed : " + str(e))

    def select_table(self, table, columns):
        try:
            self.conn.execute(f'''
            SELECT {"".join("")}
            ''')
        except Exception as e:
            print(f"Select table {table_name} failed : " + str(e))

class BookStoreDb(DatabaseConnection):
    def __init__(self):
        super().__init__("db/book_store.db")
        self.setupdb()

    def setupdb(self):
        # Customers
        super().create_table("customers",[
            ["customer_id", "integer", "primary key", "autoincrement"],
            ["first_name", "text"],
            ["last_name", "text"],
            ["phone", "integer"],
        ], if_not_exists=True)

        # Orders
        super().create_table("orders",[
            ["order_id", "integer", "primary key", "autoincrement"],
            ["customer_id", "integer", "not null"],
            ["total", "float"],
            ["foreign key", "(customer_id) references customers(customer_id)"]
        ], if_not_exists=True)

        # Order Items
        super().create_table("orderitems",[
            ["order_id", "integer", "not null"],
            ["customer_id", "integer", "not null"],
            ["isbn", "varchar", "not null"],
            ["purchased_on", "datetime", "not null"],
            ["foreign key", "(order_id) references orders(order_id)"],
            ["foreign key", "(customer_id) references customers(customer_id)"],
            ["foreign key", "(isbn) references books(isbn)"]
        ], if_not_exists=True)

        # Publisher
        super().create_table("publishers",[
            ["publisher_id", "integer", "primary key"],
            ["name", "text"]
        ], if_not_exists=True)

        # Inventory
        super().create_table("inventory",[
            ["isbn", "varchar", "primary key"],
            ["sold", "integer"],
            ["total", "integer"],
            ["last_updated", "datetime"],
            ["foreign", "key", "(isbn) references books(isbn)"]
        ], if_not_exists=True)

        # Authors
        super().create_table("authors",[
            ["author_id", "integer", "primary key autoincrement"],
            ["name", "varchar", "not null"]
        ], if_not_exists=True)

        # Books
        super().create_table("books",[
            ["isbn", "varchar", "primary key"],
            ["name", "varchar"],
            ["author_id", "integer"],
            ["publisher_id", "integer"],
            ["order_id", "integer"],
            ["foreign key", "(author_id)", "references author(author_id)"],
            ["foreign key", "(publisher_id) references publisher(publisher_id)"],
            ["foreign key", "(order_id) references orders(order_id)"],
            ["foreign key", "(isbn) references inventory(isbn)"]
        ], if_not_exists=True)