#FOR loop prints Hello! 10 times
for hello in range (10):
    print ("hello!")
#FOR loop creats a variable
for i in range (15):
    i=i+1
    print ('Hello! i is set to ' + str(i))
#Counts to 1 million
for count in range (0,10):
    print (count)
#sum all of the numbers up to 1 million
sum = 0
for million in range (10000000):
    sum += million

print (sum)

#input 2 integers and use the power operator to print the square of every other number between those two numbers
integer1= input ("Please enter one number")
integer1= int(integer1)                 
integer2= input ("Please enter another number")
integer2= int(integer2)
for square in range (integer1, integer2,2):
                 print (square **2)
#input an integer and then tell the user if it is a prime number
integerty= input ("please enter an integer number:")
integerty= int(integerty)
if integerty==2:
    print("prime number")
elif integerty %2==0:
    print("even number")
else:
    print("prime number")
