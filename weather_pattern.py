#open the file and read the contents

f = open('weather_pattern.csv','r')
data = f.read()
rows = data.split('\n')

# store the value of file in list
weather_data = []
for row in rows:
	split_row  = row.split(',')
	weather_data.append(split_row)
	
#store only second colum on list
weather_column = []
for item in weather_data:
    weather_column.append(item[1])	

#remove header
weather = weather_column[1:]    

# count the weather 
weather_counts = {}
for item in weather:
    if item in weather_counts:
        weather_counts[item] = weather_counts[item] + 1
    else:
        weather_counts[item] = 1
print (weather_counts)     


   