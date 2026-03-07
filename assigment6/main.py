print("---TASK 1---")
numbers = []
while True:
    user_input = input("Enter a number (press Enter to quit): ")
    if user_input == "":
        break
    number = float(user_input)
    numbers.append(number)
numbers.sort(reverse=True)
print("Five greatest numbers:")
print(numbers[:5])

print("---TASK 2---")
seasons = ("winter", "spring", "summer", "autumn")
month = int(input("Enter month number (1-12): "))
if month == 12 or month == 1 or month == 2:
    season = seasons[0]
elif month == 3 or month == 4 or month == 5:
    season = seasons[1]
elif month == 6 or month == 7 or month == 8:
    season = seasons[2]
else:
    season = seasons[3]
print("Season:", season)

print("---TASK 3---")
names = set()
while True:
    name = input("Enter a name (press Enter to quit): ")
    if name == "":
        break
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)
print("All names:")
for n in names:
    print(n)

print("---TASK 4---")
def word_frequency(text):
    words = text.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
text = input("Enter a text: ")
result = word_frequency(text)
print(result)

print("---TASK 5---")
def remove_odd(numbers):
    new_list = []
    for n in numbers:
        if n % 2 == 0:
            new_list.append(n)
    return new_list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = remove_odd(numbers)
print("Original list:", numbers)
print("Without odd numbers:", result)