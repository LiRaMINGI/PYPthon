import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Определение параметров графика
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)

# Определение функции MSE
def mse(x, y):
    return (x**2 + y**2) / 2

# Вычисление значений MSE
Z = mse(X, Y)

# Создание первого графика
fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax1.plot_surface(X, Y, Z)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('MSE')
ax1.set_title('MSE (Линейный масштаб)')

# Создание второго графика с логарифмической осью z
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
ax2.plot_surface(X, Y, Z)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('MSE (Логарифмический масштаб)')
ax2.set_title('MSE (Логарифмический масштаб)')
ax2.set_zscale('log')

# Отображение графиков
plt.show()

