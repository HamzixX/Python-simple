def prime():
 a =int(input("gine a number \n"))
 s=0
 for i in range (1,a) :
     if (a % 2) == 0 :
         s=s+1
 if s > 2 :
     print("not a prime number")
 else:
     print("prime number")
prime()

