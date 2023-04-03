from datetime import timedelta, datetime


class Book:
    def __init__(self, title, author, condition):
        self.title = title
        self.author = author
        self.status = 'On Shelf'
        self.condition = condition
        self.due_date = None

    def check_out(self):
        if self.status == 'Checked Out':
            print(f'The book "{self.title}" is already checked out.')
        else:
            self.status = 'Checked Out'
            first_date = datetime.today() + timedelta(days=14)
            self.due_date = first_date.strftime('%Y-%m-%d')
            self.condition -= 1
            print(f'The book "{self.title}" has been checked out and is due on {self.due_date}.')

    def return_book(self):
        self.status = 'On Shelf'
        print(f'The book "{self.title}" has been returned.')

    def recycle(self):
        self.status = 'Recycled'


book1 = Book("The Handmaid's Tale", "Margaret Atwood", 10)
book2 = Book("The Hunger Games", "Suzanne Collins", 10)
book3 = Book("The Stranger", "Albert Camus", 10)
book4 = Book("The Alchemist", "Paulo Coelho", 10)
book5 = Book("Beloved", "Toni Morrison", 10)
book6 = Book("The Color Purple", "Alice Walker", 10)
book7 = Book("The Devil Wears Prada", "Lauren Weisberger", 10)
book8 = Book("The Hobbit", "J.R.R. Tolkien", 5)
book9 = Book("To Kill a Mockingbird", "Harper Lee", 10)
book10 = Book("The Diary of a Young Girl", "Anne Frank", 10)
book11 = Book("The Chronicles of Narnia", "C.S. Lewis", 10)
book12 = Book("The Da Vinci Code", "Dan Brown", 10)

books = [book1, book2, book3, book4, book5, book6, book7, book8, book9, book10, book11, book12]

returned_books = []
checked_out_books = []
recycle_bin = []


def display_books():
    for index, book in enumerate(books):
        print(f'{index + 1}, {book.title}, by {book.author} is {book.status}')


def search_by_author():
    found_author = False
    while not found_author:
        author = input('Enter the name of the author: ')
        found_books = [book for book in books if book.author == author]
        if found_books:
            for book in found_books:
                print(f'We found {book.title} by {book.author}!')
            found_author = True
        else:
            print(f'No books by {author} found.')


def search_by_title():
    found_title = False
    while not found_title:
        keyword = input('Enter a keyword from the title: ')
        found_books = [book for book in books if keyword.lower() in book.title.lower()]
        if found_books:
            for book in found_books:
                print(f'We found {book.title}!')
            found_title = True
        else:
            print(f'No books with "{keyword}" in the title found.')


def check_out_book():
    book_checked = False
    while not book_checked:
        title = input('Confirm the title of the book you would like to check out or enter exit: ')
        found_book = None
        for book in books:
            if book.title == title:
                found_book = book
                break
        if found_book:
            found_book.check_out()
            books.remove(found_book)
            checked_out_books.append(found_book)
            book_checked = True
        elif title.lower() == 'exit':
            book_checked = True
        else:
            print(f'The book "{title}" is not in our catalog.')


def return_book():
    title = input('Enter the title of the book you are returning: ')
    found_book = None
    for book in checked_out_books:
        if book.title == title:
            found_book = book
            break
    if found_book:
        found_book.return_book()
        print(f'Processing {found_book.title}.')
        returned_books.append(found_book)
        books.append(found_book)
        if found_book.condition < 5:
            found_book.recycle()
            returned_books.remove(found_book)
            checked_out_books.remove(found_book)
            books.remove(found_book)
            recycle_bin.append(found_book)
            print(f'{found_book.title} has been recycled due to bad condition.')
        else:
            found_book.due_date = None
            found_book.status = 'On Shelf'
    else:
        print(f'The book "{title}" is not in our catalog.')


def main_menu():
    while True:
        print('1. Display all books')
        print('2. Search for a book by title')
        print('3. Search for a book by author')
        print('4. Check out a book')
        print('5. Return a book')
        print('6. Exit')

        choice = input('Enter your choice: ')
        if choice == '1':
            display_books()
            print('Would you like to check out one of these? (y or n)')
            would_check_out = input('> ')
            if would_check_out == 'y':
                check_out_book()
                print('Would you like to go back to the main menu?')
                response = input('> ')
                if response == 'y':
                    continue
                else:
                    print('Goodbye!')
                    break
            else:
                continue
        elif choice == '2':
            search_by_title()
            print('Would you like to check out one of these? (y or n)')
            would_check_out = input('> ')
            if would_check_out == 'y':
                check_out_book()
                print('Would you like to go back to the main menu?')
                response = input('> ')
                if response == 'y':
                    continue
                else:
                    print('Goodbye!')
                    break
            else:
                continue
        elif choice == '3':
            search_by_author()
            print('Would you like to check out one of these? (y or n)')
            would_check_out = input('> ')
            if would_check_out == 'y':
                check_out_book()
                print('Would you like to go back to the main menu?')
                response = input('> ')
                if response == 'y':
                    continue
                else:
                    print('Goodbye!')
                    break
            else:
                continue
        elif choice == '4':
            check_out_book()
            print('Would you like to return to the main menu? (y or n)')
            return_to_menu = input('> ')
            if return_to_menu == 'y':
                continue
            else:
                print('Goodbye!')
                break
        elif choice == '5':
            return_book()
            print('Would you like to return to the main menu? (y or n)')
            return_to_menu = input('> ')
            if return_to_menu == 'y':
                continue
            else:
                print('Goodbye!')
                break
        elif choice == '6':
            print('Thank you for using the library system!')
            break
        else:
            print('Invalid choice. Please try again.')


print('Welcome to the library system!')
print('Please choose an option from the following menu:')
main_menu()
print('Books left in book list')
for index, book in enumerate(books):
    print(f'{index + 1}, {book.title}, by {book.author} is {book.status}')
print('Books in returned book list')
for index, book in enumerate(returned_books):
    print(f'{index + 1}, {book.title}, by {book.author} is {book.status}')
print('Books in checked out list')
for index, book in enumerate(checked_out_books):
    print(f'{index + 1}, {book.title}, by {book.author} is {book.status}')
print('Books in recycle bin')
for index, book in enumerate(recycle_bin):
    print(f'{index + 1}, {book.title}, by {book.author} is {book.status}')