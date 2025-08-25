import pandas as pd

def create_dataframe():
    aid_df = pd.DataFrame({
        "State": ["Andhra", "Bihar", "Delhi", "Kerala", "Punjab", "W.B."],
        "Toy": [120, 100, 90, 60, 110, 80],
        "Books": [200, 180, 150, 120, 170, 160],
        "Uniform": [80, 70, 60, 90, 100, 85],
        "Shoes": [60, 55, 50, 65, 70, 60]
    })
    return aid_df

def menu():
    print("\n--- Aid DataFrame Menu ---")
    print("1. Show the data of Toy column")
    print("2. Show the data of Books and Uniform columns")
    print("3. Show the data of Toy and Uniform columns for top 3 rows (loc)")
    print("4. Show the data of top 3 rows and first 3 columns (iloc)")
    print("5. Set the index as State and display the DataFrame")
    print("6. Show the data for Toy, Uniform and Shoes columns of Andhra, Bihar and W.B.")
    print("7. Reset the index and display the DataFrame")
    print("8. Exit")

aid_df = create_dataframe()

while True:
    menu()
    choice = int(input("Enter your choice (1-8): "))

    if choice == 1:
        print("\nToy column:")
        print(aid_df["Toy"])

    elif choice == 2:
        print("\nBooks and Uniform columns:")
        print(aid_df[["Books", "Uniform"]])

    elif choice == 3:
        print("\nToy and Uniform columns (top 3 rows):")
        print(aid_df.loc[0:2, ["Toy", "Uniform"]])

    elif choice == 4:
        print("\nTop 3 rows and first 3 columns:")
        print(aid_df.iloc[0:3, 0:3])

    elif choice == 5:
        aid_df = aid_df.set_index("State")
        print("\nDataFrame with State as index:")
        print(aid_df)

    elif choice == 6:
        if "State" in aid_df.columns:
            aid_df = aid_df.set_index("State")
        print("\nData for Toy, Uniform, Shoes of Andhra, Bihar, W.B.:")
        print(aid_df.loc[["Andhra", "Bihar", "W.B."], ["Toy", "Uniform", "Shoes"]])

    elif choice == 7:
        aid_df = aid_df.reset_index()
        print("\nDataFrame after resetting index:")
        print(aid_df)

    elif choice == 8:
        print("Exiting... Thank you!")
        break

    else:
        print("Invalid choice! Please enter a number between 1–8.")