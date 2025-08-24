import pandas as pd

rollno = ['10E01','12E05','10E12','12E15','10E25']
name = ['AMAN','RAGHAV','RISHI','MANVI','VIVEK']
year = [1982,1984,1982,1984,1982]
percentage = [98.5,86.9,76.6,80.0,87.5]

df = pd.DataFrame({'rollno':rollno,'name':name,'year':year,'percentage':percentage})
print(df)

df = df.set_index('rollno')
print(df)

df = df.reset_index()
print(df)

df = df.set_index('name')
print(df)

df = df.reset_index()
print(df)

df = df.set_index('year')
print(df)

df = df.reset_index()
print(df)

df = df.set_index('percentage')
print(df)

df = df.reset_index()
print(df)
