import unittest
from util import validate_citation, UserInputError


class TestCitationValidation(unittest.TestCase):
    def setUp(self):
        self.citation = {"title": "A Great Book", "author": "John Doe",
                         "publisher": "Fiction House", "year": "2020"}

    def test_valid_length_does_not_raise_error(self):
        validate_citation(self.citation["title"], self.citation["author"],
                          self.citation["publisher"], self.citation["year"])

    def test_too_short_or_long_title_raises_error(self):
        with self.assertRaises(UserInputError):
            validate_citation(
                "ok", self.citation["author"], self.citation["publisher"], self.citation["year"])
            validate_citation(
                "okeiz"*21, self.citation["author"], self.citation["publisher"], self.citation["year"])

    def test_too_short_or_long_author_raises_error(self):
        with self.assertRaises(UserInputError):
            validate_citation(
                self.citation["title"], "ok", self.citation["publisher"], self.citation["year"])
            validate_citation(
                self.citation["title"], "okeiz"*21, self.citation["publisher"], self.citation["year"])

    def test_too_short_or_long_publisher_raises_error(self):
        with self.assertRaises(UserInputError):
            validate_citation(
                self.citation["title"], self.citation["author"], "ok", self.citation["year"])
            validate_citation(
                self.citation["title"], self.citation["author"], "okei"*21, self.citation["year"])

    def test_too_short_or_long_year_raises_error(self):
        with self.assertRaises(UserInputError):
            validate_citation(
                self.citation["title"], self.citation["author"], self.citation["publisher"], "1")
            validate_citation(
                self.citation["title"], self.citation["author"], self.citation["publisher"], "20011")

    def test_future_year_raises_error(self):
        with self.assertRaises(UserInputError):
            validate_citation(
                self.citation["title"], self.citation["author"], self.citation["publisher"], "2027")
