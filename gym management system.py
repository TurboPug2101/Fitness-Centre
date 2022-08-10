import mysql.connector
db=mysql.connector.connect(host='localhost',user='root',password='root@123')
mycursor=db.cursor()
mycursor.execute('create database if not exists diy')
db=mysql.connector.connect(host='localhost',user='root',password='root@123',database= 'diy')
mycursor=db.cursor()
mycursor.execute("create table if not exists diydata(Mcode int(5) primary key,Mname varchar(20),Madd varchar(20),Mindate varchar(5),Moutdate varchar(5),diy_no varchar(5), Room_rent varchar(10),Food_bill varchar(10) default '00',Laudry_bill varchar(10) default '00',Game_bill varchar(10) default '00',SubTotal_bill varchar(10),Add_charges varchar(10) default '1800',GrandTotal_bill varchar(10))") 
mycursor.execute("create table if not exists Member(Mcode int(5),Mid_type varchar  (20),Mid_no varchar(15) primary key , Mname varchar(15), Mcontact_no varchar(15),Madd varchar(20),Mindate varchar(5), Moutdate varchar(5), MNationality varchar(10))") 

db.commit()
def speciality():

     print("\nDESCRIPTION:")
     print("-------------------------------------------------------------------------------------------------------------------------------------------------")
     print('DIY Fitness Has Been The Authority In Fitness Since 1965. It Is A Place For Serious Fitness. Opened Long Before The Modern Day Health Club Existed, DIY Fitness Featured Homemade Equipment And A Dedication To Getting Results')
     print('From The First Cetre In Mumbai, DIY Has Become The Largest Co-Ed Fitness Chain In India .Today, DIY Fitness Has Expanded Its Fitness Profile To Offer All Of The Latest Equipment And Services, Including Group Exercise, Personal Training, Cardiovascular Equipment, Spinning And Yoga, While Maintaining Its Core Weight Lifting Tradition')
     print("-------------------------------------------------------------------------------------------------------------------------------------------------")
     print("PROGRAMS:")
     print("Cardiovascular Training")
     print('Strength and Circuit Training') 
     print("Free Weight Training")
     print('Massage And Steam')
     print("-------------------------------------------------------------------------------------------------------------------------------------------------")
     print("BOOKING:")
     print("Group Training/Personal Training/Offsite And Onsite Programs")
     print("-------------------------------------------------------------------------------------------------------------------------------------------------")



