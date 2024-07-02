searched_book= input()

count_searched_books = 0
result = ''

while True:
    book_name = input()

    if book_name == 'No More Books':
        result = f'The book you search is not here!\nYou checked {count_searched_books} books.'
        break

    if book_name == searched_book:
        result = f'You checked {count_searched_books} books and found it.'
        break

    count_searched_books += 1


print(result)