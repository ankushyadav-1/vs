#Consider a csv file  and write a menu driven program to create dataframes from the given csv with the following specifications:
#(a) Read csv and transfer it to a dataframe stdf.
#(b) Accept the column names which the user wants to include in the dataframe
#(c) Accept the number of rows user wants to skip from the csv while creating the dataframe.
#(d) Write the updated dataframe into a new csv file named "student1"


import pandas as pd

filename = "student.csv"



def menu():
    print("\n--- Student CSV DataFrame Menu ---")
    print("1. Read CSV into DataFrame (stdf)")
    print("2. Create DataFrame with selected columns")
    print("3. Create DataFrame by skipping rows")
    print("4. Write updated DataFrame to new CSV (student1.csv)")
    print("5. Display current DataFrame")
    print("6. Exit")

while True:
    menu()
    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        try:
            stdf = pd.read_csv(filename)
            print("\n(a) DataFrame created successfully from CSV!")
            print(stdf)
        except FileNotFoundError:
            print("\nError: File not found at given path.")

    elif choice == 2:
        if stdf is not None:
            cols = input("Enter column names separated by comma: ").split(",")
            cols = [c.strip() for c in cols]
            try:
                stdf = pd.read_csv(filename, usecols=cols)
                print("\n(b) DataFrame created with selected columns:")
                print(stdf)
            except ValueError:
                print("\nError: One or more columns not found in CSV.")
        else:
            print("\nPlease read the CSV first (Option 1).")

    elif choice == 3:
        if stdf is not None:
            skip = int(input("Enter number of rows to skip: "))
            stdf = pd.read_csv(filename, skiprows=skip)
            print(f"\n(c) DataFrame created by skipping {skip} rows:")
            print(stdf)
        else:
            print("\nPlease read the CSV first (Option 1).")

    elif choice == 4:
        if stdf is not None:
            stdf.to_csv(newfile, index=False)
            print(f"\n(d) Updated DataFrame written to {newfile}")
        else:
            print("\nPlease create the DataFrame first (Option 1).")

    elif choice == 5:
        if stdf is not None:
            print("\nCurrent DataFrame:")
            print(stdf)
        else:
            print("\nNo DataFrame available. Please read CSV first.")

    elif choice == 6:
        print("Exiting... Thank you!")
        break

    else:
        print("Invalid choice! Please enter a number between 1–6.")
