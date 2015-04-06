#first open the file

f = open('weather_pattern.csv','r')
data = f.read()
rows = data.split('\n')