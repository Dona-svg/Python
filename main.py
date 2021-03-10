class student:
   def __init__(self,name,mark,branch):
     self.name= name
     self.mark= mark
     self.branch= branch

   def display(self):
         print ( "name:" , self.name, ",mark:" ,self.mark, " branch:" , self.branch)
   def __del__(self):
       print("deleted")

stud1 = student("Dona",20,"mca")
stud2=student("sona",20,"mca")


stud1.display()
stud2.display()

del stud1
