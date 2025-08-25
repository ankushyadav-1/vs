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