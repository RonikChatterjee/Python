#   Question4:  Create a Python class named Book to represent books. Include the following attributes: title, author, and published_year. Implement a method named get_summary that returns a string summarizing the book's information. Additionally, use the _doc_ attribute to provide documentation for the class. Create an object of the class and print the summary and documentation.

class Book:
    def __init__(self,title,author,published_year):
        self.title = title
        self.author = author
        self.published_year = published_year

    def get_summary(self):
        return f"{self.title} by {self.author} was published in {self.published_year}"

    def __doc__(self):
        return "This class represents a book with a title, author, and published year."

#book1 = Book("The Great Gatsby","F. Scott Fitzgerald",1925)
book_name = input("Enter the book name: ")
author_name = input("Enter the author name: ")
year = input("Enter the published year: ")

book1 = Book(book_name, author_name, year)
print(book1.get_summary())
print(book1.__doc__())