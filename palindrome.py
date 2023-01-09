x = (input("enter a string: "))

w = ""
for i in x:
	w = i + w

if (x == w):
	print(x, "is a palindrome string")
else:
	print(x, "is not a palindrome string")
