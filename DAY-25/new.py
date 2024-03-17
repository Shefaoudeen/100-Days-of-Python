import pandas

data_set = pandas.read_csv("Squirrel_Data.csv")

color_data = data_set["Primary Fur Color"]

grey_sq_count = len(data_set[color_data == "Gray"])
red_sq_count = len(data_set[color_data == "Cinnamon"])
black_sq_count = len(data_set[color_data == "Black"])

print(grey_sq_count)
print(red_sq_count)
print(black_sq_count)

data_dict = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count" : [grey_sq_count,red_sq_count,black_sq_count]
}

new_frame = pandas.DataFrame(data_dict)
new_frame.to_csv("count.csv")