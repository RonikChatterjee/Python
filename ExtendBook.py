#   Question5:	Modify the Book class from Question 4 to include a destructor method (_del_) that prints a message when a book object is destroyed. Create two book objects, display their summaries, and then explicitly delete one of the objects. Observe the messages printed when objects are destroyed.

class Book:
    def __init__(self,title,author,published_year):
        self.title = title
        self.author = author
        self.published_year = published_year

    def get_summary(self):
        return f"{self.title} by {self.author} was published in {self.published_year}"

    def __doc__(self):
        return "This class represents a book with a title, author, and published year."
    
    def __del__(self):
        print(f"The book {self.title} by {self.author} was destroyed.")

#book1 = Book("The Great Gatsby","F. Scott Fitzgerald",1925)
book_name = input("Enter the name of the first book: ")
author_name = input("Enter the author name of the first book: ")
year = input("Enter the published year of the first book: ")

book1 = Book(book_name, author_name, year)

book_name = input("Enter the name of the second book: ")
author_name = input("Enter the author name of the second book: ")
year = input("Enter the published year of the second book: ")

book2 = Book(book_name, author_name, year)

print(book1.get_summary())
print(book1.__doc__())
print(book2.get_summary())
print(book2.__doc__())

del book1