class Myclass:
    def __init__(self,p,q):
        self.p=p
        self.q=q
    def displays(self):
        return self.p,self.q
o1=Myclass(input("Enter String 1:\n"),int(input("Enter number 1:\n")))
o2=Myclass(input("Enter String 2:\n"),int(input("Enter number 2:\n")))
print(o1.displays())
print(o2.displays())        