# with open("csv/products.csv") as file:
#     print(file.read())

import csv

with open("csv/products.csv") as file:
    csv_reader=csv.reader(file)
    next(csv_reader)
    for p in csv_reader:
        print(f"urun adi :{p[0]}, urun fiyati :{p[1]}")
