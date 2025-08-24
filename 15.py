<<<<<<< HEAD
#Considering the given dataframe empdf, Now write a menu driven program to retrieve the records as per the following conditions.

#a) To display those employees whose  bonus>=  entered bonus
#b) To display all those records whose Salary lies in the range of x and y.
#c) To display empcode, ename,salary & job  for the entered job only.
#d) To display those records for two entered zone only.
#e) To display Ename, Job and Salary of those Employees whose  job and salary is entered by the user.

import pandas as pd

# Sample employee DataFrame
data = {
    "EmpCode": [101, 102, 103, 104, 105, 106],
    "EName": ["Amit", "Priya", "Rahul", "Sneha", "Vikas", "Thomas"],
    "Salary": [45000, 52000, 38000, 60000, 75000, 40000],
    "Job": ["Manager", "Clerk", "Analyst", "Manager", "Clerk", "Analyst"],
    "Bonus": [5000, 3000, 2500, 7000, 6000, 2000],
    "Zone": ["North", "East", "West", "South", "East", "North"]
}

empdf = pd.DataFrame(data)

while True:
    print("\n===== Employee DataFrame Menu =====")
    print("1. Display employees with Bonus >= entered value")
    print("2. Display employees with Salary in given range")
    print("3. Display EmpCode, EName, Salary, Job for entered Job")
    print("4. Display employees for two entered Zones")
    print("5. Display EName, Job, Salary for entered Job and Salary")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        bonus_val = int(input("Enter bonus value: "))
        print(empdf[empdf["Bonus"] >= bonus_val])

    elif choice == 2:
        x = int(input("Enter lower Salary limit: "))
        y = int(input("Enter upper Salary limit: "))
        print(empdf[(empdf["Salary"] >= x) & (empdf["Salary"] <= y)])

    elif choice == 3:
        job_val = input("Enter Job title: ")
        print(empdf.loc[empdf["Job"] == job_val, ["EmpCode", "EName", "Salary", "Job"]])

    elif choice == 4:
        zone1 = input("Enter first Zone: ")
        zone2 = input("Enter second Zone: ")
        print(empdf[empdf["Zone"].isin([zone1, zone2])])

    elif choice == 5:
        job_val = input("Enter Job title: ")
        sal_val = int(input("Enter Salary value: "))
        print(empdf.loc[(empdf["Job"] == job_val) & (empdf["Salary"] == sal_val),
                        ["EName", "Job", "Salary"]])

    elif choice == 6:
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice, try again!")
=======
#Considering the given dataframe empdf, Now write a menu driven program to retrieve the records as per the following conditions.

#a) To display those employees whose  bonus>=  entered bonus
#b) To display all those records whose Salary lies in the range of x and y.
#c) To display empcode, ename,salary & job  for the entered job only.
#d) To display those records for two entered zone only.
#e) To display Ename, Job and Salary of those Employees whose  job and salary is entered by the user.

import pandas as pd

# Sample employee DataFrame
data = {
    "EmpCode": [101, 102, 103, 104, 105, 106],
    "EName": ["Amit", "Priya", "Rahul", "Sneha", "Vikas", "Thomas"],
    "Salary": [45000, 52000, 38000, 60000, 75000, 40000],
    "Job": ["Manager", "Clerk", "Analyst", "Manager", "Clerk", "Analyst"],
    "Bonus": [5000, 3000, 2500, 7000, 6000, 2000],
    "Zone": ["North", "East", "West", "South", "East", "North"]
}

empdf = pd.DataFrame(data)

while True:
    print("\n===== Employee DataFrame Menu =====")
    print("1. Display employees with Bonus >= entered value")
    print("2. Display employees with Salary in given range")
    print("3. Display EmpCode, EName, Salary, Job for entered Job")
    print("4. Display employees for two entered Zones")
    print("5. Display EName, Job, Salary for entered Job and Salary")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        bonus_val = int(input("Enter bonus value: "))
        print(empdf[empdf["Bonus"] >= bonus_val])

    elif choice == 2:
        x = int(input("Enter lower Salary limit: "))
        y = int(input("Enter upper Salary limit: "))
        print(empdf[(empdf["Salary"] >= x) & (empdf["Salary"] <= y)])

    elif choice == 3:
        job_val = input("Enter Job title: ")
        print(empdf.loc[empdf["Job"] == job_val, ["EmpCode", "EName", "Salary", "Job"]])

    elif choice == 4:
        zone1 = input("Enter first Zone: ")
        zone2 = input("Enter second Zone: ")
        print(empdf[empdf["Zone"].isin([zone1, zone2])])

    elif choice == 5:
        job_val = input("Enter Job title: ")
        sal_val = int(input("Enter Salary value: "))
        print(empdf.loc[(empdf["Job"] == job_val) & (empdf["Salary"] == sal_val),
                        ["EName", "Job", "Salary"]])

    elif choice == 6:
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice, try again!")
>>>>>>> 3c9c742133ba84fee9a4b2bed9f365c392f7b214
