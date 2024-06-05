# test_app.py
import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_hello_world(self):
        rv = self.app.get('/')
        self.assertEqual(rv.data.decode('utf-8'), 'Hola Mundo')

if __name__ == "__main__":
    unittest.main()
