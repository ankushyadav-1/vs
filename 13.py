import pandas as pd

title = ['Book A', 'Book B', 'Book C']
author = ['Author 1', 'Author 2', 'Author 3']
price = [250, 300, 200]
books = pd.DataFrame({"Title":title,"Author":author,"Price":price}, index= ('B001','B002','B003'))

while True:
    print('1. To get book detail.')
    print('2. exit.')

    choice = input('Enter your choice: ')

    match choice:
        case '1':
            print(books.index)
            bid = input('Enter Book Number: ')
            book_id = bid.upper()
            if book_id.upper() in books.index:
                print('\n',books.loc[book_id],'\n')

            else:
                print('\nBook Number not found!!\n')

        case '2':
            print('Have A Nice Day.')
            break