class ShoppingCartRepository:
    #     handles interactions with the shopping cart in the MySQL database
    def __init__(self, db_connection):
        # initializes the ShoppingCartRepository with a database connection.
        self.db_connection = db_connection

    def get_subtotal(self, user_id):
        # calculates and retrieves the subtotal of the user's shopping cart
        query = "SELECT SUM(books.price) FROM shoppingcart " \
                "INNER JOIN books ON shoppingcart.isbn = books.isbn " \
                "WHERE shoppingcart.user_id = %s"
        result = self.db_connection.execute_query(query, (user_id,))
        subtotal = result[0][0] if result else 0
        return subtotal

    def add_item_to_cart(self, isbn, user_id):
        # add book to user's shopping cart
        insert_item_query = "INSERT INTO shoppingcart (user_id, isbn) VALUES (%s, %s)"
        self.db_connection.execute_query(insert_item_query, (user_id, isbn))

        # Commit the changes to the database
        self.db_connection.connection.commit()
    def get_cart_items(self, user_id):
        # retrieves items in the user's shopping cart with book details
        query = "SELECT books.*, author.firstname, author.lastname AS author_name FROM shoppingcart " \
            "INNER JOIN books ON shoppingcart.isbn = books.isbn " \
            "INNER JOIN author ON books.author_id = author.author_id " \
            "WHERE shoppingcart.user_id = %s"
        result = self.db_connection.execute_query(query, (user_id,))
        return result

    def delete_item_from_cart(self, isbn, user_id):
        # removes book from user's shopping cart
        query = "DELETE FROM shoppingcart WHERE user_id = %s AND isbn = %s"
        print(f"Deleting item from cart. ISBN: {isbn}, User ID: {user_id}")
        self.db_connection.execute_query(query, (user_id, isbn,))
        self.db_connection.connection.commit()
