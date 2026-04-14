with open("sample.txt", "w") as f:
    f.write("hello world\n")
    f.write("\n")
    f.write("this is a test\n")
    f.write("hello again\n")
    f.write("\n")
    f.write("final line\n")

with open("scores.txt", "w") as f:
    f.write("Alice,85\n")
    f.write("Bob,90\n")
    f.write("Charlie,78\n")
    f.write("Diana,95\n")


print("--- TASK 1 ---")

def count_lines(filename):
    with open(filename, "r") as f:
        total = 0
        for line in f:
            if line.strip():
                total += 1
    return total

print(count_lines("sample.txt"))


print("--- TASK 2 ---")

def find_keyword_lines(filename, keyword):
    with open(filename, "r") as f:
        result = []
        line_number = 1
        for line in f:
            if keyword in line:
                result.append(line_number)
            line_number += 1
    return result

print(find_keyword_lines("sample.txt", "hello"))


print("--- TASK 3 ---")

def convert_to_uppercase(filename):
    with open(filename, "r") as f:
        content = f.read()
    with open("output.txt", "w") as f:
        f.write(content.upper())

convert_to_uppercase("sample.txt")


print("--- TASK 4 ---")

def average_score(filename):
    with open(filename, "r") as f:
        total = 0
        count = 0
        for line in f:
            if line.strip():
                parts = line.strip().split(",")
                score = int(parts[1])
                total += score
                count += 1
    if count == 0:
        return 0
    return total / count

print(average_score("scores.txt"))