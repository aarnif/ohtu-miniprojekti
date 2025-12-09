import unittest
from bibtex_generator import create_bibtex
from entities.citation import Citation

class TestCitationRepository(unittest.TestCase):

    def test_empty_input(self):
        result = create_bibtex(None)
        self.assertEqual(result, "")

    def test_generate_bibtex_with_single_input(self):
        entry = Citation(1, "All Night Long", "Mary Jane", "Tammi", "1998", "book", "10.1000/183")
        self.assertEqual(str(entry), "All Night Long, Mary Jane, Tammi, 1998")
        
        result = create_bibtex([entry])
        expected_header = "@Book{Jane1998"
        expected_author = "author = {Mary Jane}"
        expected_doi = "doi = {10.1000/183}"
        
        self.assertIn(expected_header, result)
        self.assertIn(expected_author, result)
        self.assertIn(expected_doi, result)