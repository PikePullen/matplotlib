import numpy as np
import matplotlib.pyplot as plt

# 1d array
# 1000 evenly spaced points
# between 0 and 20
x = np.linspace(0, 20, 1000)

# totally pointless arbitrary function to generate data
y = np.sin(x) + 0.2 * x

plt.plot(x,y)
plt.xlabel("input")
plt.ylabel("output")
# semi-colon prevents text from rendering in draw. Only valid for some notebooks
plt.title("My Plot");
plt.show()

