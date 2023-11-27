class WishListRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    # gets a whislist by its unique ID
    def get_wishlist_by_id(self, idwishlist):
        query = "SELECT * FROM Wishlist WHERE idwishlist = %s"
        results = self.db_connection.execute_query(query, (idwishlist,))

        if not results:
            return {"message": "Wishlist not found"}

        return results

    # gets all wishlists form a user by their userID
    def get_wishlists_by_user(self, iduser):
        query = "SELECT idwishlist, name FROM Wishlist WHERE iduser = %s"
        results = self.db_connection.execute_query(query, (iduser,))

        if not results:
            return {"message": "No wishlists found for user."}

        wishlists = [{"idwishlist": row[0], "name": row[1]} for row in results]
        return wishlists

    # Creates a new wishlist for a user with the given name.
    def create_wishlist(self, iduser, wishlistName):
        # Check the count of existing wishlists for the user
        count_query = "SELECT COUNT(*) FROM Wishlist WHERE iduser = %s"
        try:
            count_result = self.db_connection.execute_query(count_query, (iduser,))
            wishlist_count = count_result[0][0]

            if wishlist_count >= 3:
                return {"error": "User already has 3 wishlists."}

            # Create Whishlist if the user has less than 3
            insert_query = "INSERT INTO Wishlist (iduser, name) VALUES (%s, %s)"
            self.db_connection.execute_query(insert_query, (iduser, wishlistName))
            self.db_connection.connection.commit()
            return {"message":"Wishlist successfully created!"}

        except Exception as e:
            if self.db_connection.connection.is_connected():
                self.db_connection.connection.rollback()
            return {"error": "Error creating wishlist: {e} "}

    # Adds a book to a wishlist by ISBN.

    def add_book_to_wishlist(self, idwishlist, isbn):
        query = "INSERT INTO WishlistBooks (idwishlist, isbn) VALUES (%s, %s)"
        try:
            self.db_connection.execute_query(query, (idwishlist, isbn))
            self.db_connection.connection.commit()
            return {"message":"Book added to wishlist successfully!"}
        except Exception as e:
            if self.db_connection.connection.is_connected():
                self.db_connection.connection.rollback()
            return {"error": "Error adding book to wishlist: {e}"}

# Removes a book from a wishlist by ISBN.

    def remove_book_from_wishlist(self, idwishlist, isbn, iduser):
        query = "DELETE FROM WishlistBooks WHERE idwishlist = %s AND isbn = %s"
        try:
            self.db_connection.execute_query(query, (idwishlist, isbn))
            insert_item_query = "INSERT INTO shoppingcart (iduser, isbn) VALUES (%s, %s)"
            self.db_connection.execute_query(insert_item_query, (iduser, isbn))
            self.db_connection.connection.commit()
            return {"message": "Book removed to the Shopping cart successfully!"}

        except Exception as e:
            if self.db_connection.connection.is_connected():
                self.db_connection.connection.rollback()
        return {"error": "Error removing book to wishlist: {e}"}

# gets all books from a wishlist by the wishlist ID.

    def get_books_in_wishlist(self, idwishlist):
        query = """
        SELECT b.isbn, b.title, b.genre, a.firstname, a.lastname
        FROM WishlistBooks wb
        JOIN Books b ON wb.isbn = b.isbn
        JOIN Author a ON b.idauthor = a.idauthor
        WHERE wb.idwishlist = %s
        """
        results = self.db_connection.execute_query(query, (idwishlist,))

        if not results:
            return {"message": "No books found in wishlist"}

        books = [{
            "isbn": row[0],
            "title": row[1],
            "genre": row[2],
            "author": f"{row[3]} {row[4]}"
        } for row in results]
        return books