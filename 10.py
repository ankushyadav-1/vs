import pandas as pd

series1 = pd.Series([1,3,5,7,9,2,4,6,8,0])

while True:
    print("Menu:")
    print("1. Display Series")
    print("2. Add element")
    print("3. Delete element")
    print("4. Display max & min")
    print("5. Exit")

    choice = int(input("Enter your Choice: "))

    if choice == 1:
        print(series1)
    
    elif choice == 2:
        data = input("enter element to add: ")
        newElement = pd.Series([data]) 
        series1 = pd.concat([series1,newElement], ignore_index= True)
        print('--Elemnet is added--')
        print(series1)

    elif choice == 3:
        print(series1)
        index = input('Enter element index which need to remove: ')
       
        if index in series1.index:
            series1 = series1.drop(index)
            print('--Element is removed--')
            print(series1)

        else:
            print('Index not found!!')


    elif choice == 4:
         print("--Max value of series--") 
         print(series1.max()) 
         print("--Min value of series--") 
         print(series1.min())

    elif choice == 5:
        print('Have a nice day.')
        break

    else:
        print('Choice not found.')