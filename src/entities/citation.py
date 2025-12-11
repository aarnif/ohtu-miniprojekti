# pylint: disable=too-many-instance-attributes
class Citation:
    def __init__(self, citation_id, title, author, publisher, year, citation_type="book", doi=None, tags=None):
        self.citation_id = citation_id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.citation_type = citation_type
        self.doi = doi
        self.tags = tags or []

    def __str__(self):
        return f"{self.title}, {self.author}, {self.publisher}, {self.year}"
