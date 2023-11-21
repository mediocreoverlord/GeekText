class BookBrowseSortRepo:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_books_by_genre(self, genre):
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
        query = "SELECT * FROM books ORDER BY copies_sold DESC LIMIT %s"
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

    def discount_books_by_publisher(self, publisher, discount_percent):
        query = "UPDATE books SET price = price - (price * %s / 100) WHERE publisher = %s"
        self.db_connection.execute_update(query, (discount_percent, publisher))

    def get_books_by_rating(self, rating):
        query = """
        SELECT * FROM books
        WHERE ISBN IN (SELECT ISBN FROM ratings WHERE rating >= %s)
        """
        result = self.db_connection.execute_query(query, (rating,))

        if not result:
            return {"error": "Book list not found for the given rating"}, 404

        books = []
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
            books.append(book_format)
        return books