import sys
import Pyro5.errors
from Pyro5.api import Proxy

# Check that the Python file library.py exists.
import os.path
if(os.path.isfile("library.py")==False):
	print("Error you need to call the Python file library.py!")

# Check that the class is called library. That is, the file library.py contains the expression "library(object):"
file_text = open('library.py', 'r', encoding="utf-8").read()
if("library(object):" not in file_text):
	print("Error you need to call the Python class library!")

sys.excepthook = Pyro5.errors.excepthook
library_object = Proxy("PYRONAME:example.library")

print("Add a user")
print(library_object.add_user("Conor Reilly", 123456))

print("Test return_users")
print(library_object.return_users())

print("Test add_author")
print(library_object.add_author("James Joyce", "fiction"))

print("Test return_authors")
print(library_object.return_authors())

print("Test add_book")
print(library_object.add_book_copy("James Joyce", "Ulysses"))

print("Test return_books_not_loan")
print(library_object.return_books_not_loan())

print("Test loan_book")
print(library_object.loan_book("Conor Reilly", "Ulysses", 2019, 1, 3))

print("Test return_books_loan")
print(library_object.return_books_loan())

print("Test end_book_loan")
print(library_object.end_book_loan("Conor Reilly", "Ulysses", 2019, 2, 4))

print("Test delete_book")
print(library_object.delete_book("Ulysses"))

print("Test delete_user")
print(library_object.delete_user("Conor Reilly"))

print("Test user_loans_date")
print(library_object.user_loans_date("Conor Reilly", 2010, 1, 1, 2029, 2, 1))
