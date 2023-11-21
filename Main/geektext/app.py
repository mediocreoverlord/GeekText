from flask import Flask


from BookBrowseSort.Routes import book_browse_sort

app = Flask(__name__)

app.register_blueprint(book_browse_sort)


# Placeholder code for default starter link
@app.route("/")
def home():
    return 'Hello World'


if __name__ == '__main__':
    app.run(debug=True)
