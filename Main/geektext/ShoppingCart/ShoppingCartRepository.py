class ShoppingCartRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_subtotal(self, user_id):
        query = "SELECT SUM(price) FROM shoppingcart WHERE user_id = %s"
        result = self.db_connection.execute_query(query, (user_id,))
        subtotal = result[0][0] if result else 0
        return subtotal

    def add_item_to_cart(self, isbn, user_id):
        query = "INSERT INTO shoppingcart (user_id, isbn) VALUES (%s, %s)"
        self.db_connection.execute_query(query, (user_id, isbn,))

    def get_cart_items(self, user_id):
        query = "SELECT isbn FROM shoppingcart WHERE user_id = %s"
        result = self.db_connection.execute_query(query, (user_id,))
        cart_items = [item[0] for item in result]
        return cart_items

    def delete_item_from_cart(self, isbn, user_id):
        query = "DELETE FROM shoppingcart WHERE user_id = %s AND isbn = %s"
        self.db_connection.execute_query(query, (user_id, isbn,))