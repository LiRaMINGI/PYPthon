import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

x = np.linspace(-1, 1, 100)
colors = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'black']

fig, ax = plt.subplots()

for n in range(1, 8):
    y = legendre(n)(x)

    ax.plot(x, y, color=colors[n-1], label=f'n = {n}')

ax.set_title('Полиномы Лежандра')
ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.2), ncol=4, fancybox=True, shadow=True)
plt.show()