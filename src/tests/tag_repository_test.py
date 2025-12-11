import unittest
from sqlalchemy import text
import repositories.tag_repository as tag_repo
from config import db, app
from db_helper import populate_db, setup_db
from data import TAGS


class TestTagRepository(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.context = self.app.app_context()
        self.context.push()
        setup_db()
        populate_db()
        sql = text("DELETE FROM citation_tags")
        db.session.execute(sql)
        db.session.commit()

    def tearDown(self):
        self.context.pop()

    def test_add_tag_to_citation_creates_new_tag_if_not_exists(self):
        tag_repo.add_tag_to_citation(1, "new-tag")
        tags = tag_repo.get_citation_tags(1)
        self.assertIn("new-tag", tags[0].name)

    def test_add_tag_to_citation_uses_existing_tag(self):
        tag_repo.add_tag_to_citation(1, "design")
        tag_repo.add_tag_to_citation(1, "design")
        tags = tag_repo.get_citation_tags(1)
        self.assertEqual(len(tags), 1)

    def test_add_tag_to_citation_adds_to_existing_tags(self):
        tag_repo.add_tag_to_citation(1, "design")
        tag_repo.add_tag_to_citation(1, "programming")
        tags = tag_repo.get_citation_tags(1)
        self.assertEqual(len(tags), 2)

    def test_remove_tag_from_citation(self):
        tag_repo.add_tag_to_citation(1, "design")
        tags = tag_repo.get_citation_tags(1)
        tag_id = tags[0].id
        tag_repo.remove_tag_from_citation(1, tag_id)
        tags_after = tag_repo.get_citation_tags(1)
        self.assertEqual(len(tags_after), 0)

    def test_get_citation_tags_returns_tags_in_alphabetical_order(self):
        tag_repo.add_tag_to_citation(1, "programming")
        tag_repo.add_tag_to_citation(1, "design")
        tag_repo.add_tag_to_citation(1, "architecture")
        tags = tag_repo.get_citation_tags(1)
        tag_names = [tag.name for tag in tags]
        self.assertEqual(tag_names, sorted(tag_names))

    def test_get_all_tags_returns_all_tags(self):
        tags = tag_repo.get_all_tags()
        self.assertEqual(len(tags), len(TAGS))

    def test_get_all_tags_returns_tags_in_alphabetical_order(self):
        tags = tag_repo.get_all_tags()
        tag_names = [tag.name for tag in tags]
        self.assertEqual(tag_names, sorted(tag_names))
