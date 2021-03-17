class Rectangle:
    def __init__(self,length,breadth):
        self.length =  length
        self.breadth = breadth
    def area(self):
        return self.breadth * self.length
    def perimeter(self):
        return 2 * (self.breadth + self.length)
print("Rectangle 1")
a = int(input("enter the length:"))
b = int(input("enter the breadth:"))
obj=Rectangle(a,b)

print("Area 1 = ", obj.area())
print("perimeter = ", obj.perimeter())


print("Rectangle 2")
a = int(input("enter the length:"))
b = int(input("enter the breadth:"))
obj=Rectangle(a,b)

print("Area 2=",obj.area())
print("perimeter =",obj.perimeter())

if obj.area() == obj.area():
    print ("the 2 Rectangle have same area")
else:
    print("not equal")

