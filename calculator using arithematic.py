num1= int(input("enter first number"))
num2= int(input("enter secod number"))

print("1: adition")
print("2: sub")
print("3: muli")
print("4: divi")


choice= input("enter your choice :(1/2/3/4)")

if choice == "1" :
  print (num1+num2)
elif choice == "2" :
  print (num1-num2)
elif choice == "3" :
  print (num1*num2)
elif choice == "4" :
  print (num1/num2)
else :
  print ("invalid statement")