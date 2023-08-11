import time
import pywhatkit
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="********",
  database="whatapp"
)
t=time.localtime()
h=t.tm_hour
m=t.tm_min
print(h,":",m)
print("Login press '#'")
print("Sig Up press *'")
ab=input("Press the option= ")
if('#'==ab):
    mycursors=mydb.cursor()
    mycursor=mydb.cursor()
    mycursorz=mydb.cursor()
    pin=int(input("Enter your pin:"))
    querys="SELECT number FROM customers2 WHERE pin=%s"
    paramss=(pin,)
    mycursors.execute(querys,paramss)
    resultss=mycursors.fetchall()
    a1=resultss
    a1=a1[0]
    a1=a1[0]
    query="SELECT balance FROM customers2 WHERE pin=%s"
    params=(pin,)
    mycursor.execute(query,params)
    results=mycursor.fetchall()
    balance=results
    queryss="SELECT pin FROM customers2 WHERE pin=%s"
    paramsss=(pin,)
    mycursorz.execute(queryss,paramsss)
    resultss=mycursorz.fetchall()
    i=True
    if(balance==None):
        balance=[0]
    else:
        a=balance
    if(resultss==[]):
        number=0000
    else:
        a=resultss[0]
        number=a[0]
    if(pin==number):
        while i==True:
            print("1-Balance")
            print("2-deposit")
            print("3-withdrawl")
            print("4-Exit")
            choice=int(input("Enter your choice = "))
            if(1==choice):
                c=balance[0]
                query="SELECT name FROM customers2 WHERE pin=%s"
                params=(pin,)
                mycursor.execute(query,params)
                results=mycursor.fetchall()
                results=results[0]
                results=results[0]
                query="SELECT number FROM customers2 WHERE pin=%s"
                params=(pin,)
                mycursorz.execute(query,params)
                resultss=mycursorz.fetchall()
                resultss=resultss[0]
                resultss=resultss[0]
                print("Name: " + results)
                print("Phone Number: "+ resultss)
                print("Your current Balance")
                print(c[0] + .0)
                print("--------------------------------------------------")
            elif(2==choice):
                deposit=int(input("Enter your Deposit Amount :"))
                de=[(deposit,)]
                bal=balance
                c=de+bal
                c=c[0]+c[1]
                bal=sum(c)
                balance=[(bal,)]
                pywhatkit.sendwhatmsg('+91'+str(a1) ,'Your deposit amount '+str(deposit)+'.0 \n Thank you for visit',h,m+1)
                print("Your Deposit Amount is "+ str(deposit)+'.0')
                print("--------------------------------------------------")
            elif(3==choice):
                withdrawl = int(input("Enter your withdrawl Amount :"))
                de=[(withdrawl,)]
                bal=balance
                c=de+bal
                c=c[0]+c[1]
                bal=c[1]-c[0]
                balance=[(bal,)]
                pywhatkit.sendwhatmsg('+91'+str(a1) ,'Your withdrawl amount '+str(withdrawl)+'.0 \n Thank you for visit',h,m+1)
                print("Your Deposit Amount is "+ str(withdrawl)+'.0')
                print("--------------------------------------------------")
            elif(4==choice):
                print("Thanking You")
                print("--------------------------------------------------")
                i=False
                mycursors=mydb.cursor()
                sql="UPDATE customers2 SET balance=%s WHERE pin=%s"
                a=balance[0]
                val=(a[0],pin)
                mycursors.execute(sql,val)
                mycursors.close()
                c=balance[0]
                c=balance[0]
                pywhatkit.sendwhatmsg('+91'+str(a1) ,'Your current amount '+str(a[0])+'.0 \n Thank you for visit',h,m+1)
                mydb.commit()
                mydb.close()
                print(mycursors.rowcount,"record(s) affected")
            else:
                print("you have entered wrong input")
    else:
        print("invalid pin")
elif('*'==ab):
    mycursorssss=mydb.cursor()
    mycursory = mydb.cursor()
    e=500
    a=input("Enter Your Name: ")
    b=int(input("Enter Your Number: "))
    c=int(input("Enter Your pin: "))
    d=int(input("Ener Re-Type pin: "))
    query="SELECT pin FROM customers2 WHERE pin=%s"
    params=(c,)
    mycursory.execute(query,params)
    resultss=mycursory.fetchall()
    if(resultss==[]):
        r=0000
    else:
        r=resultss[0]
        r=r[0]
    
    if(r!=c):
        if(c==d):
            sql = "INSERT INTO customers2 (name,number,pin,balance) VALUES (%s, %s,%s,%s)"
            val = (a,b,c,e)
            mycursory.execute(sql, val)
            mydb.commit()
            print("1 record inserted, ID:", mycursory.lastrowid)
            querys="SELECT number FROM customers2 WHERE pin=%s"
            paramss=(c,)
            mycursorssss.execute(querys,paramss)
            resultsss=mycursorssss.fetchall()
            a1=resultsss
            a1=a1[0]
            a1=a1[0]
            pywhatkit.sendwhatmsg('+91'+str(a1) ,'Successfully created pin  \n Thank you for visit',h,m+2)
        else:
            print("don't match re-type pin")
    else:
        print("Already using this pin. 'please change your pin'")
    

else:
    print("Something wrong please check your option")
