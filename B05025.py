class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append({'title': title, 'author': author})
        print(f'Book "{title}" by {author} added to the library.')

    def view_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("Books in the library:")
            for index, book in enumerate(self.books, start=1):
                print(f'{index}. "{book["title"]}" by {book["author"]}')

    def remove_book(self, title):
        for book in self.books:
            if book['title'].lower() == title.lower():
                self.books.remove(book)
                print(f'Book "{title}" removed from the library.')
                return
        print(f'Book "{title}" not found in the library.')

    def search_book(self, title):
        for book in self.books:
            if book['title'].lower() == title.lower():
                print(f'Found: "{book["title"]}" by {book["author"]}')
                return
        print(f'Book "{title}" not found in the library.')


def main():
    library = Library()
    
    while True:
        print("\nLibrary Menu:")
        print("1. Add a Book")
        print("2. View Books")
        print("3. Remove a Book")
        print("4. Search for a Book")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            library.add_book(title, author)

        elif choice == '2':
            library.view_books()

        elif choice == '3':
            title = input("Enter the title of the book to remove: ")
            library.remove_book(title)

        elif choice == '4':
            title = input("Enter the title of the book to search: ")
            library.search_book(title)

        elif choice == '5':
            print("Exiting the library system.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()