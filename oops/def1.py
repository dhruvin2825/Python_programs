def one():
    a=int(input("enter number:"))
    q=two(a)
    return q

def two(a):
    i=1
    n=[]
    while i<=a:
        name=input("enter name")
        sub=int(input("enter subject:"))
        w=subject(sub)
        n.append(name)
        i=i+1
    return n,w
def subject(sub):
    return sub

z=one()
print(z)