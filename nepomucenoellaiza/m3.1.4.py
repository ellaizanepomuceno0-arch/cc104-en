var = 1
print(var)
var = 0
print(var)

white_sheep = 5
black_sheep = 2 * white_sheep
print(black_sheep == 2 * white_sheep)

var = 0  
print(var == 0)

var = 1
print(var == 0)

var = 0  # Assigning 0 to var
print(var != 0)
 
var = 1  # Assigning 1 to var
print(var != 0)

black_sheep > white_sheep  

centigrade_outside = 10.0
print(centigrade_outside >= 0.0)  # Greater than or equal to

current_velocity_mph = 80
print(current_velocity_mph < 85)  # Less than
print(current_velocity_mph <= 85)  # Less than or equal to

stock_count = 0

grade = 75

if grade <= 74:
    print("Failed")
else:
    print("Passed")
