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
    p=0
    a=int(input("give a number \n"))
    x=int(input("give power \n"))
    print("the result is",a**x)
prime()
power()

