import pandas 

data = pandas.read_csv("./Day 25/weather_data.csv")
print((data))
print(type(['temp']))

data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(temp_list)
total =0
for temp in temp_list:
    total += temp
average = total/len(temp_list)
print(average)
# or using pandas to calculate the average temperature

print(data['temp'].mean())
# printing the highest temperature

print(data['temp'].max())

# get data in a row
print(data[data.day== 'Monday'])

# printing the row that had the max temperature 
max_temp = data['temp'].max()
print(data[data.temp == max_temp])

# creating a dataframe from scratch
new_dat_dict ={
    "students" :["john", "mary", "paul", "peter"],
    "scores": [12, 13, 16, 20]

}

new_data= pandas.DataFrame(new_dat_dict)
# print(new_data)
# creating a new csv file
new_data.to_csv("./Day 25/ new_data.csv")
