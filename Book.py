
from Author import Author


class Book(Author):

    def __init__(self, id, name, email, price, description, image_url):
        Author.__init__(self, id, name, email)
        self.id = id
        self.description = description
        self.price = price
        self.image_url = image_url

    def getBooks(self):
        return f"Id: {self.id} Description:{self.description}Price:{self.price} Image_URL {self.image_url} Author:{Author.getAuthor()}"
