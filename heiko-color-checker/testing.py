# impor

# with open('colors.csv', 'r') as csvFile:
#     reader = csv.reader(csvFile)
    
#     for row in reader:
#         print(row)
#     print(type(reader))
# csvFile.close()

# l = list(range(0,10)) + ['a', 'b', 'c', 'd', 'e', 'f']
# print(l)
#form = cgi.FieldStorage()

import csv

def checkColor(color, check):
    check_values = {'colorName': 0, 'hexNum': 2}
    to_check = check_values[check]
    isColor = False

    with open('colors.csv', 'r') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                if color == row[to_check]:
                    return row[1]
                    
    csvFile.close()

color = "#00308f"
message = ''
colorName = checkColor(color, 'hexNum')  
if colorName:
    message = colorName + ", this is a color that has a name"

print(message)

