import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

species_column = iris[:, 4]
unique_species, counts = np.unique(species_column, return_counts=True)
print("Уникальные виды цветов:")
for i in range(len(unique_species)):
  print(f"{unique_species[i]}: {counts[i]}")