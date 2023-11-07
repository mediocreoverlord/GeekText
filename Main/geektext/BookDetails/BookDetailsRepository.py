# Interacts with the mySQL database and receives the Book object and its attributes.
from flask import jsonify


class BookDetailsRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_book_by_id(self, isbn):  # alter possibly to display author name and not id when author object is created
        query = "SELECT * FROM books WHERE isbn = %s" #check why this is highlighted?
        result = self.db_connection.execute_query(query, (isbn,))

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
        return jsonify(book)

    def get_books_list(self, author_id):
        query = "SELECT * FROM books WHERE author_id = %s"
        result = self.db_connection.execute_query(query, (author_id,))

        if not result:
            return {"error": "Book list not found for author"}, 404

        return jsonify (result)

    def add_book(self, new_book):  # add query for inserting new book in db
        query = "INSERT INTO books VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (new_book.isbn, new_book.title, new_book.description, new_book.price, new_book.author, new_book.genre,
                new_book.publisher, new_book.year_pub, new_book.copies_sold)

        try:
            self.db_connection.execute_query(query, data)
            self.db_connection.connection.commit()  # Commit the transaction to the database!
            return {"success": "Book added successfully"}
        except Exception as e:
            print(f"Error adding book: {e}")
            return {"error": "An error occurred while trying to add the book"}, 500