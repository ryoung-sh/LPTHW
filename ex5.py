my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
height_in_centimeter = my_height * 2.54 # 1 inch = 2.54 centimeter.
trans_height_in_meters = my_height * 0.0254 # 1 inch = 0.0254 meter.
height_in_meters = round(trans_height_in_meters,2) # round to two decimal.

my_weight = 180 # lbs
weight_in_kg = my_weight * 0.454 # 1 lbs = 0.454 kg
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d centimeter tall." % height_in_centimeter
print "He's %.2f meters tall." % height_in_meters # not round to two decimal? Because %d only output integer.
print "He's %d pounds heavy." % my_weight
print "He's %d kilograms heavy." % weight_in_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
