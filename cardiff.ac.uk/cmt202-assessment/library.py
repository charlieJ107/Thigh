import Pyro5.api
from Pyro5.server import Daemon, serve


@Pyro5.api.expose
class library(object):
    def __init__(self) -> None:
        # Create a list to store the users
        self.users = list()
        # Create a list to store the authors
        self.authors = list()
        # Create a dictionary to store the books
        self.books = dict()

    """
    Task 1:
    Add a user to the system. Implement this using a method with the following header:
    def add_user(self, user_name, user_number)
    An example of calling this method is:
    library_object.add_user(“Allen Hatcher”, 123456)
    You can assume that each user added to the system has a unique user name
    """

    def add_user(self, user_name, user_number) -> str:
        # Create a dictionary to store the user
        user = dict()
        # Add the user name and user number to the dictionary
        user["user_name"] = user_name
        user["user_number"] = user_number
        # Add the user to the users list
        self.users.append(user)
        return "Following user added successfully: \n" + self.toTableStr([user])

    """
    Task 2:
    Return all associated pieces of information relating to the set of users currently
    stored in the system (i.e. a set of user names and contact numbers). Implement this
    using a method with the following header:
    def return_users(self)
    An example of calling this method is:
    library_object.return_users()
    The information returned by this method should have the property that it can be
    easily interpreted when displayed using the Python print function. That is, the output
    from the following print function should be easily interpreted and understood by a
    human reader:
    print(rental_object.return_users())
    """

    def return_users(self) -> str:
        # Return the users list
        if len(self.users) == 0:
            return "No users found"
        return self.toTableStr(self.users)

    """
    Task 3:
    Add an author to the system. Implement this using a method with the following 
    header: 

    def add_author(self, author_name, author_genre):
    
    An example of calling this method is: 

    library_object.add_author(“James Joyce”, “fiction”)

    You can assume that all author names are unique.
    """

    def add_author(self, author, author_genre) -> str:
        # Create a dictionary to store the author
        author_dict = dict()
        # Add the author and author genre to the dictionary
        author_dict["author"] = author
        author_dict["author_genre"] = author_genre
        # Add the author to the authors list
        self.authors.append(author_dict)
        return "Following author added successfully: \n" + self.toTableStr([author_dict])

    """
    Task 4:
    Return all associated pieces of information relating to the set of authors currently
    stored in the system (i.e. a set of author names and genres). Implement this using a
    method with the following header:
    def return_authors(self)
    An example of calling this method is:
    library_object.return_authors()
    The information returned by this method should have the property that it can be
    easily interpreted when displayed using the Python print function. That is, the output
    """

    def return_authors(self) -> str:
        if len(self.authors) == 0:
            return "No authors found"
        return self.toTableStr(self.authors)

    """
    Task 5:
    Add a copy of a book to the system. Implement this using a method with the
    following header:
    def add_book_copy(self, author_name, book_title)
    An example of calling this method is:
    library_object.add_book_copy(“James Joyce”, “Ulysses”)
    When a book copy is first added to the system it is initially not loaned to any user.
    Multiple copies of a single book (books with the same author and title) may be added
    to the system.
    You can assume that all book titles are unique.
    You can assume that the author in question has previously been added using the
    add_author method.
    """

    def add_book_copy(self, author_name, book_title) -> str:
        # Create a dictionary to store the book
        book = dict()
        # Add the book title and author name to the dictionary
        book["book_title"] = book_title
        book["author_name"] = author_name
        book["is_loan"] = False
        # Add the book to the books dictionary
        if author_name not in self.books.keys():
            # No books by this author have been added yet
            # Create a new list to store the books
            self.books[author_name] = list()
        # Add the book to the list
        self.books[author_name].append(book)
        return "Following book added successfully: \n" + self.toTableStr([book])

    """
    Task 6:
    Return all associated pieces of information relating to the set of book copies
    currently not on loan (i.e. a set of book authors plus titles). Implement this using a
    method with the following header:

    def return_books_not_loan(self)

    An example of calling this method is:

    library_object.return_books_not_loan()

    Note, multiple copies of a single book can exist in the system.
    The information returned by this method should have the property that it can be
    easily interpreted when displayed using the Python print function
    """

    def return_books_not_loan(self) -> str:
        # Create a new dictionary to store the books that are not loaned
        books_not_loan = list()
        # Loop through the books dictionary
        for author_name, books in self.books.items():
            # Create a new list to store the books that are not loaned

            # Loop through the books
            for book in books:
                # If the book is not loaned, add it to the books_not_loan dictionary
                if not book["is_loan"]:
                    # Create a new dictionary to store the book
                    book_not_loan = dict()
                    # Add the author name and book title to the dictionary
                    book_not_loan["author_name"] = author_name
                    book_not_loan["book_title"] = book["book_title"]
                    # Add the book to the books_not_loan list
                    books_not_loan.append(book_not_loan)
        # Return the books_not_loan dictionary
        if len(books_not_loan) == 0:
            return "No books are currently not loaned"
        return self.toTableStr(books_not_loan)

    """
    Task 7:
    Loan a copy of a specified book to a specified user on a specified date. Implement
    this using a method with the following header:
    def loan_book(self, user_name, book_title, year, month, day)
    An example of calling this method is:
    library_object.loan_book(“Conor Reilly”, “Ulysses”, 2019, 1, 3)
    Each copy of a book can only be loaned to a single user at a time. For example,
    consider the case where there are two copies of a given book and both are currently
    on loan. In this case the book in question cannot be loaned until one of the copies is
    returned or an additional copy is added to the system.
    You can assume that the user in question has previously been added using the
    add_user method.
    The method loan_book should return a value of 1 if the book in question was
    successfully loaned. Otherwise, the method should return a value of 0.
    """

    def loan_book(self, user_name, book_title, year, month, day) -> int:
        # Loop through the books
        for books in self.books.values():
            # Loop through the books
            for book in books:
                # If the book is not loaned, loan it to the user
                if book["book_title"] == book_title and not book["is_loan"]:
                    # Add the user name, year, month and day to the book
                    book["user_name"] = user_name
                    book["year"] = year
                    book["month"] = month
                    book["day"] = day
                    book["is_loan"] = True
                    return 1
        return 0

    """
    Task 8:
    Return all associated pieces of information relating to the set of book copies
    currently on loan (i.e. a set of book authors plus titles). Implement this using a
    method with the following header:
    def return_books_loan(self)
    An example of calling this method is:
    library_object.return_books_loan()
    The information returned by this method should have the property that it can be
    easily interpreted when displayed using the Python print function.
    """

    def return_books_loan(self) -> str:
        # Create a new list to store the books that are loaned
        books_loan = list()
        # Loop through the books
        for books in self.books.values():
            for book in books:
                # If the book is loaned, add it to the books_loan list
                if book["is_loan"]:
                    books_loan.append(book)
        # Return the books_loan list
        if len(books_loan) == 0:
            return "No books are loaned"
        return self.toTableStr(books_loan)
    """
    Task 9:
    Return to the library a loaned copy of a specified book by a specified user on a
    specified date; that is, set the status of the book in question from loaned to not
    loaned. Implement this using a method with the following header:
    def end_book_loan(self, user_name, book_title, year, month, day)
    An example of calling this method is:
    library_object.end_book_loan(“Conor Reilly”, “Ulysses”, 2019, 2, 4)
    You can assume that the user has previously loaned the copy in question and this
    method call corresponds to them returning that copy.
    You can assume that a user will only loan one copy of a given book at any one time.
    Therefore, there will never exist any ambiguity regarding which book copy is being
    returned.
    You can assume that the date in question is valid.
    """

    def end_book_loan(self, user_name, book_title, year, month, day) -> str:
        # Loop through the books
        for author_name, books in self.books.items():
            for book in books:
                # If the book is loaned to the user, return it
                # Since the user can only loan one copy of a book, dates are not checked
                if book["book_title"] == book_title and book["is_loan"] and book["user_name"] == user_name:
                    book["is_loan"] = False
                    return "Following book returned: \n" + self.toTableStr([book])
        return "Book not found"

    """
    Task 10:
    Delete from the system all copies of a specified book which are currently not on loan.
    Copies which are currently on loan should not be deleted. Implement this using a
    method with the following header:
    def delete_book(self, book_title)
    An example of calling this method is:
    library_object.delete_book("Ulysses")
    """

    def delete_book(self, book_title) -> str:
        # Loop through the books
        for books in self.books.values():
            for book in books:
                # If the book is not loaned, delete it
                if book["book_title"] == book_title and not book["is_loan"]:
                    books.remove(book)
                    return "Following book deleted: \n" + self.toTableStr([book])
        return "Book not found"

    """
    Task 11:
    Delete from the system a specified user. A user should only be deleted if they have
    never loaned a book. Implement this using a method with the following header:
    def delete_user(self, user_name)
    An example of calling this method is:
    library_object.delete_user(“Conor Reilly”)
    You can assume that the user in question has previously been added using the
    add_user method.
    The method delete_user should return a value of 1 if the user in question was
    deleted. Otherwise, the method should return a value of 0.
    """

    def delete_user(self, user_name) -> int:
        # Loop through the users
        for user in self.users:
            # If the user is not loaned, delete it
            if user["user_name"] == user_name:
                self.users.remove(user)
                return 1
        return 0

    """
    Task 12:
    Return all book titles a user previously has loaned where the corresponding loan and
    return dates both lie between a specified start and end date inclusive.
    Implement this using a method with the following header:
    def user_loans_date(self, user_name, start_year, start_month, start_day, end_year,
    end_month, end_day)
    An example of calling this method is:
    library_object.user_loans_date("Conor Reilly", 2010, 1, 1, 2029, 2, 1)
    Note, the book titles returned may contain duplicates if the user loaned the book in
    question more than once.
    You can assume that the dates in question are valid.
    You can assume that the user in question has previously been added using the
    add_user method.
    The information returned by this method should have the property that it can be
    easily interpreted when displayed using the Python print function.
    """

    def user_loans_date(self, user_name, start_year, start_month, start_day, end_year, end_month, end_day) -> str:
        # Create a new list to store the books that are loaned
        books_loan = list()
        # Loop through the books
        for books in self.books.values():
            for book in books:
                # If the book is loaned to the user, add it to the books_loan list
                if book["user_name"] == user_name and book["is_loan"]:
                    # Check if the book is loaned between the start and end date
                    if book["year"] >= start_year and book["year"] <= end_year:
                        if book["month"] >= start_month and book["month"] <= end_month:
                            if book["day"] >= start_day and book["day"] <= end_day:
                                books_loan.append(book)
        # convert the books_loan list to a table as a string
        if len(books_loan) > 0:
            return self.toTableStr(books_loan)
        else:
            return "No books loaned"

    def toTableStr(self, myDict, colList=None, sep='\n'):
        """ Pretty print a list of dictionaries (myDict) as a dynamically sized table.
        If column names (colList) aren't specified, they will show in random order.
        sep: row separator. Ex: sep='\n' on Linux. Default: dummy to not split line.
        Author: Thierry Husson
        """
        res = ""
        if not colList:
            colList = list(myDict[0].keys() if myDict else [])
        myList = [colList]  # 1st row = header
        for item in myDict:
            myList.append([str(item[col] or '') for col in colList])
        colSize = [max(map(len, (sep.join(col)).split(sep)))
                   for col in zip(*myList)]
        formatStr = ' | '.join(["{{:<{}}}".format(i) for i in colSize])
        line = formatStr.replace(
            ' | ', '-+-').format(*['-' * i for i in colSize])
        item = myList.pop(0)
        lineDone = False
        while myList or any(item):
            if all(not i for i in item):
                item = myList.pop(0)
                if line and (sep != '\uFFFA' or not lineDone):
                    res += line + "\n"
                    lineDone = True
            row = [i.split(sep, 1) for i in item]
            res += formatStr.format(*[i[0] for i in row]) + '\n'
            item = [i[1] if len(i) > 1 else '' for i in row]
        return res


daemon = Daemon()
serve({library: "example.library"}, daemon=daemon, use_ns=True)
