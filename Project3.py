#  ________  ________  ________        ___  _______   ________ _________        ________
# |\   __  \|\   __  \|\   __  \      |\  \|\  ___ \ |\   ____\\___   ___\     |\_____  \
# \ \  \|\  \ \  \|\  \ \  \|\  \     \ \  \ \   __/|\ \  \___\|___ \  \_|     \|____|\ /_
#  \ \   ____\ \   _  _\ \  \\\  \  __ \ \  \ \  \_|/_\ \  \       \ \  \            \|\  \
#   \ \  \___|\ \  \\  \\ \  \\\  \|\  \\_\  \ \  \_|\ \ \  \____   \ \  \          __\_\  \
#    \ \__\    \ \__\\ _\\ \_______\ \________\ \_______\ \_______\  \ \__\        |\_______\
#     \|__|     \|__|\|__|\|_______|\|________|\|_______|\|_______|   \|__|        \|_______|

# Author: Daniel Flesch
# CIST2110-001-Project-3 Library Management System (LMS)
# Project 3 will implement a library management system (LMS) that will allow users to manage books, users, and a library to manage collection of books and users.
# The LMS will be menu driven and will allow users to add, delete, and update books and users.
# Users will also be able to borrow and return books.
# The LMS will also allow users to search for books and users.

# ENABLE WORD WRAP TO MAKE THINGS EASIER TO READ:
# VIEW (at the top) -> WORD WRAP

# Import statements:
import csv

# Project outline and requirements:

# OUTLINE - The LMS will consist of the following classes and methods:

# 1. Create a Book class that has the following attributes (create a __init__ method)):
#    a. ISBN (int)
#    b. Title (string)
#    c. Author (string)
#    d. borrowed (boolean) - this should not be passed in as a parameter, it should be set to False by default
# USE SELF IN THE __INIT__ METHOD TO CREATE THESE ATTRIBUTES
class Book:
    def __init__(self,title: str, author: str, isbn: int):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.borrowed = False
# Methods:
#    a. __str__ (returns a string representation of the book using the following format: ISBN: <ISBN>, Title: <Title>, Author: <Author>, Borrowed: <Borrowed>)
    def __str__(self) -> str:
        return f" ISBN: {self.isbn}, Title: {self.title}, Author: {self.author}, Borrowed: {self.borrowed}"
    
#    b. checkout - sets borrowed to True and returns a message that the book has been checked out
    def check_out(self) -> str:
        """
        Checks out a book.

        Parameters: None

        Returns: str: A message that the book has been checked out.
        """
        self.borrowed = True

        return "\n The book has been checked out, thank you."
       
            
#    c. checkin - sets borrowed to False and returns a message that the book has been checked in
    def check_in(self) -> str:
        """
        Checks out a book.

        Parameters: None

        Returns: str: A message that the book has been checked in.
        """
        self.borrowed = False
        
        return "\n The book has been checked in, thank you."
    
#    d. isBorrowed - returns True if the book is borrowed and False if the book is not borrowed
    def isBorrowed(self)-> bool:
        if self.borrowed:
            return True
        else:
            return False
                

# 2. Create a User class that has the following attributes (create a __init__ method)):
#    a. Name (string)
#    c. ID (int)
#   d. borrowedBooks (list of books)
# USE SELF IN THE __INIT__ METHOD TO CREATE THESE ATTRIBUTES
class User:
    def __init__(self, name: str, id: int):
        self.name = name
        self.member_id = id
        self.borrowed_books = []

    def __str__(self) -> str:
        borrowed_books_str = ", ".join(str(book.title) for book in self.borrowed_books)
        return f"\n Name: {self.name}, ID: {self.member_id}, Borrowed Books: {borrowed_books_str}"
# Methods:
#    a. __str__ (returns a string representation of the user using the following format: Name: <Name>, ID: <ID>, Borrowed Books: <Borrowed Books>)
#    b. borrow_book - adds the book to the borrowedBooks list, updates the isBorrowed attribute of the book to True, and returns a message that the book has been checked out (should take a book as a parameter)
#    c. return_book - removes the book from the borrowedBooks list, updates the isBorrowed attribute of the book to False, and returns a message that the book has been checked in (should take a book as a parameter)
    def borrow_book(self, book: Book) -> str:
        """
        Updates isBorrowed to true, adds the book to the user's borrowed list and checks out the book.

        Parameters: Book

        Returns: str: A message that the book has been checked out.
        """
        if book.isBorrowed() is False:
            book.isBorrowed() == True
            book.check_out()
            self.borrowed_books.append(book)
            return f"\n {book.title} has been borrowed by {self.name}"
        else:
            return f"\n {book.title} is already borrowed."
    
    def return_book(self, book: Book)-> str:
        """
        Updates isBorrowed to false, removes the book from the user's borrowed list and checks in the book.
        Parameters: Book
        Returns: str: A message that the book has been returned to the library.
        """
        if book.isBorrowed():
            book.check_in()
            self.borrowed_books.remove(book)
            return f"\n {book.title} has been returned by {self.name}"
        else:
            return f"\n {book.title} is not borrowed by {self.name}"
        
