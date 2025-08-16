#Given the ages of 80 participants in some game. Write a program to plot a histogram from given data with 6 bins of your choice.
#Data = [ 9,10,11,13,13,15,16,17,18,19,21,23,23,23,24,24,25,25,25,25,25, 26,26,27,27,27, 27, 29,30,30,30,30,31,33,34,34,35,36, 36,37,37,37, 38,39,40,40,40,41,42,43,43,39,30,31,32,33,34,35,36,37,38,39,36,37,38,40,41,42,43,44,45,50,51,52,53,54,55,56,57,58]


import matplotlib.pyplot as plt

# Given data
data = [9,10,11,13,13,15,16,17,18,19,21,23,23,23,24,24,25,25,25,25,25, 
        26,26,27,27,27,27,29,30,30,30,30,31,33,34,34,35,36,36,37,37,37,
        38,39,40,40,40,41,42,43,43,39,30,31,32,33,34,35,36,37,38,39,36,
        37,38,40,41,42,43,44,45,50,51,52,53,54,55,56,57,58]

# Plot histogram with 6 bins
plt.hist(data, bins=6, edgecolor="black", color="skyblue")

# Labels and title
plt.xlabel("Age Groups")
plt.ylabel("Number of Participants")
plt.title("Histogram of Ages of 80 Participants")

# Show the plot
plt.show()

