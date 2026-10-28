with open("sample.txt", "r") as file:
    lines = file.readlines()

longest_line = ""
line_number = 0
    
for i, line in enumerate(lines, start=1):
    if len(line) > len(longest_line):
        line_number = i
            
    print("longest line:", longest_line.strip())
    print("line  number:", line_number)