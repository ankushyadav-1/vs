import pandas as pd

rollno = ['10E01','12E05','10E12','12E15','10E25']
name = ['AMAN','RAGHAV','RISHI','MANVI','VIVEK']
year = [1982,1984,1982,1984,1982]
percentage = [98.5,86.9,76.6,80.0,87.5]

df = pd.DataFrame({"Rollno":rollno,"Name":name,"Year":year,"Percentage":percentage})
print(df)
# print('--index of DataFrame--')
# print(df.index,'\n')
# print('--columns of DataFrame--')
# print(df.columns,'\n')
# print('--shape of DataFrame--')
# print(df.shape,'\n')
# print('--size of DataFrame--')
# print(df.size,'\n')
# print('--axes of DataFrame--')
# print(df.axes,'\n')
# print("--Rows of DataFrame--")
# print(df,'\n')
# print("--Columns of DataFrame--")
# print(df.columns.tolist())