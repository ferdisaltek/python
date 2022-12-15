from csv import DictReader
import csv

with open("csv/products.csv") as file:
    csv_reader=DictReader(file,delimiter="|")
    print(csv_reader)
    for _ in  csv_reader:
        print(_)