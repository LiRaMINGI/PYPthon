import numpy as np

def find_max_after_zero(x):
  max_element = None
  for i in range(1, len(x)):
    if x[i - 1] == 0:
      if max_element is None or x[i] > max_element:
        max_element = x[i]

  return max_element

x = np.array([6, 2, 0, 3, 0, 89, 5, 7, 0])
max_element = find_max_after_zero(x)
print(f"Максимальный элемент: {max_element}")