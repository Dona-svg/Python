class publisher:
    def __init__(self):
        print("parent class")
class book(publisher):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        print("the title of the book is ",self.title)
        print("the author of the book is".self.author)
class python(book):
    def __init__(self,price,pages):
        self.price=price
        self.pages=pages
    def display(self):
        print("the price of the book is",self.price)
        print("total pages of the book is",self.pages)
c=book("learing python","khaled hussain")
c.display()
c=python(550,852)
c.display()