import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_hello_world(self):
        rv = self.app.get('/')
        self.assertEqual(rv.data.decode('utf-8'), 'Hola Mundo')

    def test_bad_request(self):
        # Envía una solicitud que contenga datos no válidos o parámetros incorrectos
        rv = self.app.get('/endpoint?invalidparam=xyz')  # Reemplaza '/endpoint' con la URL de tu API
        self.assertEqual(rv.status_code, 400)
        # Asegúrate de verificar el contenido del mensaje de error también si es necesario
        self.assertIn("Error message expected", rv.data.decode('utf-8'))

    def test_server_error(self):
        # Llama a una ruta que pueda desencadenar una excepción o error interno
        rv = self.app.get('/endpoint/triggerinternalerror')  # Reemplaza '/endpoint/triggerinternalerror' con la URL que puede causar error interno
        self.assertEqual(rv.status_code, 500)
        self.assertIn("Internal Server Error", rv.data.decode('utf-8'))

if __name__ == "__main__":
    unittest.main()
