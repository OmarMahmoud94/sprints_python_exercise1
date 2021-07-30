import math
while True:
    first_point = input("Enter first point in form of a,b :  ").split(",")
    Second_point = input("Enter second point in form of a,b : ").split(",")
    res = math.sqrt(pow((int(Second_point[0]) - int(first_point[0])), 2)
                    + pow((int(Second_point[1]) - int(first_point[1])), 2))
    print(res)
