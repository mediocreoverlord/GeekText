from flask import Flask, request, jsonify
import mysql

app = Flask

app.config['MYSQL_HOST'] = 'your_mysql_host'
app.config['MYSQL_USER'] = 'your_mysql_user'
app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
app.config['MYSQL_DB'] = 'your_mysql_db'

mysql = Flask(__name__)

@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.json
    username = data['username']
    password = data['password']
    name = data.get('name')
    email = data.get('email')
    home_address = data.get('home_address')

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO users (username, password, name, email, home_address) VALUES (%s, %s, %s, %s, %s)",
                   (username, password, name, email, home_address))
    mysql.connection.commit()
    cursor.close()

    return "User created successfully", 201


@app.route('/get_user/<string:username>', methods=['GET'])
def get_user(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT username, name, email, home_address FROM users WHERE username = %s", (username,))
    user_data = cursor.fetchone()
    cursor.close()

    if user_data:
        user = {
            "username": user_data[0],
            "name": user_data[1],
            "email": user_data[2],
            "home_address": user_data[3]
        }
        return jsonify(user)
    else:
        return "User not found", 404














