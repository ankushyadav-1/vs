import pandas as pd

df1 = pd.DataFrame({
    "A": [10, 20, 30],
    "B": [40, 50, 60],
    "C": [70, 80, 90]
})

df2 = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [4, 5, 6],
    "C": [7, 8, 9]
})

def menu():
    print("\n--- Binary Operations Menu ---")
    print("1. Display DataFrames")
    print("2. Addition (df1 + df2)")
    print("3. Subtraction (df1 - df2)")
    print("4. Multiplication (df1 * df2)")
    print("5. Division (df1 / df2)")
    print("6. Exit")

while True:
    menu()
    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        print("\nFirst DataFrame (df1):")
        print(df1)
        print("\nSecond DataFrame (df2):")
        print(df2)

    elif choice == 2:
        print("\nAddition of df1 and df2:")
        print(df1.add(df2))

    elif choice == 3:
        print("\nSubtraction of df1 and df2:")
        print(df1.sub(df2))

    elif choice == 4:
        print("\nMultiplication of df1 and df2:")
        print(df1.mul(df2))

    elif choice == 5:
        print("\nDivision of df1 and df2:")
        print(df1.div(df2))

    elif choice == 6:
        print("Exiting... Thank you!")
        break

    else:
        print("Invalid choice! Please enter a number between 1–6.")