class time:
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second

    def __add__(self, other):
        return self.hour + other.hour , self.minute + other.minute , self.second + other.second
t1 = time(2,10,10)
t2 = time(5,12,20)
t3 = t1+t2
print(t3)