import random
def inputdata():
     r=0
     l=0
     p=0
     s=0
     db=mysql.connector.connect(host='localhost',user='root',password='root@123',database='diy')
     mycursor=db.cursor()
     print("-------------------------------------------------------------------------------------------------------------------------------------------------")
     Mcode=int(input("\nEnter Member Code:"))
     Mname=input("Enter Member Name:")
     Madd=input("Enter Member Address:")
     Mindate=input("Enter Member Membership Date:")
     Moutdate=input("Enter Membership Expiry Date:")
     Mid_type=input("Enter your Identity card name:")
     Mid_no=input("Enter your Identity number:")
     Mcontact_no=input("Enter you Contact number:")
     MNationality=input("Enter your nationality:")
     print("-------------------------------------------------------------------------------------------------------------------------------------------------")
     print("\n")
     
     print ("We have the following programs for you:-")
     print ("1. Long Term Membership----->Rs 6000 PN\-")
     print ("2. Personal Training Program ---->Rs 5000 PN\-")
     print ("3. Quick Result Program ------>Rs 4000 PN\-")
     print ("4. Group Program------->Rs 3000 PN\-")
     print ("5. Weight Loss Program------->RS 2000 PN\-")
     print ("6. Next")

     while (1):
          x=int(input("\nEnter you choice:"))
          if (x==1):
               n=int(input("How Many months would you like to get a Membership for:"))
               print ("You have opted long term Membership")
               s=s+6000*n
               diy_no= random.randint(1,501)
               print("Your DIY ID is:",diy_no)
          elif (x==2):
               n=int(input("How Many months would you like to get a Membership for:"))
               print ("You have opted Personal Training Program")
               s=s+5000*n
               diy_no= random.randint(501,1001)
               print("Your DIY ID is:",diy_no)
          elif (x==3):
               n=int(input("How Many months would you like to get a Membership for:"))
               print ("You have opted Quick Result Program")
               s=s+4000*n
               diy_no= random.randint(1001,1501)
               print("Your DIY ID is:",diy_no)
          elif (x==4):
               n=int(input("How Many months would you like to get a Membership for:"))
               print ("You have opted Group Program")
               s=s+3000*n
               diy_no= random.randint(1501,2001)
               print("Your DIY ID is:",diy_no)
          elif (x==5):
               n=int(input("How Many months would you like to get a Membership for:"))
               print ("You have opted Weight Loss Program")
               s=s+5000*n
               diy_no= random.randint(2001,2501)
               print("Your DIY ID is:",diy_no)
          elif (x==6) :
               break
          else:
               print ("Please Select A Program")
     print ("\nYour Total is",s,'RS')
     

     print("\n")
     print("-------------------------------------------------------------------------------------------------------------------------------------------------")
     print("*****RESTAURANT MENU*****")
     print("1.Water----->Rs20\n2.Tea----->Rs10\n3.Breakfast combo--->Rs90\n4.Lunch---->  Rs110\n5.Dinner--->Rs150\n6.Next")
     while (1):
          c=int(input("\nEnter your choice:"))
          if (c==1):
               d=int(input("Enter the quantity:"))
               r=r+20*d
          elif (c==2):
               d=int(input("Enter the quantity:"))
               r=r+10*d
          elif (c==3):
               d=int(input("Enter the quantity:"))
               r=r+90*d
          elif (c==4):
               d=int(input("Enter the quantity:"))
               r=r+110*d
          elif (c==5):
               d=int(input("Enter the quantity:"))
               r=r+150*d
          elif (c==6):
               break
          else:
               print("Invalid option")
     print ("\nTotal food Cost=Rs ",r)
     print("-------------------------------------------------------------------------------------------------------------------------------------------------")
     print ("\n")
     print ("******BUY GYM EQUIPMENTS*******")
     print ("1.Dumbbells(10kg)----->Rs1000\n2.Dumbbells(20)kg----->Rs1200\n3.Gym Ball--->Rs800\n4.Push Up Bar---->Rs2500\n5.Exercise Wheels--->Rs1500\n6.Next")

     while (1):
          e=int(input("\nEnter your choice:"))
          if (e==1):
               f=int(input("Enter the quantity:"))
               l=l+1000*f
          elif (e==2):
               f=int(input("Enter the quantity:"))
               l=l+1200*f
          elif (e==3):
               f=int(input("Enter the quantity:"))
               l=l+800*f
          elif (e==4):
               f=int(input("Enter the quantity:"))
               l=l+2500*f
          elif (e==5):
               f=int(input("Enter the quantity:"))
               l=l+1500*f
          elif (e==6):
               break
          else:
               print ("Invalid option")
     print ("\nTotal Shopping Cost=Rs",l)
     print("-------------------------------------------------------------------------------------------------------------------------------------------------")

     print ("\n")
     print ("******SPA FACILITIES*****")
     print ("1.Head Massage----->Rs450\n2.Full Body Massage----->Rs1500\n3.Foot Massage--->Rs500\n4.Sauna---->Rs1500\n5.Jacuzzi--->Rs1000==6\n6.Next")
     while (1):
          g=int(input("\nEnter your choice:"))
          if (g==1):
               h=int(input("No. of hours:"))
               p=p+450*h
          elif (g==2):
               h=int(input("No. of hours:"))
               p=p+1500*h
          elif (g==3):
               h=int(input("No. of hours:"))
               p=p+500*h
          elif (g==4):
               h=int(input("No. of hours:"))
               p=p+1500*h
          elif (g==5):
               h=int(input("No. of hours:"))
               p=p+1000*h
          elif (g==6):
               break
          else:
               print ("Invalid option")
     print ("\nTotal SPA Bill=Rs",p)
     print("-------------------------------------------------------------------------------------------------------------------------------------------------")


     Add_charges=1800
     Membership_bill=int(s)
     SPA_bill=int(p)
     Food_bill=int(r)
     Shop_bill=int(l)
     SubTotal_bill=int(s)+int(r)+int(l)+int(p)
     GrandTotal_bill=SubTotal_bill+Add_charges
     print("\nYou have to pay Rs",GrandTotal_bill)
     rec=("insert into diydata values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
     cotm=("insert into Member values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
     data1=(Mcode,Mid_type,Mid_no,Mname,Mcontact_no,Madd,Mindate,Moutdate,MNationality)
     data2=(Mcode,Mname,Madd,Mindate,Moutdate,diy_no,Membership_bill,Food_bill,Shop_bill,SPA_bill,SubTotal_bill,Add_charges,GrandTotal_bill)
     mycursor.execute(cotm,data1)
     mycursor.execute(rec,data2)
     db.commit()
     mycursor.close()
     print("\nRecord Inserted.......")
     db.close()

def display():
     print("\n")
     print("-------------------------------------------------------------------------------------------------------------------------------------------------")
     print("1.Display all records")
     print("2.Display through membership number")
     d=input("\nEnter your choice:")
     if (d=='1'):
          db=mysql.connector.connect(host='localhost',user='root',password='root@123',database= 'diy')
          mycursor=db.cursor()
          qry=("select h.Mcode,h.Mname,h.Madd,h.Mindate,h.Moutdate,h.diy_no,c.MNationality, c.Mcontact_no,c.Mid_type,c.Mid_no from diydata h, Member c where h.Mcode=c.Mcode")
          mycursor.execute(qry)
          for(Mcode,Mname,Madd,Mindate,Moutdate,diy_no,MNationality, Mcontact_no,Mid_type,Mid_no) in mycursor:
               print ("\n")
               print ("_____________________________________________________________________________________________________")
               print ("MEMBER DETAILS ARE AS FOLLOWS:")
               print ("Member code:",Mcode)
               print ("Member name:",Mname)
               print ("Member Id type:",Mid_type)
               print ("Member Id Number:",Mid_no)
               print ("Member address:",Madd)
               print ("Member Nationality:",MNationality)
               print ("Check in date:",Mindate)
               print ("Check out date",Moutdate)
               print ("Membership number:",diy_no)
               print ("Member Contact number:",Mcontact_no)
               print ("_____________________________________________________________________________________________________")
          mycursor.close()
          print("\nThese are all the records")
          db.close()
     elif (d=='2'):
          db=mysql.connector.connect(host='localhost',user='root',password='root@123',database='diy')
          mycursor=db.cursor()
          diy_no=input("\nEnter Membership number:")
          qry=("select h.Mcode,h.Mname,h.Madd,h.Mindate,h.Moutdate,h.diy_no,c.MNationality,c.Mcontact_no,c.Mid_type,c.Mid_no from diydata h, Member c where h.Mcode=c.Mcode and h.diy_no=%s")
          rec_code=(diy_no,)
          mycursor.execute(qry,rec_code)
          rec_count=0
          for(Mcode,Mname,Madd,Mindate,Moutdate,diy_no,MNationality,Mcontact_no,Mid_type,Mid_no) in mycursor:
               rec_count+=1
               print ('\nRECORD FOUND......')
               print ("Here are the member details:-")
               print ("Member code:",Mcode)
               print ("Member name:",Mname)
               print ("Member Id type:",Mid_type)
               print ("Member Id Number:",Mid_no)
               print ("Member address:",Madd)
               print ("Member Nationality:",MNationality)
               print ("Check in date:",Mindate)
               print ("Check out date",Moutdate)
               print ("Membership number:",diy_no)
               print ("Member Contact number:",Mcontact_no)
          if (rec_count==0):
               print("\nRecord not found!!")
               db.commit()
               mycursor.close()
               db.close()
     else :
          print("Invalid Input!!")
     print("-------------------------------------------------------------------------------------------------------------------------------------------------")

def search():
     db=mysql.connector.connect(host='localhost',user='root',password='root@123',database='diy')
     mycursor=db.cursor()
     print("-------------------------------------------------------------------------------------------------------------------------------------------------")
     Mcode=input("\nEnter Member Code to be Searched in DIY Fitness Centre:")
     qry=("select * from diydata where Mcode=%s")
     rec_srch=(Mcode,)
     mycursor.execute(qry,rec_srch)
     rec_count=0
     for(Mcode,Mname,Madd,Mindate,Moutdate,diy_no,Membership_bill,Food_bill,Shop_bill,SPA_bill,SubTotal_bill,Add_charges,GrandTotal_bill) in mycursor:
          rec_count+=1
          print ('\nRECORD FOUND')
          print ("MEMBER DETAILS ARE AS FOLLOWS:")
          print ("Member code:",Mcode)
          print ("Member name:",Mname)
          print ("Member address:",Madd)
          print ("Check in date:",Mindate)
          print ("Check out date",Moutdate)
          print ("Room number:",diy_no)
          print ("Membership Bill is:",Membership_bill)
          print ("Food bill is:",Food_bill)
          print ("Shop Bill is:",Shop_bill)
          print ("SPA bill is:",SPA_bill)
          print ("Sub total bill is:",SubTotal_bill)
          print ("Additional Service Charges is:",Add_charges)
          print ("Grand Total bill is:",GrandTotal_bill)
     if (rec_count==0):
          print("\nRecord not found!!")
          db.commit()
          mycursor.close()
          db.close()
     print("-------------------------------------------------------------------------------------------------------------------------------------------------")

def delete():
     db=mysql.connector.connect(host='localhost',user='root',password='root@123',database='diy')
     mycursor=db.cursor()
     print("-------------------------------------------------------------------------------------------------------------------------------------------------")
     Mcode=input("\nEnter Member Code to be delete from DIY Fitness:")
     qry=("delete from diydata where Mcode=%s")
     qry1=("delete from Member where Mcode=%s")
     del_rec=(Mcode,)
     mycursor.execute(qry,del_rec)
     mycursor.execute(qry1,del_rec)
     rec_count=0
     for Mcode in mycursor:
          rec_count+=1
          print("\nRecord Deleted......")
     if rec_count==0:
          print("\nRecord not Found!!")
          print("Enter valid data")
     db.commit()
     mycursor.close()
     db.close()
     print("-------------------------------------------------------------------------------------------------------------------------------------------------")
     
def update():
     print("-------------------------------------------------------------------------------------------------------------------------------------------------")
     print("\nWhich Data Should be Updated......")
     print("1.Member Name:")
     print("2.Member Address")
     print("3.Member out Date")
     print("4.Member Room Number")
     print("5.Member Contact number")
     c=int(input("\nSelect your Choice:"))
     if (c==1):
          db=mysql.connector.connect(host='localhost',user='root',password='root@123',database='diy')
          mycursor=db.cursor()
          Mcode=input('\nEnter Code of Member to be Updated:')
          qry=('select * from diydata where Mcode=%s')
          Mname=input("Enter Member Name:")
          q=('update diydata set Mname=%s where Mcode=%s')
          data=(Mname,Mcode)
          mycursor.execute(q,data)
          q=('update Member set Mname=%s where Mcode=%s')
          data=(Mname,Mcode)
          mycursor.execute(q,data)
          print('\nRecord Updated.....')
          db.commit()
          mycursor.close()
          db.close()
     elif (c==2):
          db=mysql.connector.connect(host='localhost',user='root',password='root@123',database='diy')
          mycursor=db.cursor()
          Mcode=int(input('\nEnter Code of Member to be Updated:'))
          qry=('select * from diydata where Mcode=%s')
          Madd=input("Enter Member Adrress:")
          q=('update diydata set Madd=%s where Mcode=%s')
          data=(Madd,Mcode)
          mycursor.execute(q,data)
          q=('update Member set Madd=%s where Mcode=%s')
          data=(Madd,Mcode)
          mycursor.execute(q,data)
          print('\nRecord Updated.....')
          db.commit()
          mycursor.close()
          db.close()
     elif (c==3):
          db=mysql.connector.connect(host='localhost',user='root',password='root@123',database='diy')
          mycursor=db.cursor()
          Mcode=int(input('\nEnter Code of Member to be Updated:'))
          qry=('select * from diydata where Mcode=%s')
          Mindate=input("Enter Member in Date:")
          q=('update diydata set Mindate=%s where Mcode=%s')
          data=(Mindate,Mcode)
          mycursor.execute(q,data)
          q=('update Member set Mindate=%s where Mcode=%s')
          data=(Mindate,Mcode)
          mycursor.execute(q,data)
          print('\nRecord Updated.....')
          db.commit()
          mycursor.close()
          db.close()
     elif (c==4):
          db=mysql.connector.connect(host='localhost',user='root',password='root@123',database='diy')
          mycursor=db.cursor()
          Mcode=int(input('\nEnter Code of Member to be Updated:'))
          qry=('select * from diydata where Mcode=%s')
          Moutdate=input("Enter Member out Date:")
          q=('update diydata set Moutdate=%s where Mcode=%s')
          data=(Moutdate,Mcode)
          mycursor.execute(q,data)
          q=('update Member set Moutdate=%s where Mcode=%s')
          data=(Moutdate,Mcode)
          mycursor.execute(q,data)
          print('\nRecord Updated.....')
          db.commit()
          mycursor.close()
          db.close()
     elif (c==5):
          db=mysql.connector.connect(host='localhost',user='root',password='root@123',database='diy')
          mycursor=db.cursor()
          Mcode=int(input('\nEnter Code of Member to be Updated:'))
          qry=('select * from Member where Mcode=%s')
          Mcontact_no=input("Enter Member Contact number:")
          q=('update Member set Mcontact_no=%s where Mcode=%s')
          data=(Mcontact_no,Mcode)
          mycursor.execute(q,data)
          print('\nRecord Updated.....')
          db.commit()
          mycursor.close()
          db.close()
     else :
          print("Invalid Input!!")
     print("-------------------------------------------------------------------------------------------------------------------------------------------------")

def diyfarecal():
     while True :
          print("\n")
          print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
          print("1.Booking for Membership")
          print("2.Show Member Record")
          print("3.Search Member Record")
          print("4.Delete Member Record")
          print("5.Update Member Record")
          print("6.Return to Main Menu")
          print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
          b=(input("\nEnter your choice:"))
          if (b=='1'):
               z='y'
               while (z=='y'):
                    inputdata()
                    z=input("\nDo you want to continue..(y/n):")
               if (z=='n'):
                    return diyfarecal()
               else :
                    print("Invalid Input!!")
                    z=input("\nDo you want to continue..(y/n):")
          elif (b=='2'):
               z='y'
               while z=='y':
                    display()
                    z=input("\nDo you want to continue..(y/n):")
               if (z=='n'):
                    return diyfarecal()
               else :
                    print("Invalid Input!!")
                    z=input("\nDo you want to continue..(y/n):")
          elif (b=='3'):
               z='y'
               while (z=='y'):
                    search()
                    z=input("\nDo you want to continue..(y/n):")
               if (z=='n'):
                    return diyfarecal()
               else :
                    print("Invalid Input!!")
                    z=input("\nDo you want to continue..(y/n):")
          elif (b=='4'):
               z='y'
               while (z=='y'):
                    delete()
                    z=input("\nDo you want to continue..(y/n):")
               if (z=='n'):
                    return diyfarecal()
               else :
                    print("Invalid Input!!")
                    z=input("\nDo you want to continue..(y/n):")
          elif (b=='5'):
               z='y'
               while (z=='y'):
                    update()
                    z=input("\nDo you want to continue..(y/n):")
               if (z=='n'):
                    return diyfarecal()
               else :
                    print("Invalid Input!!")
                    z=input("\nDo you want to continue..(y/n):")
          elif (b=='6'):
               break
          else:
               print("Invalid Input......")
print("\n\t\t       ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
print("֎֎֎֎֎֎֎֎ ֎֎░░░░░░░░░ WELCOME TO DIY FITNESS ░░░░░░░░░֎֎ ֎֎֎֎֎֎֎֎")
print("\t\t       ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
print("---------------------------------------------------------------DIY FITNESS!-----------------------------------------------------------------")

while True:
     print("\n")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MENU~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     print("1.Speciality of your Fitness Centre")
     print("2.Member Management")
     print("3.EXIT")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     b=input("\nEnter your choice:")
     if (b=='1'):
          speciality()
     elif (b=='2'):
          diyfarecal()
     elif (b=='3'):
          quit()
     else:
          print("Wrong Choice")
