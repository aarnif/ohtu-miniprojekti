import unittest
from unittest.mock import patch
from config import app, test_env
import app as app_module

class TestApp(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()
    
    def test_index_route(self):
        with patch("repositories.citation_repository.get_citations", return_value=[]):
            res = self.client.get("/")
            self.assertEqual(res.status_code, 200)
