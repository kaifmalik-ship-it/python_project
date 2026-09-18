menu ={

    "pizza" :900,
    "Burger": 500,
    "pasta": 800,
    "fries": 200,
    "coffee":120
}


print("***welcome our Resturent***")

print(" pizza:900\n","Burger:500\n","pasta:800 \n","fries:200\n","coffee:120\n")
order_item=0
item=input("Enter a item please :")
if item in menu:
  order_item+= menu[item]
  print(f"your item :{item} : has been added in your order")
else:

  print("sorry it is not Available Right Now")

another_order=input("Do you want Add another order(yes/Not)")
if another_order== "yes":
  item_2 =input("Enter a 2nd order ")
  if item_2 in menu:
   order_item+=menu[item_2]

  else:
    print (f"sorry this {item_2} is not avaialable")
print(f"Total amount is{order_item}")
  