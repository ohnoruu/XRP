"""
x1 = float(input("Enter first x coord: "))
y1 = float(input("Enter first y coord: "))
x2 = float(input("Enter second x coord: "))
y2 = float(input("Enter second y coord: "))

def calculateSlope(x1, y1, x2, y2):
    rise = (y2-y1)
    run = (x2-x1)
    slope = rise/run
    print(slope)
    
calculateSlope(x1, y1, x2, y2)
"""

x = input("Enter x coord: ")
y = input("Enter y coord")
point1 = {'x':x, 'y':y}
x = input("Enter x coord: ")
y = input("Enter y coord")
point2 = {'x':x,'y':y}

def calculateSlope():
    rise = point2.get('y')/point1.get('y')
    run = point2.get('x')/point1.get('x')
    return(rise/run)
print(calculateSlope())
