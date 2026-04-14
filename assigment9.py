print("---TASK 1---")

def count_lines(filename):
    total = 0
    with open(filename, "r") as file:
        for line in file:
            if line.strip() != "":
                total += 1
    return total

result = count_lines("sample.txt")
print("Total non-blank lines:", result)



print("---TASK 2---")

def find_keyword(filename, keyword):
    line_numbers = []
    with open(filename, "r") as file:
        for line_number, line in enumerate(file, start=1):
            if keyword.lower() in line.lower():
                line_numbers.append(line_number)
    return line_numbers

result = find_keyword("sample.txt", "python")
print("Keyword found on lines:", result)



print("---TASK 3---")

def convert_to_uppercase(filename):
    with open(filename, "r") as file:
        content = file.read()

    uppercase_content = content.upper()

    with open("output.txt", "w") as output_file:
        output_file.write(uppercase_content)

    print("Uppercase content saved to output.txt")

convert_to_uppercase("sample.txt")


print("---TASK 4---")

def calculate_average(filename):
    total_score = 0
    student_count = 0

    with open(filename, "r") as file:
        for line in file:
            if line.strip() != "":
                parts = line.strip().split(",")
                name = parts[0]
                score = int(parts[1])
                total_score += score
                student_count += 1

    average = total_score / student_count
    print("Average score:", average)
    return average

calculate_average("scores.txt")

    







    


