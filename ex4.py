cars = 100
space_in_a_car = 4 #if here is 4.0 then...
drivers = 30
passengers = 30
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car #here will be 120.0
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in this car.")

# study Drills

#1. the error was due to that carpool_capacity is mistakenly spelled to car_pool_capacity and which was not specified earlier.

# 2. if space_in_a_car = 4 instead of 4.0, then anything associated with space_in_a_car will be integer rather than floating number.
