import math
user_in = input("Enter radius : ")


def calculation(rad):
    circumference = 2.0 * math.pi * float(rad)
    area = math.pi * pow(float(rad), 2)
    print(circumference)
    print(area)


calculation(user_in)
