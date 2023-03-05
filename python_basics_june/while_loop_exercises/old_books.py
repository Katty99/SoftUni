searched_book = input()
book_checked = input()
checked_counter = 0
book_is_found = False
while book_checked != 'No More Books':
    if book_checked == searched_book:
        book_is_found = True
        break
    checked_counter += 1
    book_checked = input()

if book_is_found:
    print(f'You checked {checked_counter} books and found it.')
else:
    print(f'The book you search is not here!')
    print(f'You checked {checked_counter} books.')
