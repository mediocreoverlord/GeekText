# Import necessary modules and classes
from flask import Blueprint, request, jsonify
from Main.geektext.Book import Book
from Main.geektext.BookBrowseSort.BookBrowseSortRepo import BookBrowseSortRepo
from Main.geektext.resources.DataAccess import db_connection

# Create a Blueprint for book browse and sort
book_browse_sort = Blueprint('book_browse_sort', __name__, url_prefix='/book-browse-sort')


# Define route for retrieving a list of books by genre
@book_browse_sort.route("/books/genre/<string:genre>", methods=['GET'])
def get_books_by_genre(genre):
    repository = BookBrowseSortRepo(db_connection)

    if request.method == 'GET':
        return jsonify(repository.get_books_by_genre(genre))
    else:
        return jsonify({"error": "Invalid request method"}), 400


# Define route for retrieving a list of top sellers
@book_browse_sort.route("/books/top-sellers", methods=['GET'])
def get_books_top_sellers():
    repository = BookBrowseSortRepo(db_connection)

    if request.method == 'GET':
        return jsonify(repository.get_books_top_sellers(copies_sold=3))
    else:
        return jsonify({"error": "Invalid request method"}), 400


# Define route for retrieving a list of books by rating and higher
@book_browse_sort.route("/books/rating/<float:rating>", methods=['GET'])
def get_books_by_rating(rating):
    repository = BookBrowseSortRepo(db_connection)

    if request.method == 'GET':
        return jsonify(repository.get_books_by_rating(rating))
    else:
        return jsonify({"error": "Invalid request method"}), 400


# Define route for discounting books by publisher
@book_browse_sort.route("/books/discount", methods=['PUT'])
def discount_books_by_publisher():
    repository = BookBrowseSortRepo(db_connection)

    if request.method == 'PUT':
        # Get discount percent and publisher from request data
        data = request.get_json()
        discount_percent = data.get('discount_percent')
        publisher = data.get('publisher')

        # Check if required parameters are present
        if discount_percent is None or publisher is None:
            return jsonify({"error": "Missing required parameters"}), 400

        # Update the price of books and return success
        repository.discount_books_by_publisher(publisher, discount_percent)
        return jsonify({"message": "Books discounted successfully"})
    else:
        return jsonify({"error": "Invalid request method"}), 400
