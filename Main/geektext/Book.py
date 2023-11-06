# book class to store values passed in by client

class Book: #This is a book object where book data can be stored and retrieved.
    def __init__(self, isbn, title, description, price, author,
                 genre, publisher, year_pub, copies_sold):
        self.isbn = isbn
        self.title = title
        self.description = description
        self.price = price
        self.author = author
        self.genre = genre
        self.publisher = publisher
        self.year_pub = year_pub
        self.copies_sold = copies_sold

