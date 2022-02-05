a={'a':'sf','v':[3,4,5,6]}
b={'a':'sf','vk':[3,4,5,6,8]}
a_values=[]
a_keys=[]
b_keys=[]
b_values=[]

a_keys=a.keys()
b_keys=b.keys()

a_values=b.values()
b_values=b.values()

if a_keys==b_keys:
    print(a_keys,b_keys)
    print("Keys are same")
else:
    print(a_keys,b_keys)
    print("keys are not same")

if a_values==b_values:
    print(a_values,b_values)
    print("values are same")
else:
    print(a_values,b_values)
    print("values are not same")