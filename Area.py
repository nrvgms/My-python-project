# write a program of a area and circumference of a rectangle

#write a program to calculate circumference- 3.14 or 22/7 r= radius formula = 2 pie r

l = float(input("length: "))
b = float(input("height: "))
A= l*b
C = 2*(l+b)
print("Area = {}".format(A)) # using format function
print("Circumference = {}".format(C)) # using format function

print("========= OR======")

print("Area = %0.4f" %A) # using % format to printing the 4 decimal points
print("Circumference = %0.4f" %C) # using format function


print("=" * 10 + " OR " + "=" * 10)

print("Area = {}".format(round(A,3)))
print("Circumference= {}". format(round(C,2)))


##### AREA OF RECTANGLE in ONE LINE:
print("Area = {}".format(float(input("length: "))*float(input("height: "))))




