#Write a program in Python Pandas to create the following DataFrame“df” from a Dictionary. Draw line charts to show the plotting of score1and score 2 for all batsman. Put legends and titles. Specify different colours and line styles of your choice for both the plotted lines. Change font size of the titles to 15 and color to green.

#B_No	Name	Score1	Score2
#1	M.S. Dhoni	95	80
#2	Virat Kohli	85	92
#3	Sachin	110	75
#4	Kartik	75	80


import pandas as pd
import matplotlib.pyplot as plt 

dict1 = {'B_No': [1,2,3,4], 'Name': ['M.S. Dhoni','Virat Kohli','Sachin','Kartik'], 'Score1': [95,85,110,75], 'Score2': [80,92,75,80]}
df = pd.DataFrame(dict1)    
print(df)

x = df['B_No']  
y1 = df['Score1']
y2 = df['Score2']   

plt.plot(x,y1)  
plt.plot(x,y2)  
plt.xlabel('Batsman Number')    
plt.ylabel('Scores')    
plt.title('Scores of Batsman')            
plt.legend(['Score1','Score2'])
plt.show()  