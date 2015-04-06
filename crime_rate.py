# Find the lowest crime rate in U.S
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')

full_data = []
for row in rows:
    split_row = row.split(",")
    split_row[1] = int(split_row[1])
    full_data.append(split_row)
    

city = ""
for item in full_data:
    if item[1] == 130:#how or why 130?
        city = item[0]
print city       