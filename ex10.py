tabby_cat = "\tI'm tabbed in." # \t escape tab .
persian_cat = "I'm split\non a line." # \n split a line. Linefeed
backlash_cat = "I'm \\ a \\ cat." # \ ignore the latter backlash

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
# \t tab a line; use ''' equals """, single-quote is faster to type than double-quotes

print tabby_cat
print persian_cat
print backlash_cat
print fat_cat

# while True:
    # for i in ["/","-","|","\\","|"]:
        # print "%s\r" % i,
