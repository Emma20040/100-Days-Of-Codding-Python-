import pandas

data =pandas.read_csv("./Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data)
grey_squirrel_count = len(data[data['Primary Fur Color']== 'Gray'])
cinnamon_count = len(data[data['Primary Fur Color']== 'Cinnamon'])
black_squirrel_count = len(data[data['Primary Fur Color']== 'Black'])

print(grey_squirrel_count)
print(cinnamon_count)
print(black_squirrel_count)

# creating dataframe
data_dict ={
    "fur color": ['Grey', 'Cinnamon', 'Black'],
    "count": [grey_squirrel_count, cinnamon_count, black_squirrel_count]
}
dataframe= pandas.DataFrame(data_dict)
dataframe.to_csv("./Day 25/squirrel_count.csv")