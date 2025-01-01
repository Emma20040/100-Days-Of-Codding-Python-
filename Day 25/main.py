import csv
with open("./Day 25/weather_data.csv") as data:
    weather_data = csv.reader(data)
    tempearture = []
    for row in weather_data:
        if row[1] != 'temp':
            tempearture.append(int(row[1]))


    print(tempearture)