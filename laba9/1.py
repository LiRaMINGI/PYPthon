import numpy as np

with open('matrix.txt', 'w') as file:
    file.write("3,4,17,-3\n")
    file.write("5,11,-1,6\n")
    file.write("0,2,-5,8")

with open('matrix.txt', 'r') as file:
    matrix_data = file.readlines()

matrix = np.array([[int(x) for x in line.strip().split(',')] for line in matrix_data])

sum_of_elements = np.sum(matrix)

max_element = np.max(matrix)
min_element = np.min(matrix)

print(f"Сумма всех элементов: {sum_of_elements}")
print(f"Максимальный элемент: {max_element}")
print(f"Минимальный элемент: {min_element}")