print("---TASK 1---")
def valid_code(code):
    if len(code) != 6:
        return False
    first_part = code[:3]
    second_part = code[3:6]
    if not first_part.isalpha() or not first_part.isupper():
        return False
    if not second_part.isdigit():
        return False
    return True
print(valid_code("AVD123"))
print(valid_code("abc123"))
print(valid_code("Ade3"))
print(valid_code("ADF432"))


print("---TASK 2---")
def valid_format(characters):
    if len(characters) != 7:
        return False
    first_letter = characters[0]
    last_letter = characters[1:7]
    if first_letter != "#" :
        return False
    for i in last_letter:
        if not (i.isdigit() or i in "ABCDEF" or i in "abcdef"):
            return False
    return True
print(valid_format("ABCDEFGH"))
print(valid_format("#123kja"))
print(valid_format("#AAAAAA"))
print(valid_format("#ABC123"))


print("---TASK 3---")
def skibidi(text):
    total = 0
    words = text.split()
    for word in words:
        if word.isdigit():
            total += int(word)
    return total

print(skibidi("hello world"))
print(skibidi("today is march 2 2026 , and the degree is 33"))
print(skibidi("i've learnt this assignment for 5 or 6 hours"))


print("---TASK 4---")
def skibidi(text):
    words = text.split()
    new_words = []
    for word in words:
        if (len(word) == 10 and word.isdigit()) or word.startswith("+84"):
            new_words.append("[RETACTED]")
        else:
            new_words.append(word)
    return " ".join(new_words)

print(skibidi("Hello World"))
print(skibidi("hello, my phone number is +84123456789"))
print(skibidi("phone number == 0981246783"))
