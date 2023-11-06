class WishListRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection


    # gets a whislist by its unique ID
    def get_wishlist_by_id(self, wishlist_id):
        query = "SELECT * FROM Wishlist WHERE idwishlist = %s"
        results = self.db_connection.execute_query(query, (wishlist_id,))

        if not results:
            return {"message": "Wishlist not found"}

        return results

    # gets all wishlists form a user by their userID
    def get_wishlists_by_user(self, user_id):
        query = "SELECT idwishlist, name FROM Wishlist WHERE iduser = %s"
        results = self.db_connection.execute_query(query, (user_id,))

        if not results:
            return {"message": f"No wishlists found for user {user_id}."}

        wishlists = [{"idwishlist": row[0], "name": row[1]} for row in results]
        return wishlists

    # Creates a new wishlist for a user with the given name.
    def create_wishlist(self, user_id, wishlist_name):
        # Check the count of existing wishlists for the user
        count_query = "SELECT COUNT(*) FROM Wishlist WHERE iduser = %s"
        try:
            count_result = self.db_connection.execute_query(count_query, (user_id,))
            wishlist_count = count_result[0][0]

            if wishlist_count >= 3:
                return {"error": "User already has 3 wishlists."}

            # Create Whishlist if the user has less than 3
            insert_query = "INSERT INTO Wishlist (iduser, name) VALUES (%s, %s)"
            self.db_connection.execute_query(insert_query, (user_id, wishlist_name))
            self.db_connection.connection.commit()
            return {"message": "Wishlist successfully created!"}

        except Exception as e:
            if self.db_connection.connection.is_connected():
                self.db_connection.connection.rollback()
            return {"error": f"Error creating wishlist: {e} "}

    # Adds a book to a wishlist by ISBN.

    def add_book_to_wishlist(self, wishlist_id, isbn):
        query = "INSERT INTO WishlistBooks (wishlist_id, isbn) VALUES (%s, %s)"
        try:
            self.db_connection.execute_query(query, (wishlist_id, isbn))
            self.db_connection.connection.commit()
            return {"message": "Book added to wishlist successfully!"}
        except Exception as e:
            if self.db_connection.connection.is_connected():
                self.db_connection.connection.rollback()
            return {"error": f"Error adding book to wishlist: {e}"}

# Removes a book from a wishlist by ISBN.

    def remove_book_from_wishlist(self, wishlist_id, isbn):
        query = "DELETE FROM WishlistBooks WHERE wishlist_id = %s AND isbn = %s"
        try:
            self.db_connection.execute_query(query, (wishlist_id, isbn))
            self.db_connection.connection.commit()
            return {"message": "Book removed from wishlist successfully!"}
        except Exception as e:
            if self.db_connection.connection.is_connected():
                self.db_connection.connection.rollback()
            return {"error": f"Error removing book from wishlist: {e}"}

# gets all books from a wishlist by the wishlist ID.

    def get_books_in_wishlist(self, wishlist_id):
        query = """
        SELECT b.isbn, b.title, b.genre, a.firstname, a.lastname
        FROM WishlistBooks wb
        JOIN Books b ON wb.isbn = b.isbn
        JOIN Author a ON b.idauthor = a.idauthor
        WHERE wb.wishlist_id = %s
        """
        results = self.db_connection.execute_query(query, (wishlist_id,))

        if not results:
            return {"message": "No books found in wishlist"}

        books = [{
            "isbn": row[0],
            "title": row[1],
            "genre": row[2],
            "author": f"{row[3]} {row[4]}"
        } for row in results]
        return books