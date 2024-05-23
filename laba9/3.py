import numpy as np

array = np.random.randn(10, 4)

minimum = np.min(array)
maximum = np.max(array)
mean = np.mean(array)
std = np.std(array)

first_five_rows = array[:5]

print("Массив:")
print(array)
print("\nМинимальное значение:", minimum)
print("Максимальное значение:", maximum)
print("Среднее значение:", mean)
print("Стандартное отклонение:", std)
print("\nПервые 5 строк:")
print(first_five_rows)