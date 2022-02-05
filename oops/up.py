import sqlite3
penny=[]
GG=[]
class ATM():
    def connection(self):
        a = sqlite3.connect('ATM00.db')
        return a

    def createTab(self,a):
        a.execute('''CREATE TABLE ATM00(ACCOUNTNO INTEGER  PRIMARY KEY , NAME TEXT,PASSWORD INT,AMOUNT INT)''')

    def Insert(self,a):
        n = int(input("Enter How Many People :"))
        for i in range(n):
            AA1 = input(" Enter account no.")
            AA2 = input("Enter Your Name :")
            AA3  = int(input("Create Your 4 Digit Password Here :"))
            AA4 = int(input("Enter Amount :"))
            a.execute("INSERT INTO ATM00(ACCOUNTNO,NAME,PASSWORD,AMOUNT) VALUES(?,?,?,?)",(AA1,AA2,AA3,AA4))
            a.commit()
    
    def amount(self,a):
        self.a=a
        return self.a
    def deposit(self,b):
        self.b=b
        self.a=self.a+self.b
        return self.a
    def withdraw(self,c):
        self.c=c
        if self.c>self.a:
            print("insuffician balance")
        else:
            print("dn")
        self.a=self.a-self.c
        return self.a
    def finalamount(self):
        return self.a

    def retrieve(self,a):
        cursor = a.cursor()
        Acc = int(input("Enter Your Account no. :"))
        User = int(input("Enter Your PIN :"))
        penny.append(Acc)
        B1 = "SELECT * FROM ATM00 WHERE ACCOUNTNO =?"
        A1 = "SELECT * FROM ATM00 WHERE PASSWORD=?"
        if A1 and B1 :
            cursor.execute(A1,(User,))
            cursor.execute(B1,(Acc,))
            rows =  cursor.fetchall() 
        for row in rows:
            continue  
        if row[1]==Acc and row[3]==User:
            print("**\tWelcome To Online ATM :)")

        x=ATM()
        n=row[3]
        print(x.amount(n))
        while True:
            print("\n1 --> deposit")
            print("2 --> withdraw")
            z=int(input("Please enter 1 or 2 :"))
            if z==1:
                nn=int(input("Enter Amount To Deposit :"))
                print(x.deposit(nn))
            elif z==2:
                nnn=int(input("Enter Amount To Withdraw :"))
                print("Remaining Balance :",x.withdraw(nnn))
            else:
                print("Final Balance in your Account :",x.finalamount())
                GG.append(x.finalamount())
                break
    def update(self,a):
        cursor=a.cursor()
        hq=penny[0]
        fc=GG[0]
        zef="UPDATE ATM00 SET AMOUNT=? WHERE ACCOUNTNO=?"
        cursor.execute(zef,(fc,hq))
z=ATM()
x=z.connection()
#y=z.createTab(x)
#y=z.Insert(x)
y=z.retrieve(x)
r=z.update(x)
x.commit()
x.close()