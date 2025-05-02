import pandas as pd

s1 = pd.Series(range(1,10,2))
s2 = pd.Series(range(1,15,3))

print('sun of two series:')
print(s2+s1)

print('Subtraction of two series:')
print(s2-s1)

print('Multiplaction of two series:')
print(s2*s1)

print('division of two series:')
print(s2/s1)