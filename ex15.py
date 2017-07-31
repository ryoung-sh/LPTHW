from sys import argv # get the argv module from sys

script, filename = argv # put the file from the user into the argv

txt = open(filename) # open the text file from the user

print(("Here is your file %r:") % filename) # print the filename
print(txt.read()) # read the content of the text and print them out

# if using only above, I will need to type in the file name at the beginning
# this way is not convenient if there are multiple text that is uncertain to
# be prompted.

print("Type the filename again:") # prompt the user for filename
file_again = input("> ")

txt_again = open(file_again) # open the file prompted from the user

print(txt_again.read()) # read the text file prompted and print them out

# using input to prompt file from the user is more convenient in getting
# the file from the user particularly if there are multiple files to be choosed from.
