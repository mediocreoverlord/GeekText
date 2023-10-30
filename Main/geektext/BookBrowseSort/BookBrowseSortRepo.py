# Interacts with the mySQL database and receives the Book object, genre, and copies_sold
# Will update book prices by a discount percent


class BookBrowseSortRepo:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_book_by_genre(self, genre):
        query = "SELECT * FROM books WHERE genre = %s"
        result = self.db_connection.execute_query(query, (genre,))

        if not result:
            return {"error": "Book not found"}, 404

        book = []
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

    def get_books_top_sellers(self, copies_sold):
        query = "SELECT * FROM books WHERE copies_sold = %s"
        result = self.db_connection.execute_query(query, (copies_sold,))

        if not result:
            return {"error": "Book list not found for top sellers"}, 404

        book = []
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


# def get_books_by_rating(self, copies_sold):
    # query = "SELECT * FROM books WHERE copies_sold = %s"
    # query = SELECT (all book columns)
    #         FROM books b
    #         JOIN ratings r
    #         ON b.ISBN = r.ISBN
    #result = self.db_connection.execute_query(query, (,)) # set parameter to book object
    #if not result:
    #    return {"error": "Book list not found for top sellers"}, 404

    #return result