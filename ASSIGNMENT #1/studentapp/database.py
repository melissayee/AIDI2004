"""
File to create database connection, including creating database file with tables
"""

import sqlite3

from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"C:\Users\melissa\OneDrive\Documents\DURHAM COLLEGE\AIDI\1B\AIDI 2004 - AI In Enterprise Systems\ASSIGNMENTS\ASSIGNMENT #1\studentapp\db\students.db"

    # Creates the student table
    sql_create_students_table = """ CREATE TABLE IF NOT EXISTS students (
                                        student_id integer PRIMARY KEY,
                                        first_name text NOT NULL,
                                        last_name text NOT NULL,
                                        date_of_birth text NOT NULL,
                                        amount_due float NOT NULL,
                                        date_entered text NOT NULL
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create students table
        create_table(conn, sql_create_students_table)

    else:
        print("Error: Cannot create database connection.")


if __name__ == '__main__':
    main()