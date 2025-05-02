import pandas as pd

d1 = {}
length = int(input('Enter the length of your series: '))

for i in range(1, length+1):
    index = int(input("Enter index in number: "))
    data = input(f"Enter {i} value of series: ")
    d1[index] = data
    
s1 = pd.Series(d1)

print("Series:")
print(s1)
print('\n')

print("\nData type:")
print(s1.dtype)
print('\n')

print("Shape:")
print(s1.shape)
print('\n')

print("No. of bytes:")
print(s1.nbytes)
print('\n')

print("No. of Dimensions:")
print(s1.ndim)
print('\n')

print("Has NaNs:")
print(s1.hasnans)
print('\n')

print("Empty:")
print(s1.empty)
print('\n')

print("Index:")
print(s1.index)
print('\n')

print("Values:")
print(s1.values)
print('\n')

print("Shape:")
print(s1.shape)
