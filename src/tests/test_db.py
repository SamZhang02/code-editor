import pytest
import os

from src.db import Database


def test_data_persists():
    db = Database("test.db")

    db.initialize_tables()
    db.add_submission("print('hello world!')", "today")
    db.add_submission("print('bye bye world!')", "tomorrow")

    results = db.execute_read_query("SELECT * FROM submissions")

    assert results[0] == (1, "print('hello world!')", "today")
    assert results[1] == (2, "print('bye bye world!')", "tomorrow")

    del db
    os.remove("test.db")


def test_sql_injection_1():
    db = Database("test.db")

    db.initialize_tables()
    injection_code = "print('hello world!'); DROP TABLE submissions; --"
    db.add_submission(injection_code, "today")

    results = db.execute_read_query("SELECT * FROM submissions")
    assert len(results) == 1
    assert results[0] == (1, injection_code, "today")

    db.add_submission("print('bye bye world!')", "tomorrow")
    results = db.execute_read_query("SELECT * FROM submissions")
    assert len(results) == 2

    del db
    os.remove("test.db")


def test_sql_injection_2():
    db = Database("test.db")

    db.initialize_tables()
    injection_code = "'; DROP TABLE submissions; --"
    db.add_submission(injection_code, "today")

    results = db.execute_read_query("SELECT * FROM submissions")
    assert len(results) == 1
    assert results[0] == (1, injection_code, "today")

    db.add_submission("print('bye bye world!')", "tomorrow")
    results = db.execute_read_query("SELECT * FROM submissions")
    assert len(results) == 2

    del db
    os.remove("test.db")
