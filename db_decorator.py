"""
Simple parameterized decorator example
"""
import unittest
from functools import wraps
import mysql.connector

def mysql_decorator(conn_settings):
    def with_connection(func):
        @wraps(func)
        def _exec(*args, **kwargs):
            conn = mysql.connector.connect(**conn_settings)
            try:
                return func(conn, *args, **kwargs)
            except mysql.connector.Error as mee:
                print "mysql error: '%s', errno: '%s'", mee.msg, mee.errno
            finally:
                conn.close()
        return _exec
    return with_connection

@mysql_decorator({'host':'localhost', 'user':'tst', 'password':'123321', 'database':'tst'})
def one(conn):
    """
    SELECT 1
    """
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    row = cursor.fetchone()
    cursor.close()
    print row
    return row

class TestDecorator(unittest.TestCase):
    def test(self):
        self.assertEqual(one(), (1,))

if __name__ == '__main__':
    unittest.main()