# 3. Create a Library class that has the following attributes (create a __init__ method)):
#    a. books (list of books)
#    b. users (list of users)
# USE SELF IN THE __INIT__ METHOD TO CREATE THESE ATTRIBUTES
class Library:
    def __init__(self):
        self.books = []
        self.users = []

# Methods:
#    a. __str__ (returns a string representation of the library using the following format: Books: <Books>, Users: <Users>)
    def __str__(self) -> str:
        return f"\n Books: {self.books}, Users: {self.users}"
    
#    b. add_book - adds a book to the books list (should take a book as a parameter)
    def add_book(self, book: Book) -> str:
        """
        Adds a book to the books list.

        Parameters:
        book (Book): The book to be added.

        Returns:
        list: The updated list of books. 
        """
        self.books.append(book)
        return "\n Book has been added to the library."


#    c. add_user - adds a user to the users list (should take a user as a parameter)
    def add_user(self, user: User)-> str:
        """
        Adds a user to the users list.

        Parameters:
        user (User): The user to be added.

        Returns:
        list: The updated list of users.
        """
        self.users.append(user)
        return "\n User has been added to the library."
        
#    d. find_book - returns the book with the given ISBN (should take an ISBN as a parameter)
    def find_book(self, isbn: int):
        """
        Finds and returns the book with the given ISBN.

        Parameters:
        isbn (int): The ISBN of the book to be found.

        Returns:
        Book: The book with the given ISBN if found, None otherwise.
         """
        try:
            for book in self.books:
                if book.isbn == isbn:
                    return book
            return None
        except ValueError:
            return "Invalid input."
            

#    e. find_user - returns the user with the given ID (should take an ID as a parameter)
    def find_user(self, id: int):
        """
        Finds and returns the user with the given ID.

        Parameters:
        id (int): The ID of the user to be found.

        Returns:
        User: The user with the given ID if found, None otherwise.
        """
        for user in self.users:
            if user.member_id == id:
                return user
        
        return "user not found"
        
