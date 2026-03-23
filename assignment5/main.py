print("---TASK 1---")
numbers = []
while True:
    x = input("please enter a number (press enter to quit): ")
    if x == "":
        break
    numbers.append(float(x))
numbers.sort(reverse=True)
print("your five greatest numbers is: ")
for num in numbers[:5]:
    print(num)

print("---TASK 2---")
num = int(input("Enter an integer: "))
if num < 2:
    print("Not a prime number")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")

print("---TASK 3---")
cities = []
for i in range(5):
    city = input("Enter a city: ")
    cities.append(city)
print("Cities:")
for city in cities:
    print(city)

print("---TASK 4---")
def sum_list(numbers):
    return sum(numbers)
nums = [1, 2, 3, 4, 5]
result = sum_list(nums)
print("Sum:", result)

print("---TASK 5---")
def remove_odd(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
nums = [1, 2, 3, 4, 5, 6, 7]
filtered = remove_odd(nums)
print("Original list:", nums)
print("Even numbers only:", filtered)