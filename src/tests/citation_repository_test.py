import repositories.citation_repository as cit_repo
import unittest
from app import app


class TestCitationRepository(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.context = self.app.app_context()
        self.context.push()

    def tearDown(self):
        self.context.pop()

    def test_citations_are_recieved(self):
        citations = cit_repo.get_citations("", "", "")
        self.assertTrue(len(citations) > 0)

        citation_id = citations[-1].citation_id
        citation = cit_repo.get_citation_by_id(citation_id)
        self.assertIsNotNone(citation)

    def test_citations_are_recieved_with_doi_or_year(self):
        cit_repo.create_citation("Boom Kah", "Robin", "Universal", "2013", "article", "10.1000/183")
        citation_by_doi = cit_repo.get_citations("https://doi.org/10.1000/183", "", "")
        self.assertIsNotNone(citation_by_doi)

        citations_by_year = cit_repo.get_citations("2013", "", "")
        self.assertIsNotNone(citations_by_year)

    def test_citations_searched_with_query_and_sort(self):
        cit_repo.create_citation("The Beauty of Code", "Tdot", "Universal", "2022", "book", "10.1000/782")
        citations = cit_repo.get_citations("code", "title", "book")
        self.assertTrue(len(citations) > 0)

    def test_citation_is_successfully_created(self):
        before = len(cit_repo.get_citations("", "", ""))
        cit_repo.create_citation("All Night Long", "Marvin Gaye", "Tammi", "1998", "article", "10.1000/182")
        after = len(cit_repo.get_citations("", "", ""))
        self.assertEqual(before + 1, after)

    def test_citation_is_successfully_deleted(self):

        cit_repo.create_citation("Norwegian Wood", "Haruki Murakami", "Tammi", "1987", "book", "10.1000/186")
        citations_before = cit_repo.get_citations("", "", "")
        last_citation = citations_before[-1]
        citation_id = last_citation.citation_id

        cit_repo.delete_citation(citation_id)

        citations_after = cit_repo.get_citations("", "", "")
        ids_after = [c.citation_id for c in citations_after]

        self.assertNotIn(citation_id, ids_after)

    def test_citation_is_successfully_edited(self):
        cit_repo.create_citation("Charlie And The Chocolate Factory", "Roald Dahl", "Scholastic", "1964", "book", "10.1000/999")

        citations = cit_repo.get_citations("", "", "")
        citation = citations[-1]
        citation_id = citation.citation_id

        cit_repo.edit_citation(citation_id, "Charlie And The Chocolate Factory", "Roald Dahl", "Pearson", "1964", "book", "10.1000/879")
        updated = cit_repo.get_citation_by_id(citation_id)

        self.assertEqual(updated.title, "Charlie And The Chocolate Factory")
        self.assertEqual(updated.doi, "10.1000/879")
        self.assertEqual(updated.publisher, "Pearson")
