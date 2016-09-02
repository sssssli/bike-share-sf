import sqlite3
import pandas as pd
import os


def open_connection_sqlite ():
    """
    Opens and sets sqlite connection
    """
    #cwd = os.getcwd()
    db = 'database.sqlite'.format(cwd=cwd)
    try:
        conn_sqlite = sqlite3.connect(db)
        # autocommit
        conn_sqlite.isolation_level = None
        curs_sqlite = conn_sqlite.cursor()
    except sqlite3.Error as err:
        logging.exception('cannot open sqlite connection')
        raise
    return (conn_sqlite, curs_sqlite)

conn_sqlite, curs_sqlite = open_connection_sqlite()
