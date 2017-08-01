from sys import argv

script, user_name = argv
<<<<<<< HEAD
prompt = '> um...'
||||||| merged common ancestors
prompt = '> '
=======
prompt = '> um... '
>>>>>>> origin/master

print("Hi %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = input(prompt)

print("Where do you live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

<<<<<<< HEAD
print("What do you want for breakfest?")
breakfest = input(prompt)

||||||| merged common ancestors
=======
print("What do you want for breakfast?")
breakfast = input(prompt)
>>>>>>> origin/master
print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
<<<<<<< HEAD
And you would like %r for your breakfest. Good choice!""" % (likes, lives, computer, breakfest))
||||||| merged common ancestors
""" % (likes, lives, computer))
=======
And you want %r for breakfast. Good for you!
""" % (likes, lives, computer, breakfast))
>>>>>>> origin/master
