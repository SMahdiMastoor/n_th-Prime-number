from prime import prime_num
x=int(input("enter number :"))
list_of_number=[]
a=2
while (len(list_of_number)<= x):
    if prime_num(a)==True :
        list_of_number.append(a)
    a=a+1

print(list_of_number)
print(list_of_number.pop())