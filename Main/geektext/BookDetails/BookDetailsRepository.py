# Interacts with the mySQL database and receives the Book object and its attributes.


class BookDetailsRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_book_by_id(self, isbn):  # do error checking if the book is not found return error for that
        query = "SELECT * FROM books WHERE isbn = %s" #check why this is highlighted?
        result = self.db_connection.execute_query(query, (isbn,))

        if not result:
            return {"error": "Book not found"}

        book = []   #NOTE!!! When output the key values are in alphabetical order? Figure this out
        for row in result:
            book_format = {
                "isbn": row[0],
                "title": row[1],
                "description": row[2],
                "price": row[3],
                "author_id": row[4],
                "genre": row[5],
                "publication": row[6],
                "year": row[7],
                "copies_sold": row[8],
            }
            book.append(book_format)
        return book

    # add more query methods
