#convert C to F
def C_to_F(Celsius):
    Fahrenheit = (9.0/5.0) * Celsius + 32
    return Fahrenheit #return statement causes your function to exit and hand back a value


print(C_to_F(20))

def F_to_C(Fahrenheit):
    Celsius = float((Fahrenheit-32) * (5.0/9.0))
    return Celsius

print(F_to_C(80))

def area_circle(radius):
    pi = 3.14
    return pi * radius ** 2

print(area_circle(2))

def volume_cylinder(radius, height): #multiple inputs parameters
    pi = 3.14159
    return pi * radius ** 2 *height

print(volume_cylinder(2,5)) #2 inputs since 2 parameters
