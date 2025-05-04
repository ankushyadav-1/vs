import pandas as pd
import numpy as np

population = pd.Series({'Delhi': 19000000, 'Mumbai': 20400000, 'Kolkata': 14900000, 'Chennai': 11200000})

avg_income = pd.Series({'Delhi': 350000, 'Mumbai': 400000, 'Kolkata': 300000, 'Chennai': 320000})

per_capita_income= population/avg_income

print('--Per Capita Income--')
print(per_capita_income)