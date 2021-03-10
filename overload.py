class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length * self.width
    def __lt__(self):
        if (rec1 < rec2):
            print("area of rectangle 1 is less than rectangle 2")
        else:
            print("area of rectangle 2 is greater than rectangle 1")

print("rectangle 1")
a=int(input("enter the length:"))
b=int(input("enter the width:"))
obj=rectangle(a,b)

print("area 1= ",obj.area)

print("rectangle 2")
a=int(input("enter the length:"))
b=int(input("enter the width:"))
obj=rectangle(a,b)

print("area 2=",obj.area)

rec1 = obj.area()
rec2 = obj.area()
obje=rectangle(rec1,rec2)
obje.__lt__()
