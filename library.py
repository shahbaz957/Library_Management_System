from database import connect_db
from log_transaction import transaction
class Library:
    def add_book(self,title,author):
        conn = connect_db()
        c = conn.cursor()
        c.execute("INSERT INTO books (title,author) VALUES(?,?)",(title,author))
        conn.commit()
        conn.close()
        msg = (f'Book named {title} by {author} has been added successfully')
        transaction(msg)
        print(msg)
    def issue_book(self,book_id,user_id):
        conn = connect_db()
        c = conn.cursor()
        c.execute("SELECT status FROM books WHERE book_id=?",(book_id,))
        book = c.fetchone()
        if book and book[0]==1:
            c.execute("UPDATE books SET status=0 WHERE book_id = ?",(book_id,))
            c.execute("UPDATE user SET issued_books = COALESCE(issued_books,'') || ? || ','  WHERE user_id = ?" , (str(book_id),user_id))   #we give the book id in str because this id is going to store in " "
            conn.commit()
            conn.close()
            msg = (f'Book of ID {book_id} has been issued to user with ID {user_id}')
            transaction(msg)
            print(msg)
        else:
            print("No book of this ID is available")
    def return_book(self,book_id,user_id):
        conn = connect_db()
        c = conn.cursor()
        c.execute("SELECT status FROM books WHERE book_id=?",(book_id,))
        book = c.fetchone()
        if book and book[0]==0:   #this means book is issued
            c.execute("UPDATE books SET status=1 WHERE book_id = ?",(book_id,))
            c.execute("UPDATE user SET issued_books=REPLACE(issued_books, ? || ',','') WHERE user_id = ?",(str(book_id),user_id))
            conn.commit()
            conn.close()
            msg = (f"Book of id {book_id} is returned by the user of id {user_id}")
            transaction(msg)
            print(msg)
        else:
            print("Book is not issued !!!")
    def list_books(self):
        conn = connect_db()
        c = conn.cursor()
        c.execute("SELECT book_id,title,author FROM books WHERE status =1")
        books = c.fetchall()
        conn.close()
        if books:
            print("\nFollowing are the available catalog of books\n")
            for book in books:
                print(f"{book[0]}: {book[1]} by {book[2]}")
        else:
            print("No book is available")

