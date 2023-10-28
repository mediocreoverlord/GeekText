from flask import Blueprint
from flask import request, jsonify

from Main.geektext.Book import Book
from Main.geektext.BookDetails.BookDetailsRepository import BookDetailsRepository
from Main.geektext.resources.DataAccess import db_connection

book_details = Blueprint('book_details', __name__, url_prefix='/book-details')


@book_details.route("/books/<string:isbn>", methods=['GET', 'POST'])
def get_book(isbn):
    repository = BookDetailsRepository(
        db_connection)  # repeated calls to this line might make the whole routes file a class and
    # initilize this line first so reptition is eliminated

    if request.method == 'GET':
        return jsonify(repository.get_book_by_id(isbn))
    else:
        return jsonify({"error": "Book not found"}), 404  # possibly delete


@book_details.route("/authors/<string:author_id>", methods=['GET'])
def get_books_list(author_id):
    repository = BookDetailsRepository(db_connection)
    return jsonify(repository.get_books_list(author_id))


''' Parse the data sent by the client.
Check if the author exists in the "authors" table based on the author's name (first_name and last_name).
If the author doesn't exist, create a new author entry in the "authors" table.
Create a new book entry in the "books" table with the book details, including the author's ID.
Return a success response to the client.'''


@book_details.route("/admin/create-book/", methods=['POST'])
def create_book():
    repository = BookDetailsRepository(db_connection)
    if request.method == 'POST':  # !!!look into another way to receive input instead of request form maybe?
        isbn = request.form['isbn']
        title = request.form['title']
        description = request.form['description']
        price = request.form['price']
        author = request.form['author']
        genre = request.form['genre']
        publisher = request.form['publisher']
        year_pub = request.form['year_pub']
        copies_sold = request.form['copies_sold']

        new_book = Book(isbn, title, description, price, author, genre, publisher, year_pub, copies_sold)
        # call repository and send the book object to it
        return (repository.add_book(new_book))
