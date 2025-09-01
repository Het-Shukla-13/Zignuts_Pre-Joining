class library:
    def __init__(self):
        self.books=[]
    
    def addBook(self, title, author, year):
        book={"title": title, "author": author, "year": year}
        self.books.append(book)
        print(f'Book "{title}" added to the library.')

    def removeBook(self, title):
        for book in self.books:
            if book["title"]==title:
                self.books.remove(book)
                print(f'Book "{title}" removed from the library.')
                return
        print(f'Book "{title}" not found in the library.')

    def searchBook(self, title):
        for book in self.books:
            if book["title"]==title:
                author=book["author"]
                year=book["year"]
                print(f'Book found: Title: {title}, Author: {author}, Year: {year}')
                return
        print(f'Book "{title}" not found in the library.')

    def displayBooks(self):
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            title=book["title"]
            author=book["author"]
            year=book["year"]
            print(f'Title: {title}, Author: {author}, Year: {year}')

def main():
    lib=library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display All Books")
        print("5. Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            title=input("Enter book title: ")
            author=input("Enter book author: ")
            year=input("Enter publication year: ")
            lib.addBook(title, author, year)
        elif choice==2:
            title=input("Enter book title to remove: ")
            lib.removeBook(title)
        elif choice==3:
            title=input("Enter book title to search: ")
            lib.searchBook(title)
        elif choice==4:
            lib.displayBooks()
        elif choice==5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()