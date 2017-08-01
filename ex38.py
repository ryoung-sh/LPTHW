ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ') # split the ten_things into list.
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10: # add items until 10 stuff
    next_one = more_stuff.pop() # pops off the last item of more_stuff
    print("Adding: ", next_one)
    stuff.append(next_one)
    print("There are %d items now." % len(stuff))

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1]) # print the 2nd item
print(stuff[-1]) # print the last item
print(stuff.pop()) # takes out the last item of stuff and print it
print(" ".join(stuff)) # turn the list into one string with space in between
print("#".join(stuff[3:5])) # turn the 4th to 5th item into string with # in between
