from flask import Flask


from BookBrowseSort.Routes import book_browse_sort
from BookDetails.Routes import book_details
from ShoppingCart.Routes import shoppingcart

app = Flask(__name__)

app.json.sort_keys = False #stops alphabetical sorting
app.register_blueprint(book_details)
app.register_blueprint(shoppingcart)
app.register_blueprint(book_browse_sort)


# Placeholder code for default starter link
@app.route("/")
def home():
    return 'Hello World'


if __name__ == '__main__':
    app.run(debug=True)