#Write a python program to represent the use of iterrows() and iteritems() in a DataFrame through menu driven.


import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    "Name": ["Amit", "Bhavna", "Chirag", "Divya"],
    "Age": [21, 22, 20, 23],
    "Marks": [85, 90, 88, 92]
})

def menu():
    print("\n--- Menu: Demonstrating iterrows() and iteritems() ---")
    print("1. Display DataFrame")
    print("2. Iterate using iterrows()")
    print("3. Iterate using iteritems()")
    print("4. Exit")

while True:
    menu()
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        print("\nDataFrame:")
        print(df)

    elif choice == 2:
        print("\nIteration using iterrows():")
        for index, row in df.iterrows():
            print(f"Index {index}: Name={row['Name']}, Age={row['Age']}, Marks={row['Marks']}")

    elif choice == 3:
        print("\nIteration using items():")
        for column, values in df.items():   
            print(f"\nColumn: {column}")
            print(values.to_list())

    elif choice == 4:
        print("Exiting... Thank you!")
        break

    else:
        print("Invalid choice! Please enter a number between 1–4.")
