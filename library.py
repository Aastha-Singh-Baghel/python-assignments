class Library:
    def __init__(self, book_name, author, available=True):
        self.book_name = book_name
        self.author = author
        self.available = available

    # Method to check out a book
    def checkout_book(self):
        if self.available:
            self.available = False
            print(self.book_name, "has been checked out.")
        else:
            print(self.book_name, "is not available.")

    # Method to return a book
    def return_book(self):
        self.available = True
        print(self.book_name, "has been returned.")

    # Method to display available books
    def display_status(self):
        if self.available:
            print(self.book_name, "by", self.author, "- Available")
        else:
            print(self.book_name, "by", self.author, "- Checked Out")

# Creating objects
book1 = Library("Python Basics", "John Smith")
book2 = Library("Data Structures", "David Miller")

# Display status
book1.display_status()
book2.display_status()

# Checkout a book
book1.checkout_book()

# Check status again
book1.display_status()

# Return the book
book1.return_book()

# Final status
book1.display_status()