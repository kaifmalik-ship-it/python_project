stuednt_grade={}

def add_student(name,grade):

   stuednt_grade[name]=grade
   print(f"Added{name} with a {grade}")




def update_student(name,grade):

   if name in stuednt_grade:
      stuednt_grade[name]=grade
      print(f"{name} with a marks update {grade}")

   else:
      print(f"{name} is not found!")

def delete_student(name):
   if name in stuednt_grade:
      del stuednt_grade[name]
      print(f"{name} has been sucessfully deleted" )

   else:
      print(f"{name} is not found!")

def display_all_student():
   if stuednt_grade:
      for name ,grade in stuednt_grade.items():
         print(f"{name}:{grade}")

   else:
         print("No stuednt found/added")
      
def main():
   while True:
      print("\n student Grade Manadement  systym")
      print("1.Add student")            
      print("2.udate student")
      print("3.Delete student")
      print("4.View student")
      print("5.Exit student")
                
      choice=int(input("Enter your choice"))
      if choice ==1:
         name=input("Enter your name")
         grade=int(input("Enter your grade"))

         add_student(name ,grade)

      elif choice ==2:
         name=input("Enter your name")
         grade= int(input("Enter a Grade"))
         update_student(name,grade)

      elif choice==3:
         name=input("Enter a  your name")
         delete_student(name)


      elif choice==4:
         display_all_student()

      elif choice==5:
         print("closing the  programe...")
         break
      else:
         print("Invalid choice")
main()         