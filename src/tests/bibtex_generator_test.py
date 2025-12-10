import unittest
from bibtex_generator import create_bibtex
from entities.citation import Citation

class TestBibtexGenerator(unittest.TestCase):

    def test_empty_input(self):
        result = create_bibtex(None)
        self.assertEqual(result, "")

    def test_generate_bibtex_with_single_input(self):
        entry = Citation(1, "Das Kapital", "Karl Marx", "Otto Meissner", "1867", "book", "10.1000/183")
        self.assertEqual(str(entry), "Das Kapital, Karl Marx, Otto Meissner, 1867")
        
        result = create_bibtex([entry])
        expected_header = "@Book{Marx1867"
        expected_author = "author = {Karl Marx}"
        expected_doi = "doi = {10.1000/183}"
        
        self.assertIn(expected_header, result)
        self.assertIn(expected_author, result)
        self.assertIn(expected_doi, result)