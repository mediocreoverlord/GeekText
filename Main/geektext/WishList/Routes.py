from flask import Blueprint, request, jsonify

from Main.geektext.WishList.WishListRepository import WishListRepository
from .WishListRepository import WishListRepository
from Main.geektext.resources.DataAccess import db_connection

Wishlist = Blueprint('Wishlist', __name__, url_prefix='/Wishlist')

repo = WishListRepository(db_connection)


# Create Wishlist
@Wishlist.route('/create_wishlist', methods=['POST'])
def create_wishlist():
    iduser = request.json['iduser']
    wishlistName = request.json['WishListName']

    result = repo.create_wishlist(iduser, wishlistName)

    if "error" in result:
        return jsonify(result)
    return jsonify({"message": "Wishlist created successfully!"})


# whislist of said user
@Wishlist.route('/user/<int:iduser>/wishlists', methods=['GET'])
def get_user_wishlists(iduser):
    wishlists = repo.get_wishlists_by_user(iduser)
    if wishlists:
        return jsonify(wishlists)
    else:
        return jsonify({"message": f"No wishlists found for user {iduser}."})


# add a book by isbn to a wishlist

@Wishlist.route('/<int:idwishlist>/add_book', methods=['POST'])
def add_book(idwishlist):
    data = request.get_json()
    isbn = data['isbn']
    result = repo.add_book_to_wishlist(idwishlist, isbn)
    return jsonify(result)


# remove a book by isbn from a wishlist add to shopping cart

@Wishlist.route('/<int:idwishlist>/remove_book', methods=['DELETE'])
def remove_book(idwishlist):
    data = request.get_json()
    isbn = data['isbn']
    iduser = data['iduser']
    result = repo.remove_book_from_wishlist(idwishlist, isbn, iduser)
    return jsonify(result)


# What books are in a whislist
@Wishlist.route('/<int:idwishlist>/books', methods=['GET'])
def get_books_in_wishlist(idwishlist):
    try:
        books = repo.get_books_in_wishlist(idwishlist)
        return jsonify(books)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"})
