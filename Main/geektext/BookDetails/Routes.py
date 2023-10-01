from flask import Flask, request, jsonify
from flask import Blueprint
from Main.geektext.BookDetails.BookDetailsRepository import BookDetailsRepository
from Main.geektext.resources.DataAccess import db_connection

book_details = Blueprint('book_details', __name__, url_prefix='/book-details')


@book_details.route("/books/<string:isbn>", methods=['GET', 'POST'])
def get_book(isbn):
    repository = BookDetailsRepository(db_connection)
    """""
    with open('mockdb_books.json', 'r') as f:
        data = json.load(f)
        print("Hi I'm working from BookDetails Routes!")
    """
    """""
        for book in data['books']:
            if book['isbn'] == isbn:
                return jsonify(book)
        else:
            return jsonify({"error": "Book not found"}), 404 # Handle the case when the ISBN is not found
        """
    if request.method == 'GET':
        return jsonify(repository.get_book_by_id(isbn))
    else:
        return jsonify({"error": "Book not found"}), 404  # Handle the case when the ISBN is not found
