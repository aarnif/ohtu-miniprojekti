CREATE TYPE citation_type AS ENUM ('article', 'book', 'booklet', 'conference', 'inbook', 'incollection', 'inproceedings', 'manual', 'mastersthesis', 'misc', 'phdthesis', 'proceedings', 'techreport', 'unpublished');

CREATE TABLE citations (
  id SERIAL PRIMARY KEY,
  citation_type citation_type NOT NULL DEFAULT 'book',
  author TEXT NOT NULL,
  title TEXT NOT NULL,
  publisher TEXT NOT NULL,
  year INTEGER,
  doi TEXT
);

CREATE TABLE tags (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL UNIQUE
);

CREATE TABLE citation_tags (
  citation_id INTEGER NOT NULL REFERENCES citations(id) ON DELETE CASCADE,
  tag_id INTEGER NOT NULL REFERENCES tags(id) ON DELETE CASCADE,
  PRIMARY KEY (citation_id, tag_id)
);