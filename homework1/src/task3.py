# Task3.py

#Check to see if a number is a certain value either positive,negative,or 0
def checkNumberSign(num):
    if num > 0:
        print(f"{num} is positive")
    elif num < 0:
        print(f"{num} is negative")  
    else:
        print(f"{num} is 0")



#Find first 10 prime numbers
def first_10_prime_nums():
    #List to hold the first 10
    prime_nums = []

    #Start num at 2 since 1 is not Prime
    num = 2

    #While list is not 10 numbers
    while(len(prime_nums) < 10):
        #Set Prime flag to true
        prime = True

        #From 2 to whatever current num is 
        for i in range(2,num):
            #Mod it and if we get a divisble number
            if num % i == 0:
                #Set prime to false and break immeditaley
                prime = False
                break
        #If true add to list   
        if prime:
            prime_nums.append(num)
        
        #Increment num 
        num += 1
    #Print the prime numbers
    for p in prime_nums:
        print(p)



# This will get the sum of all nums 1 to 100
def one_too_onehundred():

    #Set number to 1
    number = 1
    #Set total to 0
    total = 0

    #While number is less or equal than 100
    while(number <= 100):
        #Increment total and number
        total += number
        number += 1

    #Return Total
    return total

    




        

