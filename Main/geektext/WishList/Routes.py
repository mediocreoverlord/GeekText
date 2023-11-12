from flask import Blueprint, request, jsonify
from .WishListRepository import WishListRepository
from Main.geektext.resources.DataAccess import db_connection

Wishlist = Blueprint('Wishlist', __name__, url_prefix='/Wishlist')

repo = WishListRepository(db_connection)

#Create Wishlist
@Wishlist.route('/wishlist', methods=['POST'])
def create_wishlist():
    user_id = request.json['UserId']
    wishlist_name = request.json['WishListName']

    result = repo.create_wishlist(user_id, wishlist_name)

    if "error" in result:
        return jsonify(result)
    return jsonify({"message": "Wishlist created successfully!"})

# whislist of said user
@Wishlist.route('/user/<int:user_id>/wishlists', methods=['GET'])
def get_user_wishlists(user_id):
    wishlists = repo.get_wishlists_by_user(user_id)
    if wishlists:
        return jsonify(wishlists)
    else:
        return jsonify({"message": f"No wishlists found for user {user_id}."})

# add a book by isbn to a wishlist

@Wishlist.route('/wishlist/<int:wishlist_id>/add_book', methods=['POST'])
def add_book(wishlist_id):
    data = request.get_json()
    isbn = data['isbn']
    result = repo.add_book_to_wishlist(wishlist_id, isbn)
    return jsonify(result)

# remove a book by isbn from a wishlist , Still working in it

@Wishlist.route('/wishlist/<int:wishlist_id>/remove_book', methods=['DELETE'])
def remove_book(wishlist_id):
    data = request.get_json()
    isbn = data['isbn']
    result = repo.remove_book_from_wishlist(wishlist_id, isbn)
    return jsonify(result)

#What books are in a whislist
@Wishlist.route('/wishlist/<int:wishlist_id>/books', methods=['GET'])
def get_books_in_wishlist(wishlist_id):
    try:
        books = repo.get_books_in_wishlist(wishlist_id)
        return jsonify(books)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"})