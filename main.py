from library import Library
from user_class import user
from database import table_setup
table_setup()
library = Library()
userr = user()
while True:

    print("\n📚 LIBRARY MANAGEMENT SYSTEM 📚")
    print("Enter the number according to your choice :")
    print("1 : add books")
    print("2 : Issue a book")
    print("3 : returning a book")
    print("4 : list of available Books")
    print("5 : adding new users ")
    print("6 : list of users")
    print("7 : Exit ") 

    choice = input("\nEnter a number :")

    if choice == '1':

        title = input("Title of Book :")
        author = input("Author of Book :")
        library.add_book(title,author)

    elif choice == "2":

        book_id = input("Enter Book id :")
        user_id = input("Enter a user id :")
        library.issue_book(book_id,user_id)

    elif choice =='3':

        book_id = input("Enter a book id :")
        user_id = input("Enter user id :")
        library.return_book(book_id,user_id)

    elif choice == '4':

        library.list_books()

    elif choice == '5':
        name = input ("\nEnter your name :")
        userr.add_user(name)

    elif choice == '6':
        userr.list_user()
    elif choice == "7":
        print("\nExiting the LMS ....")
        break
    else:
        print("\nInvalid Number entered ...\n Please Select Again..")











