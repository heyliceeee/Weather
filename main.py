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
print(data)