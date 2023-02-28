# import csv

# with open("C:/python_learn/python/csv-with-python/weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     temperatures=[]
#     for  row in data:
#         #print(row)
#         temperatures.append(row[1])
    
#     print(temperatures)

import pandas

data=pandas.read_csv("C:/python_learn/python/csv-with-python/weather_data.csv")
print(data)
print(data["temp"])