from operator import index

a=[23,78,45,8,32,56]

for i in range(len(a)):
    j=0
    k=1
    print(a)
    
    while True:
        if a[j]>a[k]:
            a[j],a[k]=a[k],a[j]
        print(a)
        j+=1
        k+=1
        

