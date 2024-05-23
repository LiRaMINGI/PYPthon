import numpy as np

def run_length_encoding(x):
  numbers = []
  counts = []
  current_number = x[0]
  current_count = 1
  for i in range(1, len(x)):
    if x[i] == current_number:
      current_count += 1
    else:
      numbers.append(current_number)
      counts.append(current_count)
      # Обновление текущих значений
      current_number = x[i]
      current_count = 1

  numbers.append(current_number)
  counts.append(current_count)


  return np.array(numbers), np.array(counts)

x = np.array([2, 2, 2, 3, 3, 3, 5])
numbers, counts = run_length_encoding(x)
print(f"Числа: {numbers}")
print(f"Количества: {counts}")