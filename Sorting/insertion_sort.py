a=[23,78,45,8,32,56]
for i in range(len(a)):
        for j in range(i,len(a)):
            if a[i]>a[j]:
                 a[i],a[j]=a[j],a[i]
        print(a)