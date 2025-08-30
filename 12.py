import pandas as pd

df = pd.DataFrame({
    "Rollno": ["10E01", "12E05", "10E12", "12E15", "10E25"],
    "Name": ["AMAN", "RAGHAV", "RISHI", "MANVI", "VIVEK"],
    "Year": [1982, 1984, 1982, 1984, 1982],
    "Percentage": [98.5, 86.9, 76.6, 80.0, 87.5]
})

print(df)

print(f"Index of the DataFrame: {df.index}")
print(f"Columns of the DataFrame: {df.columns}")
print(f"Shape of the DataFrame: {df.shape}")
print(f"Size of the DataFrame: {df.size}")
print(f"Axes of the DataFrame: {df.axes}")
print(f"Rows of the DataFrame: {df.axes[0]}")
print(f"Columns of the DataFrame: {df.axes[1]}")