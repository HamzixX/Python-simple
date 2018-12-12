def prime():
 s=0
 a =int(input("give a number \n"))
 for i in range (1,a) :
     if (a % 2) == 0 :
         s=s+1
 if s > 2 :
     print("not a prime number \n")
 else:
     print("prime number \n")
def power() :
    p=1
    a=int(input("give a number \n"))
    x=int(input("give power \n"))
    for i in range(1,x):
        p=p*a
    print("the result is",p)
prime()
power()

