from flask import Flask

from BookDetails.Routes import book_details
from ShoppingCart.Routes import shoppingcart

app = Flask(__name__)


app.register_blueprint(book_details)
app.register_blueprint(shoppingcart)


# Placeholder code for default starter link
@app.route("/")
def home():
    return 'Hello World'


if __name__ == '__main__':
    app.run(debug=True)