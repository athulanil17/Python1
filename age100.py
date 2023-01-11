cyear=int(input("Enter current year:"))
name=input("Enter your Name:" )
age=int(input("Enter your age:" ))
hage=int(cyear+(100-age))
if age>0:
  print("Hi" ,name, "you will be 100 years old in the year", hage)
else:
  print("Invalid age")
