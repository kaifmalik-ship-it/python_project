import json
import random
import string
from pathlib import Path


class bank:
   database="data.json"
   data=[]
   try:
        if Path (database).exists():
         with open (database) as fs:
              data= json.loads(fs.read())
        else:
             print("No such file exsist")
   except Exception as err:
      print(f"an exception occured as {err}")          


   @staticmethod
   def __update():
     with open(bank.database,"w") as fs:
      fs.write(json.dumps(bank.data))
           
   @staticmethod

   def __account_genrater():
       alpha= random.choices(string.ascii_letters,k=3)
       num= random.choices(string.digits,k=3)
       spchar= random.choices("!@#^&*",k=1)
       id=alpha+num+spchar
       random.shuffle(id)
       return "".join(id)




   
   def create_account(self):
        data= {
           "name" : input("Enter your Name :"),
            "age":  int(input("Enter your Age :")),
            "email":input("Enter your email"),
            "pin":int(input("Enter your 4 Number pin")),
            "account": bank.__account_genrater(),
            "balance" :0
        }
        if data["age"] < 18 or len(str(data["pin"])) !=4:
             print("sorry you cannot create account ")  

        else:
            print("account has been created succesfully")
            for i in data:
                print(f"{i}:{data[i]}")
            print("please not down your account number ")
            bank.data.append(data)
            bank.__update()


   def deposite_money(self):
    acc_no = input("Enter your Account Number: ")
    pin = int(input("Enter your pin: "))

    userdata = [
        i for i in bank.data
        if i["account"] == acc_no and i["pin"] == pin
    ]

    if not userdata:
        print("Sorry, no data found")

    else:
        amount = int(input("How much you want to deposit: "))

        if amount <= 0:
            print("You have to deposit an amount above 0")

        else:
            userdata[0]["balance"] += amount
            bank.__update()
            print("Amount deposited successfully")              

   def withdraw_money(self):
    acc_no = input("Enter your Account Number: ")
    pin = int(input("Enter your pin: "))

    userdata = [
        i for i in bank.data
        if i["account"] == acc_no and i["pin"] == pin
    ]

    if not userdata:
        print("Sorry, no data found")

    else:
        amount = int(input("How much you want to withdraw: "))

        if amount <= 0:
         print("Please enter an amount above 0")

        elif userdata[0]['balance'] < amount:
            print("sorry you dont have that much money")

        else:
            userdata[0]["balance"] -= amount
            bank.__update()
            print("Amount withdraw successfully")
   def show_details(self):
        acc_no = input("Enter your Account Number: ")
        pin = int(input("Enter your pin: "))
       
        userdata = [
                i for i in bank.data
                if i["account"] == acc_no and i["pin"] == pin
            ]  

        if not userdata:
         print("Sorry, no data found")
        else:
          print("your information are \n\n")
          for i in userdata[0]:
           print(f"{i}:{userdata[0][i]}")
        
   def update_details(self):
     acc_no = input("Enter your Account Number: ")
     pin = int(input("Enter your pin: "))

     userdata = [
                    i for i in bank.data
                    if i["account"] == acc_no and i["pin"] == pin
                ] 

     if not userdata:
         print("no such user data found") 
     else:
          print("you cannot change the age ,account number,balance")
          print("fill the details for change or leave it empty if no change")    

          newdata = {
          "name":input("please Enter your name"),
           "email":input("Enter your gmail"),

            "pin":input("Enter your pin or press skip button")             
            }

          if newdata["name"] == "":
           newdata["name"] = userdata[0]["name"]

          if newdata["email"] == "":
           newdata["email"] = userdata[0]["email"]

          if newdata["pin"] == "":
           newdata["pin"] = userdata[0]["pin"]

          newdata['age']=userdata[0]['age']    

          newdata["account"]=userdata[0]['account']
          newdata['balance']=userdata[0]['balance']


          if type(newdata["pin"]) == str:
           newdata["pin"] = int(newdata["pin"])
          for i in newdata:
           if newdata[i] != userdata[0][i]:
             userdata[0][i] = newdata[i]
          bank.__update()
          print("details update succesfully")


   def delete(self):
        
     acc_no = input("Enter your Account Number: ")
     pin = int(input("Enter your pin: "))
     
     userdata = [
                         i for i in bank.data
                         if i["account"] == acc_no and i["pin"] == pin
                     ] 
     
     if not userdata:
         print("sorry no such data exsist") 

     else:
         check= input(" press y if you want to delete data or press n") 
         if check == 'n' or check == 'N':
          print("bypasssed")

         elif check == 'y' or check == 'Y':
          index = bank.data.index(userdata[0])
          bank.data.pop(index)
          print("account deleted succesfully")
          bank.__update() 
user= bank()
print("press 1: create Account")
print("press 2 :Deposite the money in the Account")
print("press 3 :withdraw money from the Account")
print("press 4 :details  Account")
print("press 5 :update details")
print("press 6 :delete Account")

 
check=int(input("tell your Response "))
if check == 1:
    user.create_account()

if check == 2:
    user.deposite_money()

if check==3:
    user.withdraw_money()    
if check==4:
    user.show_details()


if check == 5:
    user.update_details()

if check==6:
   user.delete()    