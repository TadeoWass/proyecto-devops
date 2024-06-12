import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_hello_world(self):
        rv = self.app.get('/')
        self.assertEqual(rv.data.decode('utf-8'), 'Hola Mundo')

    def test_error_500(self):
        rv = self.app.get('/error500')
        self.assertEqual(rv.status_code, 500)

    def test_error_400(self):
        rv = self.app.get('/error400')
        self.assertEqual(rv.status_code, 400)

if __name__ == "__main__":
    unittest.main()
