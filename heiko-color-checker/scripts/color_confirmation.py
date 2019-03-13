# use python's the CGI package
import cgi
import csv


# get the output of the form.
form = cgi.FieldStorage()

# get an input filed from the form called 'name'
colorName = form.getvalue('new_color')
hexColor = form.getvalue('hex_color')
message = ""

#this function adds a row to the csv file with the new color
def add_hex_color(colorName, hexColor):
    #create var for first column input
    colorBadName = colorName.replace(" ", "_").lower()
    #check if the name already exists and return message if true
    with open('colors.csv', 'r') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                if row:
                    if colorBadName == row[0]:
                        return colorName + " already exists please choose a different name"              
    
    #fields to be filled into the csv file
    fields = [colorBadName, colorName.title(), hexColor]
    #write fields to csv file and return success message
    with open('colors.csv', 'a') as csvFile:
            csvFile.write("\n" + ",".join(fields))
            message = colorName + ", was added to the database Successfully"
    return message


message = add_hex_color(colorName, hexColor)

# send an html response.
print("""
<html>
<body>
<p>
%s
</p>
<a href="index.html">Go Home</a>
</body>
</html>
""" % message)




