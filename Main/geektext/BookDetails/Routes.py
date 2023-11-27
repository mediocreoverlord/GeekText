from flask import Blueprint
from flask import request

from Main.geektext.Author import Author
from Main.geektext.Book import Book
from Main.geektext.BookDetails.BookDetailsRepository import BookDetailsRepository
from Main.geektext.resources.DataAccess import db_connection

book_details = Blueprint('book_details', __name__, url_prefix='/book-details')

#May reformat file in future into a class?
@book_details.route("/books/<string:isbn>", methods=['GET'])
def get_book(isbn):
    repository = BookDetailsRepository(
        db_connection)  # repeated calls to this line might make the whole routes file a class and
    # initialize this line first so repetition is eliminated
    if request.method == 'GET':
        return repository.get_book_by_id(isbn)


@book_details.route("/authors/<string:author_id>", methods=['GET'])
def get_books_list(author_id):
    repository = BookDetailsRepository(db_connection)
    return repository.get_books_list(author_id)


@book_details.route("/admin/create-book/", methods=['POST'])
def create_book():
    repository = BookDetailsRepository(db_connection)
    if request.method == 'POST':  # !!!look into another way to receive input instead of request form maybe?
        data = request.json
        new_book = Book(**data)

        # call repository and send the book object to it
        return (repository.add_book(new_book))

@book_details.route("/admin/create-author/", methods=['POST'])
def create_author():
    repository = BookDetailsRepository(db_connection)
    if request.method == 'POST':
        data = request.json
        new_author = Author(**data)
        return(repository.add_author(new_author))