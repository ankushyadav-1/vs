<<<<<<< HEAD
# Write a menu driven python program to create a DataFrame with marks of 5 students in 5 subjects. And the handle the following options using menu. 

#(a) Add a column Total showing sum of marks of all subjects.
#(b) Now increase 5 marks in the 'Total' column for all students 
#(c) Add one more column Percentage, calculated on the basis of
#'Total' marks obtained out of 500 
#(d) Add a new row in the above DataFrame.( Using loc)
#(e) Now modify the English marks of Thomas as 70,accordingly update his Total and percentage.
#(f) Add two more rows together in the above dataFrame.( Using append)


import pandas as pd

# Step 1: Create initial DataFrame
df = pd.DataFrame({
    "Name": ["John", "Alice", "Robert", "Thomas", "Sophia"],
    "English": [80, 75, 60, 65, 70],
    "Maths": [90, 85, 70, 60, 75],
    "Science": [85, 80, 75, 70, 65],
    "History": [70, 60, 80, 75, 85],
    "Geography": [75, 70, 65, 80, 90]
})

def menu():
    print("\n--- Student Marks DataFrame Menu ---")
    print("1. Display DataFrame")
    print("2. Add column 'Total'")
    print("3. Increase 5 marks in 'Total' column")
    print("4. Add column 'Percentage'")
    print("5. Add a new row (using loc)")
    print("6. Modify English marks of Thomas = 70 and update Total & Percentage")
    print("7. Add two more rows together (using concat)")
    print("8. Exit")

while True:
    menu()
    choice = int(input("Enter your choice (1-8): "))

    if choice == 1:
        print("\nCurrent DataFrame:")
        print(df)

    elif choice == 2:
        df["Total"] = df[["English", "Maths", "Science", "History", "Geography"]].sum(axis=1)
        print("\nColumn 'Total' added successfully!")
        print(df)

    elif choice == 3:
        if "Total" in df.columns:
            df["Total"] = df["Total"] + 5
            print("\nIncreased 5 marks in 'Total' column:")
            print(df)
        else:
            print("\nPlease add 'Total' column first (Option 2).")

    elif choice == 4:
        if "Total" in df.columns:
            df["Percentage"] = (df["Total"] / 500) * 100
            print("\nColumn 'Percentage' added successfully!")
            print(df)
        else:
            print("\nPlease add 'Total' column first (Option 2).")

    elif choice == 5:
        new_row = {"Name": "David", "English": 65, "Maths": 70, "Science": 75, "History": 80, "Geography": 85}
        df.loc[len(df)] = new_row
        print("\nNew row added successfully (David).")
        print(df)

    elif choice == 6:
        df.loc[df["Name"] == "Thomas", "English"] = 70
        df["Total"] = df[["English", "Maths", "Science", "History", "Geography"]].sum(axis=1)
        df["Percentage"] = (df["Total"] / 500) * 100
        print("\nUpdated Thomas' English marks to 70, and recalculated Total & Percentage:")
        print(df)

    elif choice == 7:
        new_rows = pd.DataFrame([
            {"Name": "Emma", "English": 75, "Maths": 80, "Science": 85, "History": 70, "Geography": 90},
            {"Name": "Liam", "English": 60, "Maths": 65, "Science": 70, "History": 75, "Geography": 80}
        ])
        df = pd.concat([df, new_rows], ignore_index=True)
        print("\nTwo new rows (Emma & Liam) added successfully.")
        print(df)

    elif choice == 8:
        print("Exiting... Thank you!")
        break

    else:
        print("Invalid choice! Please enter a number between 1–8.")
=======
# Write a menu driven python program to create a DataFrame with marks of 5 students in 5 subjects. And the handle the following options using menu. 

#(a) Add a column Total showing sum of marks of all subjects.
#(b) Now increase 5 marks in the 'Total' column for all students 
#(c) Add one more column Percentage, calculated on the basis of
#'Total' marks obtained out of 500 
#(d) Add a new row in the above DataFrame.( Using loc)
#(e) Now modify the English marks of Thomas as 70,accordingly update his Total and percentage.
#(f) Add two more rows together in the above dataFrame.( Using append)


import pandas as pd

# Step 1: Create initial DataFrame
df = pd.DataFrame({
    "Name": ["John", "Alice", "Robert", "Thomas", "Sophia"],
    "English": [80, 75, 60, 65, 70],
    "Maths": [90, 85, 70, 60, 75],
    "Science": [85, 80, 75, 70, 65],
    "History": [70, 60, 80, 75, 85],
    "Geography": [75, 70, 65, 80, 90]
})

def menu():
    print("\n--- Student Marks DataFrame Menu ---")
    print("1. Display DataFrame")
    print("2. Add column 'Total'")
    print("3. Increase 5 marks in 'Total' column")
    print("4. Add column 'Percentage'")
    print("5. Add a new row (using loc)")
    print("6. Modify English marks of Thomas = 70 and update Total & Percentage")
    print("7. Add two more rows together (using concat)")
    print("8. Exit")

while True:
    menu()
    choice = int(input("Enter your choice (1-8): "))

    if choice == 1:
        print("\nCurrent DataFrame:")
        print(df)

    elif choice == 2:
        df["Total"] = df[["English", "Maths", "Science", "History", "Geography"]].sum(axis=1)
        print("\nColumn 'Total' added successfully!")
        print(df)

    elif choice == 3:
        if "Total" in df.columns:
            df["Total"] = df["Total"] + 5
            print("\nIncreased 5 marks in 'Total' column:")
            print(df)
        else:
            print("\nPlease add 'Total' column first (Option 2).")

    elif choice == 4:
        if "Total" in df.columns:
            df["Percentage"] = (df["Total"] / 500) * 100
            print("\nColumn 'Percentage' added successfully!")
            print(df)
        else:
            print("\nPlease add 'Total' column first (Option 2).")

    elif choice == 5:
        new_row = {"Name": "David", "English": 65, "Maths": 70, "Science": 75, "History": 80, "Geography": 85}
        df.loc[len(df)] = new_row
        print("\nNew row added successfully (David).")
        print(df)

    elif choice == 6:
        df.loc[df["Name"] == "Thomas", "English"] = 70
        df["Total"] = df[["English", "Maths", "Science", "History", "Geography"]].sum(axis=1)
        df["Percentage"] = (df["Total"] / 500) * 100
        print("\nUpdated Thomas' English marks to 70, and recalculated Total & Percentage:")
        print(df)

    elif choice == 7:
        new_rows = pd.DataFrame([
            {"Name": "Emma", "English": 75, "Maths": 80, "Science": 85, "History": 70, "Geography": 90},
            {"Name": "Liam", "English": 60, "Maths": 65, "Science": 70, "History": 75, "Geography": 80}
        ])
        df = pd.concat([df, new_rows], ignore_index=True)
        print("\nTwo new rows (Emma & Liam) added successfully.")
        print(df)

    elif choice == 8:
        print("Exiting... Thank you!")
        break

    else:
        print("Invalid choice! Please enter a number between 1–8.")
>>>>>>> 3c9c742133ba84fee9a4b2bed9f365c392f7b214
