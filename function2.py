#convert C to F
def C_to_F(Celsius):
    Fahrenheit = (9.0/5.0) * Celsius + 32
    return Fahrenheit #return statement causes your function to exit and hand back a value

C = int(input("Enter temperature in Celsius: "))
print(C_to_F(C))

def F_to_C(Fahrenheit):
    Celsius = float((Fahrenheit-32) * (5.0/9.0))
    print(Celsius)
F = float(input("Enter temperature in Fahrenheit: "))
F_to_C(F)

def area_circle(radius):
    pi = 3.14
    return pi * radius ** 2
r = float(input("Enter radius of circle: "))
print(area_circle(r))

def volume_cylinder(radius, height): #multiple inputs parameters
    pi = 3.14159
    return pi * radius ** 2 *height
rC = float(input("Enter radius of cylinder: "))
hC = float(input("Enter height of cylinder: "))
print(volume_cylinder(rC,hC)) #2 inputs since 2 parameters
