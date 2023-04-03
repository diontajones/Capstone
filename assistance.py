def search_by_title():
    keyword = input('Enter a keyword from the title: ')
    found_books = [book for book in books if keyword.lower() in book.title.lower()]
    if found_books:
        for book in found_books:
            print(book)
    else:
        print(f'No books with "{keyword}" in the title found.')