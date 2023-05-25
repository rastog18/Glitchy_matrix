import pandas

data = pandas.read_csv("Time Converter.csv")
dict_data = {value.TZ:value.STD for (key,value) in data.iterrows()}
list_place = [item for item in dict_data.keys()]
list_time = [item for item in dict_data.values()]
