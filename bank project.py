import random
import os
import matplotlib.pyplot as plt
import numpy as np

tlist=[]

def createac():
    fp=open('bank.txt','a')
    name=input('enter your name')
    age=input('enter your age')
    bal=str(input('enter balance'))
    accno=str(random.randint(0,20))
    print('your acc no is',accno)
    pin=str(input('give 4 digit pin'))
    data=accno+':'+pin+':'+name+':'+age+':'+bal+'\n'
    tdata = [accno,[]]
    tlist.append(tdata)
    fp.write(data)
    fp.close()
    
def openacc():
    fp=open('bank.txt','r')
    acn1=str(input('Enter accno:'))
    pin1=str(input('Enter pin :'))
    s=0
    for i in fp.readlines():
             x=i.split(':')
             if acn1==x[0] and pin1==x[1]:
                 print(i)
                 print('Acc no    |Name     |Age    |Balance  ')
                 print(x[0],'      ',x[2],'      ',x[3],'  ',x[4])
                 s=1
                 n=int(input('choose : \n1) Withdraw \n2) Deposit \n3)Transfer'))
                 m=int(input('enter amount'))
                 if n==1:
                     fp.close()
                     withdraw(acn1,m)
                 elif n==2:
                    deposit(acn1,m)
                 elif n==3:
                     transfer(acn1,m)
    if s==0:
                 print('wrong acc no or pin')
                 
def withdraw(acn1,m):
    fp=open("bank.txt","r")
    tmp=open("temp.txt","w")
    for i in tlist:
        if i[0]==acn1:
            a=len[i[1]]
            t=str(a+1)+")"+"-"+str(m)
            i[1].append()
    for i in fp.readlines():
        row=i.split(":")
        bn=row[0]
        if bn==acn1:
            name=row[2]
            age=row[3]
            bal=str(int(row[4])-m)
            pin=row[1]
            data=acn1+':'+pin+':'+name+':'+age+':'+bal+'\n'
            tmp.write(data)
        else:
            tmp.write(i)
    fp.close()
    tmp.close()
    os.remove("bank.txt")
    os.rename("temp.txt","bank.txt")
    
def deposit(acn1,m):
    fp=open("bank.txt","r")
    tmp=open("temp.txt","w")
    for i in tlist:
        if i[0]==acn1:
            a=len[i[1]]
            t=str(a+1)+")"+"+"+str(m)
            i[1].append()
    for i in fp.readlines():
        row=i.split(":")
        bn=row[0]
        if bn==acn1:
            name=row[2]
            age=row[3]
            bal=str(int(row[4])+m)
            pin=row[1]
            data=acn1+':'+pin+':'+name+':'+age+':'+bal+'\n'
            tmp.write(data)
            tmp1.write()
        else:
            tmp.write(i)
    fp.close()
    tmp.close()
    os.remove("bank.txt")
    os.rename("temp.txt","bank.txt")
    
def transfer(acn1,m):
    fp=open("bank.txt","r")
    tmp=open("temp.txt","w")
    acn2=input('enter acc no to be transfered')
    withdraw(acn1,m)
    deposit(acn2,m)
    '''
    for i in fp.readlines():
        row=i.split(":")
        bn=row[0]
        if bn==acn1:
            name=row[2]
            age=row[3]
            bal=str(int(row[4])-m)
            pin=row[1]
            data=acn1+':'+pin+':'+name+':'+age+':'+bal+'\n'
            tmp.write(data)
        else:
            tmp.write(i)    
    fp.close()
    tmp.close()
    tmp=open("temp.txt","r")
    tmp1 = open("temp1.txt","w")
    for i in fp.readlines():
            row1=i.split(':')
            bn1=row1[0]
            if bn1==acn2:
                name=row1[2]
                age=row1[3]
                bal=str(int(row1[4])+m)
                pin=row1[1]
                data=acn2+':'+pin+':'+name+':'+age+':'+bal+'\n'
                tmp1.write(data)
            else:
                tmp1.write(i)
    tmp.close()
    tmp1.close()
    os.remove("bank.txt")
    os.remove("temp.txt")
    os.rename("temp1.txt","bank.txt")
    '''

def feedback():
    print('Rate services:1)Excellent')
    print("              2)Average")
    print('              3)Poor')
    a1=int(input('Enter choice ;'))
    print('Rate infrastructure :1)Excellent')
    print("                     2)Average")
    print('                     3)Poor')
    a2=int(input('Enter choice ;'))
    x=np.arrange(1,3)
    y=[a1,a2]
    plt.plot(x,y)
    
    
'''
ch=0
while(ch!=6):
   print("===========")
   print("Bank")
   print("===========")
   print("1. Open account")
   print("2. show acc details")
   print("3. Search Record")
   print("4. Modify Record")
   print("5. Delete Record")
   print("6. Exit")
   print("Enter your ch..1-6")
   ch=int(input("\n your ch...."))
   if ch==1:
       createac()
   elif ch==2:
       openacc()
       
   elif ch==3:
       search()
   elif ch==4:
       upd()
   elif ch==5:
       delt()
'''
