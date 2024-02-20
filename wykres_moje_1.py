import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 101)
y = np.linspace(-2, 2, 101)

X, Y = np.meshgrid(x, y)

Z1 = np.exp(-X ** 2 - Y ** 2)
Z1 = np.exp(-X ** 2 - Y ** 2)
Z2 = np.exp(-(X - 1) ** 2 - Y ** 2)
Z3 = np.exp(-(X + 1) ** 2 - Y ** 2)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot_surface(X, Y, Z1, cmap='Reds')
ax.plot_surface(X, Y, Z2, cmap='Blues')
ax.plot_surface(X, Y, Z3, cmap='Greens')

ax.set_xlabel('Coś X')
ax.set_ylabel('Coś Y')
ax.set_zlabel('Coś Z')

ax.set_title("Wykres próbny")

plt.show()
