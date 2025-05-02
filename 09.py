import pandas as pd
import numpy as np

d1 = {}
length = int(input('Enter the number of employees : '))

for i in range(1, length+1):
    name  = input(f"Enter name of {i} employee: ")
    salary  = input(f"Enter salary of {name}: ")
    lname = name.lower()
    print('lname', lname)
    d1[lname] = salary 

s1 = pd.Series(d1)
print(s1)

empName = input("Enter name of employee whose salary to update: ")
eName = empName.lower()
if eName in s1:
    new_salary = input('Enter new salary: ')
    s1[eName] = new_salary
else:
    print('Employee not found!!')