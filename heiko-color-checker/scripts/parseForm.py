# use python's the CGI package
import cgi
import csv


# get the output of the form.
form = cgi.FieldStorage()

def checkColor(color, check):
    check_values = {'colorName': 0, 'hexNum': 2}
    to_check = check_values[check]

    with open('colors.csv', 'r') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                if color == row[to_check]:
                    return row[1], row[2]
                    
    csvFile.close()



# get an input filed from the form called 'name'
# and assign it's value to a local variable called v_name
color = form.getvalue('color')
color = color.replace(" ", "_").lower()
#declare some global variables 
message = ""
colorName = ""
hexColor = ""

hexchar = ['a', 'b', 'c', 'd', 'e', 'f','0' ,'1', '2', '3', '4', '5', '6', '7', '8', '9']



if color[0] == '#':    
    #check if valid hex
    isNotValid = False
    for i in color[1:]:
        if i not in hexchar:
            isNotValid = True      
    if len(color) > 7 or len(color) < 2 or isNotValid:
        message = "Please enter valid hex"
    else:
        #check if color is in database and save name in colorName, otherwise save None
        try: 
            colorName, hexColor = checkColor(color, 'hexNum')
            message = colorName + ", is a color and actually even has name, you know your hex quite well"  
        except:
            hexColor = color
            message = """This color has no name yet, would you like to name it? 
            <form action="./color_confirmation.py" method="post">
                <p>
                    <label for="color_hex">Color: </label>
                    <input type="text" id="color_hex" name="hex_color" readonly="readonly" value= %s required>
                    <label for="Name">Name the color: </label>
                    <input type="text" id="Name" name="new_color" required>
                    <input type="submit" value="Send">
                </p>
            </form>
            """ % hexColor
else:
    #check if the name is in the database and save the name in colorName
    try: 
        colorName, hexColor = checkColor(color, 'colorName')
        message = colorName + ", yeah this color actually exists"
    except:
        message = "This color does not exists. You should go back to kindergarden and learn some colors"

#can set default color if there is no color found
if not hexColor:
    hexColor = "grey"



# send an html response.
print("""
<html>
<body>
<p>
%s
</p>
"""  % message)
print("""
<div style="background-color: %s; width: 50px; height: 50px"></div>
</body>
</html>
""" % hexColor)
