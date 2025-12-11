class Tag:
    def __init__(self, tag_id, name):
        self.id = tag_id
        self.name = name

    def __str__(self):
        return self.name
