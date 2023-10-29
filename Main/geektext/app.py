from flask import Flask


from BookDetails.Routes import book_details

app = Flask(__name__)
app.json.sort_keys = False #stops alphabetical sorting
app.register_blueprint(book_details)


# Placeholder code for default starter link
@app.route("/")
def home():
    return 'Hello World'


if __name__ == '__main__':
    app.run(debug=True)
