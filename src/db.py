import sqlite3
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import logging


class DatabaseError(Exception):
    """Custom exception class for database errors"""

    pass


class Database:
    def __init__(self, db_path):
        self.connection = None
        try:
            self.engine = create_engine(f"sqlite:///{db_path}")
            self.connection = self.engine.connect()
            print(f"Connected to database at {db_path}.")
            self.initialize_tables()
        except SQLAlchemyError as e:
            raise DatabaseError(f"Error connecting to database: {e}")

    def execute_query(self, query, params=None):
        if not self.connection:
            raise DatabaseError(
                "Cannot execute query, database connection does not exist"
            )

        try:
            if params:
                self.connection.execute(text(query), params)
            else:
                self.connection.execute(text(query))
            self.connection.commit()
        except SQLAlchemyError as e:
            raise DatabaseError(f"Error executing query: {e}")

    def execute_read_query(self, query, params=None):
        if not self.connection:
            raise DatabaseError(
                "Cannot execute query, database connection does not exist"
            )

        try:
            if params:
                result = self.connection.execute(text(query), params).fetchall()
            else:
                result = self.connection.execute(text(query)).fetchall()
            return result
        except SQLAlchemyError as e:
            raise DatabaseError(f"Error reading query: {e}")

    def initialize_tables(self):
        query = """
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT NOT NULL,
            timestamp TEXT NOT NULL
        );
        """
        self.execute_query(query)

    def add_submission(self, code: str, timestamp: str):
        insert_query = (
            "INSERT INTO submissions (code, timestamp) VALUES (:code, :timestamp);"
        )
        self.execute_query(insert_query, {"code": code, "timestamp": timestamp})

    def close(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")


if __name__ == "__main__":
    ...
