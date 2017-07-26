name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_in_centimeter = height * 2.54 # 1 inch = 2.54 centimeter.
trans_height_in_meters = height * 0.0254 # 1 inch = 0.0254 meter.
height_in_meters = round(trans_height_in_meters,2) # round to two decimal.

weight = 180 # lbs
weight_in_kg = weight * 0.454 # 1 lbs = 0.454 kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print("Let's talk about %s." % name)
print("He's %d inches tall." % height)
print("He's %d centimeter tall." % height_in_centimeter)
print("He's %.2f meters tall." % height_in_meters) # not round to two decimal? Because %d only output integer.
print("He's %d pounds heavy." % weight)
print("He's %d kilograms heavy." % weight_in_kg)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (eyes, hair))
print("His teeth are usually %s depending on the coffee." % teeth)

#this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight))
