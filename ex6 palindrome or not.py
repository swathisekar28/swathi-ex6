n=int(input("enter the numbet:"))
org=n
sum=0
while(n>0):
    a=n%10
    sum=sum*10+a
    n=n//10
if(sum==org):
    print("the given is palindrome")
else:
    print("the given is nota palindrome")
