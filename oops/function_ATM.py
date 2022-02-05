import sqlite3
class ATM():
    def connection():
        a=sqlite3.connect('ATM.db')
        return a

    def create1(a):
        a.execute('''CREATE TABLE BANK(ACCOUNT_NO INTEGER PRIMARY KEY, NAME TEXT,PIN INTEGER,AMOUNT INTEGER)''')
        return a

    def insert(a):
        person=int(input("Enter people="))
        for i in range(person):
            acc_no=int(input("Enter account no:"))
            name_1=input("Enter name:")
            pin_1=int(input("Enter PIN no:"))
            amount_1=int(input("Enter amount:"))
        a.execute("insert into BANK(ACCOUNT_NO,NAME,PIN,AMOUNT) values(?,?,?,?)",(acc_no,name_1,pin_1,amount_1))
        return a
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

    def fetch(a):
        cursor=a.cursor()
        reacc_no=int(input("ReEnter your account no="))
        re_pin=int(input("ReEnter your pin"))
        a.cursor("select * from BANK where ")

obj=connection()
# create1(obj)
insert(obj)
obj.commit()
obj.close()