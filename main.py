import os
import csv
import pandas

data = []
dir_path = os.path.dirname(os.path.abspath(__file__)) # get the path of the current file

def get_data_from_csv():
    """
    get data from csv file
    :return: list data
    """
    file_path = dir_path + "/data/weather_data.csv"
    return pandas.read_csv(file_path)

data = get_data_from_csv()
print("\ndata: \n", data)

print("\naverage temperature: ", float(data["temp"].mean())) # average temperature

max_temperature = float(data["temp"].max()) # max value temperature
print("\nmax temperature: ", max_temperature)

temperatures = data["temp"] # temperature column
day_highest_temperature = data[data.temp == max_temperature] # data who day with the highest temperature
print("\nday with the highest temperature: \n", day_highest_temperature)

monday = data[data.day == "Monday"] # data who day is Monday
monday_temperature = float(monday.temp[0]) # monday temperature
fahrenheit = (monday_temperature * 1.8) + 32 # convert temperature to Fahrenheit
print("monday temperature in fahrenheit: ", fahrenheit)