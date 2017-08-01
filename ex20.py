from sys import argv

script, input_file = argv

def print_all(f): # define a function that read the content of the txt
    print(f.read())

def rewind(f):
    f.seek(0) # move back to the beginning of the file

def print_a_line(line_count, f):
    print(line_count, f.readline()) # funtion that prints one line at a time

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file) # return the file at the beginning

print("Let's print three lines:")

current_line = 1 # mark No.1
print_a_line(current_line, current_file) # print the first line

current_line += 1 # 
print_a_line(current_line, current_file) # print the second line

current_line += 1
print_a_line(current_line, current_file) # print the third line
