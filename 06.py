import pandas as pd
import numpy as np

dict1 = {'jan':31,'feb':28,'mar':31}
s1 = pd.Series(dict1)
print(s1)

nint = int(input("Enter number: "))
ar1 = np.array(range(1,nint+1))
s2 = pd.Series(ar1)
print(s2) 