def input1():
    
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    choice=int(input("Enter Choice:"))
    q=processing(a,b,choice)
    return q

def processing(a,b,choice):
    if choice==1:
        total=a+b
        
    elif choice==2:
        total=a-b
        
    elif choice==3:
        total=a*b
        
    elif choice==4:
        total=a/b
        
    s=output1(total)
    return s

def output1(total):
    return total


obj=input1()
print(obj)




