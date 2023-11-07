class ShoppingCartRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_subtotal(self, user_id):
        query = "SELECT SUM(books.price) FROM shoppingcart " \
                "INNER JOIN books ON shoppingcart.isbn = books.isbn " \
                "WHERE shoppingcart.user_id = %s"
        result = self.db_connection.execute_query(query, (user_id,))
        subtotal = result[0][0] if result else 0
        return subtotal

    def add_item_to_cart(self, isbn, user_id):
        # Insert the item into the shoppingcart table
        insert_item_query = "INSERT INTO shoppingcart (user_id, isbn) VALUES (%s, %s)"
        self.db_connection.execute_query(insert_item_query, (user_id, isbn))

        # Commit the changes to the database
        self.db_connection.connection.commit()
    def get_cart_items(self, user_id):
        query = "SELECT books.*, author.firstname, author.lastname AS author_name FROM shoppingcart " \
            "INNER JOIN books ON shoppingcart.isbn = books.isbn " \
            "INNER JOIN author ON books.author_id = author.author_id " \
            "WHERE shoppingcart.user_id = %s"
        result = self.db_connection.execute_query(query, (user_id,))
        return result

    def delete_item_from_cart(self, isbn, user_id):
        query = "DELETE FROM shoppingcart WHERE user_id = %s AND isbn = %s"
        self.db_connection.execute_query(query, (user_id, isbn,))
        self.db_connection.connection.commit()