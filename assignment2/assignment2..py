def skibidi():
    print("---TASK 1---")
    x = float(input(" Hello fisher!, please enter the length of zander in centimeters:"))
    if x < 42:
         print(" please release the fish back into the lake, the limit size must be 42 centimeters or longer")
    elif x >= 42:
        print(" the fish meet the requirement, have a nice day !")
skibidi()

def cabin():
    print("---TASK 2---")
    x = input(" please enter the cabin class: ")
    if x == "LUX" or x == "LUXURY":
        print("upper-deck cabin with a balcony.")
    elif x == "A" or x == "a":
        print("above the car deck, equipped with a window.")
    elif x == "B" or x == "b":
        print("windowless cabin above the car deck.")
    elif x == "C" or x == "c":
        print("windowless cabin below the car deck.")
    else:
        print("Invalid cabin class.")
cabin()
    
def bio_sex():
    print("---TASK 3---")
    x = input("your biological sex:")
    y = float(input("your hemoglobin value(g/l):"))
    if x.upper() == "FEMALE" and y < 117:
        print("your hemoglobin value is low")
    elif x.upper() == "FEMALE" and 117 <= y <= 155:
        print("your hemoglobin value is normal")
    elif  x.upper() == "FEMALE" and y > 155:
        print("your hemoglobin value is high")
    if x.upper() == "MALE" and y < 134:
        print("your hemoglobin value is low")
    elif x.upper() == "MALE" and 134 <= y <= 167:
        print("your hemoglobin value is normal")
    elif  x.upper() == "MALE" and y > 167:
        print("your hemoglobin value is high")
bio_sex()

def leap_year():
    print("---TASK 4---")
    year = int(input("please enter a year: "))
    if year % 4 == 0 and year % 100 != 0:
        print("this a leap year")
    elif year % 100 == 0 and year % 400 == 0:
        print("this is leap year")
    else:
        print("not a leap year")
leap_year()

print("---TASK 5---")
import math

def pizza_unit_price(diameter_cm, price):
    radius_m = (diameter_cm / 2) / 100
    area = math.pi * radius_m ** 2
    return price / area


def piza():
    d1 = float(input("Enter diameter of pizza 1 (cm): "))
    p1 = float(input("Enter price of pizza 1 (USD): "))

    d2 = float(input("Enter diameter of pizza 2 (cm): "))
    p2 = float(input("Enter price of pizza 2 (USD): "))

    unit1 = pizza_unit_price(d1, p1)
    unit2 = pizza_unit_price(d2, p2)

    if unit1 < unit2:
        print("Pizza 1 provides better value for money.")
    elif unit2 < unit1:
        print("Pizza 2 provides better value for money.")
    else:
        print("Both pizzas have the same value for money.")

piza()

