import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,1000)

plt.plot(x, np.sin(x))
plt.show()