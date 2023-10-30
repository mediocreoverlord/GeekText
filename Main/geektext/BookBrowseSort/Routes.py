from flask import Blueprint
from flask import request, jsonify

from Main.geektext.Book import Book
from Main.geektext.BookBrowseSort.BookBrowseSortRepo import BookBrowseSortRepo
from Main.geektext.resources.DataAccess import db_connection

book_browse_sort = Blueprint('book_browse_sort', __name__, url_prefix='/book-browse-sort')


@book_browse_sort.route("/books/<string:genre>", methods=['GET', 'POST'])
def get_book(genre):
    repository = BookBrowseSortRepo(db_connection)

    if request.method == 'GET':
        return jsonify(repository.get_book_by_genre(genre))
    else:
        return jsonify({"error": "Book not found"}), 404

@book_browse_sort.route("/books/<string:copies_sold>", methods=['GET', 'POST'])
def get_book(copies_sold):
    repository = BookBrowseSortRepo(db_connection)

    if request.method == 'GET':
        return jsonify(repository.get_books_top_sellers(copies_sold))
    else:
        return jsonify({"error": "Book not found"}), 404


# @book_browse_sort.route("/ratings/<object:book>", methods=['GET'])
# def get_books_list(rating):
#    repository = BookBrowseSortRepo(db_connection)
#    return jsonify(repository.get_books_list(rating))
