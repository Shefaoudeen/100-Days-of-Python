"""
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        print(row)
        temperature.append((row[1]))
    print(temperature)
 """

import pandas

data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()
temp_list = data["temp"].to_list()

#print(data["temp"].mean())
#max_temp = (data["temp"].max())
#print(data[data.temp == max_temp])
#print((sum(temp_list)/len(temp_list)))

monday = data[data.day == 'Monday']
c = monday.temp[0]
print((9*c/5) + 32)