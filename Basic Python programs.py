#FACTORS
n=12
sum=0
for i in range(1,12):
    if n%i==0:
        sum=sum+i
print("sum is:",sum)
if sum>n:
    print("True")
else:
    print("False")

#DIVISIBLE BY
n=12354
temp=n
sum=0
while n>0:
    r=n%10
    sum=sum+r
    n=n//10

if temp%sum==0:
    print("divisible")
else:
    print("not divisible")

#ARMSTRONG NUMBER   
n=153
sum=0
cnt=0
a=n
temp=n
while a>0:
    a=a//10
    cnt=cnt+1
while n>0:
    r=n%10
    s=r**cnt
    sum=sum+s
    n=n//10
print(sum)
if temp==sum:
    print("yes")
else:
    print("no")
    
#PALINDROME
n=12321
rev=0
org=n
while n>0:
   r=n%10
   rev=rev*10+r
   n=n//10
print(rev)
if org==rev:
    print("palindrome")
else:
    print("not a palindrome")

#FACTORIAL
n=int(input("enter a number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

#FIBNOCCI
a=0
b=1
print(a)
print(b)
for i in range(3,11):
    c=a+b
    print(c)
    a=b
    b=c

