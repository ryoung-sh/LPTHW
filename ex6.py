x = "There are %d types of people." % 10 # there are 10 types of people.
binary = "binary" # define variable as "binary"
do_not = "don't" # define variable as "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # print binary and don't into the sentence.

print x
print y

print "I said: %r." % x # print raw data of x
print "I also said: '%s'." % y # print string of y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious # here it prints raw data of hilarious in joke_evaluation

w = "This is the left side of ..."
e = "a string with a right side."

print w + e
