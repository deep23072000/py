'''count = 0
a = 0
while a%2==0:
    a = int(input("Enter number"))
    print("out ")
    count+=1
else:
    print("out of loop")'''

#Write a while loop that counts down from 10 to 1 and print each number
#when the loop finishes print  "liftoff"
'''count = 10
while count > 0:
    print(count,end=",")
    count-=1
else:
    print("lift off")'''

#WAP that keeps asking the user to input a number and add all the isers together and stop
#asing when the user enters 0 . finally print the total sum
'''collect = 0;
while True:
    print("Enter 0 for sum of all number you entered") 
    inp = int(input("Enter number = "))
    if inp > 0 or inp < 0:
        collect += inp
    elif inp == 0:
        print("Enter number is equal to 0 you are out of loop")
        print(f"sum of all entered number is {collect}")
        break
    else:
        print("invalid input")'''

#use a while loop to print all even number between 1 and 20

'''count = 1
while count < 20:
    if count%2==0:
        print(count,end="\n")
    count+=1'''


#Guess the number

'''num = 7
while True:
    uinput = int(input("Guess the number = "))
    if uinput == num:
        print("correct")
        break
    else:
        print("You guessed wrong please try again")'''

#reverse digits

'''d = int(input("Enter integer that you want to reverse"))
f = str(d)
#print(f)
#print(type(f))

count = len(f)
store = ""
while (count-1) >= 0:
    store = store + f[count-1]
    count -= 1
print(store)'''

#factorial calculator

'''n = 6
count = 1
d = 1
while count <= n:
    d *= count
    count += 1

print(d)'''

#collatz sequence
'''while True:
    uinput = int(input("enter positive integer"))
    if uinput%2 == 0:
        uinput /= 2
        print(uinput)
        if uinput == 1:
            break
    elif uinput%2 == 1:
        uinput*=3
        uinput +=1
        print(uinput)
        if uinput == 1:
            break'''

#prime number

'''n = int(input("Enter number"))
count = 1
v = 0
while count < n/2:
    if n % count == 0 and n%1==0:
        v += 1    
    count += 1

if v == 1:
    print(" It is prime number")
elif n == 2:
    print(" It is prime number")    
else:
    print("not a prime number")'''

#simulate a bank account
'''initial_balance = 1000

while True:
    print("Enter 1 for deposit balance")
    print("Enter 2 for withdraw balance")
    print("Enter 3 for check balance")
    c = int(input("Enter = "))
    if c == 1:
        print("Enter amount you want to deposit")
        a = int(input("Enter = "))
        initial_balance += a
    elif c == 2:
        print("Enter amount you want to withdraw")
        a = int(input("Enter = "))
        initial_balance -= a
    elif c == 3:
        print(f"your balance is {initial_balance}")
        print("================================================================")'''

#find the GCD ( greatest common divisor ) of two numbers using a while loop

'''a = 45
b = 18
count = 1
gcda = 0
gcdb = 0



while count < b/2+1:
    if a % count == 0:
        gcda = count
    if b % count == 0:
        gcdb = count
    count+=1
print(gcda)
print(gcdb)'''

import math

a = 18
b = 36
c = math.gcd(a,b)
print(c)
    
        




        
        
    
    
    



    
    
    


        
    
    
    


        
        
        
        



    
