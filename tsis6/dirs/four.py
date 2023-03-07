filepath = "samplefile.txt"

with open(filepath) as file:
    line_count = 0
    for line in file:
        line_count += 1

print(f"Number of lines in file: {line_count}")
