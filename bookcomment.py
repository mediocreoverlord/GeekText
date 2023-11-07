
from flask import request, jsonify
import sys
from Main.geektext.BookDetails.app import app



#  Database structure of the ratings and comments
ratings = []
comments = []

# Creating the ratings for the book with Tentative variables
@app.route('/ratings', methods=['POST'])
def create_rating():
    data = request.json
    user_id = data['user_id']
    book_id = data['book_id']
    rating = data['rating']

    # Put the rating into the list
    ratings.append({
        'user_id': user_id,
        'book_id': book_id,
        'rating': rating
    })

    return '', 201  # Gives indication of created response

# Creating comment for the book
@app.route('/comments', methods=['POST'])
def create_comment():
    data = request.json
    user_id = data['user_id']
    book_id = data['book_id']
    comment = data['comment']

    # Add the comment to the comments list
    comments.append({
        'user_id': user_id,
        'book_id': book_id,
        'comment': comment
    })

    return '', 201  

# Retrieve comments for a particular book
@app.route('/comments/<int:book_id>', methods=['GET'])
def get_comments(book_id):
    book_comments = [c for c in comments if c['book_id'] == book_id]
    return jsonify(book_comments)

# Retrieve the average rating for a book
def get_average_rating(book_id):
    book_ratings = [r['rating'] for r in ratings if r['book_id'] == book_id]

    if not book_ratings:
        return jsonify({'average_rating': None}), 200  # Return None if there are no ratings

    average_rating = sum(book_ratings) / len(book_ratings)
    return jsonify({'average_rating': average_rating}), 200
