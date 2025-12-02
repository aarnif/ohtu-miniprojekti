class UserInputError(Exception):
    pass


def validate_citation(title, author, publisher, year, citation_type):
    if not citation_type or citation_type == "":
        raise UserInputError("Citation type is required")

    if len(title) < 3 or len(title) > 100:
        raise UserInputError("Title length must be between 3 and 100")

    if len(author) < 3 or len(author) > 100:
        raise UserInputError("Author length must be between 3 and 100")

    if len(publisher) < 3 or len(publisher) > 100:
        raise UserInputError("Publisher length must be between 3 and 100")

    if len(year) != 4:
        raise UserInputError("Year length must be 4.")

    if int(year) > 2025:
        raise UserInputError("Year can not be in the future.")