#    f. export_books_to_csv - exports the books list to a csv file (should take a filename as a parameter)
#       The csv file should have the following format: ISBN,Title,Author,Borrowed
#       The csv.DictWriter class is very useful for this: https://docs.python.org/3/library/csv.html#csv.DictWriter
    def export_books_to_csv(self, filename)-> None:
        """
        Exports the books list to a csv file.

        Parameters:
        filename (str): The name of the file to be exported to.

        Returns:
        None
        """

        fieldnames = ["ISBN", "Title", "Author", "Borrowed"]
        try:
            
            with open(filename, "w", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

                for book in self.books:
                    book_dict = {
                        "ISBN": book.isbn,
                        "Title": book.title,
                        "Author": book.author,
                        "Borrowed": book.isBorrowed()
                    }
                    writer.writerow(book_dict)

            print("\n"f"Books exported successfully to {filename}")

        except FileNotFoundError:
            print("File does not exist.")


#    g. export_users_to_csv - exports the users list to a csv file (should take a filename as a parameter)
#       This will be similar to the export_books_to_csv method but there is a slight difference with the borrowedBooks attribute if you get stuck this code might help:
#       borrowed_books_titles = [book.title for book in user.borrowed_books]
#       Use that and pythons .join method to create a string of the borrowed books titles
    def export_users_to_csv(self, filename)-> None:
        """
        Exports the users list to a csv file.

        Parameters:
        filename (str): The name of the file to be exported to.

        Returns:
        None
        """
        try:
            with open(filename, "w", newline='') as file:
                fieldnames = ["Name", "ID", "Borrowed Books"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

                for user in self.users:
                    borrowed_books_titles = [book.title for book in user.borrowed_books]
                    user_dict = {
                        "Name": user.name,
                        "ID": user.member_id,
                        "Borrowed Books": ", ".join(borrowed_books_titles)
                    }
                    writer.writerow(user_dict)

            print("\n",f"Users exported successfully to {filename}")

        except FileNotFoundError:
            print("File does not exist.")


# 4. Create a menu that will allow users to:
def main_menu()-> str:
    """
    Displays the library management system choices.
    Parameters: None
    Returns: str: The user's choice.
    """
    print("\n""Please select an option from the menu below:""\n")
    print("a. Add books")
    print("b. Add users")
    print("c. Delete books")
    print("d. Delete users")
    print("g. Borrow books")
    print("h. Return books")
    print("i. Search books")
    print("j. Check if book is available")
    print("k. Search users")
    print("l. Export books to csv")
    print("m. Export users to csv")
    print("z. Exit")
    choice = input("Enter your selection: ").lower()

    if choice == int:
        print("Please enter a valid selection.")
        return main_menu()
    return choice
#

# RQUIREMENTS:
# 1. You should be doing error checking on all user input (make sure the user enters a valid ISBN, ID, etc.) and handle any errors appropriately (i.e. if the user enters an invalid ISBN, ask them to enter a valid ISBN)
# 2. You should be using try except blocks to handle any errors
# 3. You should be using the classes and methods outlined above with the exact names and parameters
# 4. You should be using the menu to call the appropriate methods
# 5. There is a Project3Tests.py file that will help you test your code. You should be able to run that file and pass all the tests.
#    Remember to run pytest use the following command in the terminal: pytest Project3Tests.py
# 6. The Project3Tests.py file is missing 2 tests. test_user_return and test_library_find_user. You will need to implement those tests and ensure they pass.
# 7. In your main method you should create a library object first to use for the rest of the program. You should not be creating a new library object every time you call a method. (Similar to the Store object in Lab 11)
# 8. In your main method you should be using a while loop to keep the program running until the user chooses to exit.

# IMPORTANT: You will only have 1 submission for this project so make sure you test your code thoroughly before submitting.

# You will be graded on the following:
# 1. Did you follow the project outline and requirements?
# 2. Does your code run without errors?
# 3. Did you use try   except blocks to handle errors?
# 4. Did you use the classes and methods outlined above with the exact names and parameters?
# 5. Did you use the menu to call the appropriate methods?
# 6. Did you include docstrings for all classes and methods?
# 7. Did you include type hints for all methods?
# 8. Did your pytests for the test_user_return and test_library_find_user work?


def main():
    """
    Runs the library management system.
    Parameters: None
    Returns: None
    """
    print("\n","Welcome to the Library Management System (LMS)\n")
    library = Library()
    while True:
        try:
            choice = main_menu()
            if choice == "a":
                title = input("Please enter the title of the book: ")
                author = input("Please enter the author of the book: ")
                isbn = int(input("Please enter the ISBN of the book: "))
                book = Book(title, author, isbn)
                library.add_book(book)
                if book in library.books:
                    print(f"\n {book.title} has been added to the library.")
                    for book in library.books: print("\n",book)
                else:
                    print("\n Book was not added to the library.")
                

            elif choice == "b":
                name = input("Please enter the name of the user: ")
                id = int(input("Please enter the ID of the user: "))
                user = User(name, id)
                library.add_user(user)
                if user in library.users:
                    print(f"\n {user.name} has been added to the library.")
                else:
                    print("\n User was not added to the library.")
                
            
            elif choice == "c":
                isbn = int(input("Please enter the ISBN of the book you would like to delete: "))
                book = library.find_book(isbn)
                if book is not None:
                    for user in library.users:
                        if book in user.borrowed_books:
                            user.borrowed_books.remove(book)
                    library.books.remove(book)
                    print(f"\n {book} has been deleted from the library.")
                else:
                    print("\n","Book was not found.")
            
            elif choice == "d":
                id = int(input("Please enter the ID of the user you would like to delete: "))
                user = library.find_user(id)
                if user is not None:
                    for book in user.borrowed_books:
                        user.return_book(book)
                    library.users.remove(user)
                    print(f"\n {user.name} has been deleted from the library system.")
                else:
                    print("\n","User was not found.")

            elif choice == "g":
                isbn = int(input("Please enter the ISBN of the book you would like to borrow: "))
                book = library.find_book(isbn)
                if book is not None:
                    id = int(input("Please enter the ID of the user borrowing the book: "))
                    user = library.find_user(id)
                    if user is not None:
                        user.borrow_book(book)
                        print(f"\n {book.title} has been borrowed by {user.name}")
                    else:
                        print("\n","User was not found.")
                else:
                    print("\n","Book was not found.")

            elif choice == "h":
                isbn = int(input("Please enter the ISBN of the book you would like to return: "))
                book = library.find_book(isbn)
                if book is not None:
                    id = int(input("Please enter the ID of the user returning the book: "))
                    user = library.find_user(id)
                    if user is not None:
                        user.return_book(book)
                        print(f"\n {book.title} has been returned by {user.name}")
                    else:
                        print("\n","User was not found.")
                else:
                    print("\n","Book was not found.")

            elif choice == "i":
                isbn = int(input("Please enter the ISBN of the book you would like to search for: "))
                book = library.find_book(isbn)
                if book is not None:
                    print(f"\n {book}")
                else:
                    print("\n","Book was not found.")
            
            elif choice == "j":  
                isbn = int(input("Please enter the ISBN of the book you would like to check if available: "))
                book = library.find_book(isbn)
                if book is not None:
                    if book.isBorrowed():
                        print(f"\n {book.title} is not available.")
                    else:
                        print(f"\n {book.title} is available.")
                else:
                    print("\n","Book was not found.")
            
            elif choice == "k":
                id = int(input("Please enter the ID of the user you would like to search for: "))
                user = library.find_user(id)
                if user is not None:
                    print(f"\n {user}")
                else:
                    print("\n","User was not found.")
            
            elif choice == "l":
                filename = input("Please enter the name of the file you would like to export the books to: ")
                library.export_books_to_csv(filename)
            
            elif choice == "m":
                filename = input("Please enter the name of the file you would like to export the users to: ")
                library.export_users_to_csv(filename)

            elif choice == "z":
                print("\n""Thank you for using the LMS. Goodbye.")
                break
            else:
                print("\n","Please enter a valid choice.")
        except ValueError:
            print("\n","Error. Please enter a valid input.")

    
if __name__ == "__main__":
    main()