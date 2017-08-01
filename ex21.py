def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b

def subtract(a, b):
    print("SUBTRACTING %d - %d" % (a, b))
    return a - b

def multiply(a , b):
    print("Multiplying %d * %d" % (a, b))
    return a * b

def divide(a, b):
    print("Dividing %d / %d" % (a, b))
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %r, Height: %r, Weight: %r, IQ: %r" % (age, height, weight, iq))

# A puzzle for the extra credit, type it in anyway
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq,2))))
testwhat = (30 + 5) + (78 - 4) - (100 / 2)/2 * (90 * 2) # this is to test if I'm understanding the formula correctly.
print(testwhat)

print("That becomes: ", what, "Can you do it by hand?")
