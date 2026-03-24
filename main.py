import numpy as np
import matplotlib.pyplot as plt

# Initial population
P = 10

# Parameters
r = 0.1     # growth rate
K = 100     # max capacity

# Time
time = 100

P_list = []

for t in range(time):
    dP = r * P * (1 - P / K)
    P = P + dP
    P_list.append(P)

# Plotting of our data
plt.plot(P_list)
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Logistic Growth Model")
plt.show()