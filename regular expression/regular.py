import re


pattern='^[a-z|A-Z]*[0-9]+@(gmail|yahoo|hotmail)+(.com|.in|.org)$'
pattern_phone=r'(+91)'

s=input("Enter Email:")
z=re.match(pattern,s)

print(z)

if z:
    print("match")
else:
    print("not match")