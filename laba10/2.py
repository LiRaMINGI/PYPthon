import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 10, 1000)  # Время от 0 до 10 с шагом 0.01
amplitudes = [1, 1]  # Амплитуды по оси x и y

frequency_ratios = [(3, 2), (3, 4), (5, 4), (5, 6)]

for i, (freq_x, freq_y) in enumerate(frequency_ratios):
    x = amplitudes[0] * np.sin(2 * np.pi * freq_x * t) # Вычисление координат кривой Лисажу
    y = amplitudes[1] * np.sin(2 * np.pi * freq_y * t)

# Построение графика
    plt.subplot(2, 2, i + 1)  # Размещение графика на сетке 2x2
    plt.plot(x, y)
    plt.title(f'Соотношение частот: {freq_x}:{freq_y}')
    plt.xlabel('x')
    plt.ylabel('y')


plt.tight_layout()  # Автоматическая подстройка расстояний между графиками
plt.show()