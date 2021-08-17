
class Author():
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def getAuthor(self):
        return f"ID:{self.id} Name:{self.name} Age:{self.email}"
