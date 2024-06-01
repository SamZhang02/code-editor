import psycopg2
from psycopg2 import Error


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    def __init__(self, db_name, user, password, host, port):
        self.connection = None
        try:
            self.connection = psycopg2.connect(
                dbname=db_name, user=user, password=password, host=host, port=port
            )
            self.cursor = self.connection.cursor()
            print(f"Connected to {db_name} database.")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def execute_query(self, query, params=None):
        if not self.connection:
            print("Cannot execute query, database connection does not exist")
            return

        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
        except Error as e:
            print(f"Error executing query: {e}")

    def execute_read_query(self, query, params=None):
        if not self.connection:
            print("Cannot execute query, database connection does not exist")
            return

        result = None
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except Error as e:
            print(f"Error reading query: {e}")
        return result

    def __del__(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Database connection closed.")


if __name__ == "__main__":
    ...
