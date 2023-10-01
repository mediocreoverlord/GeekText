from flask import Flask
from Main.geektext.Test.TestRoutes import test



from BookDetails.Routes import book_details

app = Flask(__name__)

app.register_blueprint(test)
app.register_blueprint(book_details)


# Placeholder code for default starter link
@app.route("/")
def home():
    return 'Hello World'


if __name__ == '__main__':
    app.run(debug=True)
