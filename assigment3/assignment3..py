print("---TASK 1---")
num = 1
while num <1000:
    if num % 3 == 0:
        print(num)
    num = num + 1

print("---TASK 2---")
inches = float(input("enter your inches to convert to centimeter(enter negative number to quit): "))
while not inches < 0:
    centimeters = inches * 2.54
    print(f"your centimeters is: {centimeters}")
    inches = float(input("enter your inches to convert to centimeter(enter negative number to quit): "))
else:
    print("thank you")

print("---TAKS 3---")
largest = None
smallest = None
user_input= input("please enter numbers(empty to quit): ")
while user_input != "":
    num = float(user_input)
    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num
    user_input = input("please enter numbers(empty to quit): ")
print(f"the largest number is {largest}")
print(f"the smallest number is {smallest}")
if user_input == "":
    print("thank you")

print("---TAKS 4---")
import random
secret = random.randint(1,10)
while True:
    guess = int(input("guess a number between 1 to 10: "))
    if guess <1 or guess > 10:
        print("please guess only a number between 1 to 10")
    elif guess < secret:
        print("too low")
    elif guess > secret:
        print("too high")
    else:
        print("correct")
        break

print("---TAKS 5---")
correct_username = "python"
correct_password = "rules"
attempts = 0
while attempts < 5:
    username = input("enter your username: ")
    password = input("enter your password: ")
    if username == correct_username and password == correct_password:
        print("welcome")
        break
    else:
        attempts = attempts + 1
if attempts == 5:
    print("access denied")

print("---TASK 6---")
text = input('Please enter a text: ')
def middle_character(text):
    length = len(text)
    mid = length//2

    if length%2 == 0:
        return text[mid-1:mid+1]
    else:
        return text[mid]
print('The middle character(s) of your text: ',middle_character(text))
print()


print("---TASK 7---")
def acronym(phrase):
    result = ""
    words = phrase.split()
    for word in words:
        result += word[0].upper()
    return result
phrase = input("Enter a phrase: ")
print(acronym(phrase))



