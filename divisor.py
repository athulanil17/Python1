divisorlist=[]
n=int(input("Enter a number: "))
print("The divisor of number",n,"is: " )
for i in range(1,n+1):
    if(n%i==0):
        divisorlist.append(i)
        
print(divisorlist)
