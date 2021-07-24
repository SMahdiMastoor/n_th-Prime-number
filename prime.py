import os
os.system('cls')
#----------------------------------------------------------------
def prime_num(num):


 n=2
 if num<=1 : print('number should be bigger than one')
 prime=None
 while (n<=num) :
    M=num%n
    n=n+1
    if (M == 0 and num != 2) :
         #print('number is not prime')
         prime=False
         break 
       
    elif (M != 0 and  n==num or num==2 ):
            #print("number is prime ")
            prime=True
            break
 return prime
   
