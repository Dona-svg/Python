class Parent:
    parentAttr = 100
    def __init__(self):
        print ("calling parent constructor")

    def parentMethod(self):
        print ("calling parent method")

class Child(Parent):
    def __init__(self):
        print ("calling child constructor")

    def childMethod(self):
        print ("Calling child method")

c = Child()
c.childMethod()
c.parentMethod()


