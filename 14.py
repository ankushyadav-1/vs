import pandas as pd

title = ['Book A', 'Book B', 'Book C']
author = ['Author 1', 'Author 2', 'Author 3']
price = [250, 300, 200]
books = pd.DataFrame({"Title":title,"Author":author,"Price":price}, index= ('B001','B002','B003'))

while True:
    print('1.list all books.')
    print('2.To add/update a Book.')
    print('3.Delete any Book.')
    print('4.Delete any Row')
    print('5.Exit is here.')

    choice = int(input('Enter your choice: '))

    if choice == 1:
        print(books)

    elif choice == 2:
        book_id = input('Enter your Book id: ')
        title = input('Enter Book Name: ')
        author = input('Enter Author name: ')
        price = input('Enter Book Price: ')
        books.loc[book_id] = [title, author, price]
        print(books)

    elif choice == 3:
        print(books)
        book_id = input('Enter Book Id: ')
        books = books.drop(book_id, errors='ignore')
        print('--Data Updated ')

    elif choice == 4:
        print(books)
        book_id = input('Enter Book Id to delete row (example: B001): ')
        books = books.drop(book_id, axis=0, errors='ignore')
        print('--Data Updated ')


    elif choice == 5:
        print('Have a nice day.')
        break

    else:
        print('Choice not found!!')
        break
