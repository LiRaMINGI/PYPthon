import csv
from random import shuffle
import os


class CSVReader:
    def __init__(self, filename, separator=","):
        with open(filename) as csv_file:
            scv_file = csv.reader(csv_file, delimiter=separator)
            self.data = []
            self.headers = []
            self.rows_len = []
            self.rows_data_types = ["integer", "integer", "integer", "string", "string", "integer", "integer",
                                    "integer", "string", "float", "string", "string"]

            for i, row in enumerate(scv_file):
                if i == 0:
                    self.headers = row
                    self.rows_len = [0 for _ in range(len(row))]
                else:
                    self.data.append(row)

                for j, value in enumerate(row):
                    self.rows_len[j] = max(self.rows_len[j], len(value))

    def show(self, print_type="top", count=5):
        for i, header in enumerate(self.headers):
            print(header + (self.rows_len[i] - len(header)) * " " + " | ", end="")
        print()

        for i, header in enumerate(self.headers):
            print(("_" * self.rows_len[i]) + "_|_", end="")
        print()

        output_data = self.data.copy()
        if print_type == "top":
            output_data = output_data[:count]
        elif print_type == "bottom":
            output_data = output_data[-count:]
        elif print_type == "random":
            shuffle(output_data)
            output_data = output_data[:count]

        for row in output_data:
            for i, length in enumerate(self.rows_len):
                print(row[i] + (length - len(row[i])) * " " + " | ", end="")
            print()

    def info(self):
        print(f"\nРазмер таблицы: {len(self.data)}x{len(self.headers)}")
        non_null_values = [0 for _ in range(len(self.headers))]
        for string in self.data:
            for i, value in enumerate(string):
                if value != "":
                    non_null_values[i] += 1

        for i in range(len(self.headers)):
            print(
                f"Cтолбец '{self.headers[i]}' имеет {non_null_values[i]} не пустых значений типа {self.rows_data_types[i]}")

    def del_none(self):
        new_data = []
        for i in self.data:
            if "" not in i:
                new_data.append(i)
        self.data = new_data

    def make_ds(self, folder_name="workdata", first_folder="learning", second_folder="testing",
                first_file="train.csv", second_file="test.csv", percent=0.7):
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        if not os.path.exists(folder_name + "/" + first_folder):
            os.mkdir(folder_name + "/" + first_folder)
        if not os.path.exists(folder_name + "/" + second_folder):
            os.mkdir(folder_name + "/" + second_folder)

        temp_data = self.data.copy()
        shuffle(temp_data)
        with open(folder_name + "/" + first_folder + "/" + first_file, 'w', newline='') as file1:
            with open(folder_name + "/" + second_folder + "/" + second_file, 'w', newline='') as file2:
                first_writer = csv.writer(file1)
                second_writer = csv.writer(file2)
                first_writer.writerow(self.headers)
                second_writer.writerow(self.headers)

                border = len(self.data) * percent
                for i, string in enumerate(temp_data):
                    if i < border:
                        first_writer.writerow(string)
                    else:
                        second_writer.writerow(string)


obj = CSVReader("Titanic.csv", ",")
obj.show("top", 10)
obj.info()
obj.del_none()
obj.show("top", 10)
obj.info()
obj.make_ds()
