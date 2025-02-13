#Print first 10 natural numbers using while loop
count=1
while count<=10:
  print(count)
  count=count+1


#Pattern printing
for i in range(1,6):
  for j in range(1,i+1):
    print(j,end="")
  print()


#Calculate sum of all numbers from 1 to a given number
#n*n+1/2
num=int(input("Enter a number: "))
total=0

for i in range(1,num+1):
  total+=i
print(total)# Print multiplication table of a given number

num=int(input())
for i in range(1,11):
  print(num*i)



#Display numbers from a list using a loop with conditions
num=[12,75,150,180,145,525,50]

for i in num:
  if i%5==0:
    print(i)
  elif i>150:
    continue
  elif i>500:
    break


#Count the total number of digits in a number
num=int(input("Enter a number : "))
count=0
while num>0:
  num//=10
  count+=1
print(count)


#Print the pattern
num=5

for i in range(num,0,-1):
  for j in range(i,0,-1):
    print(j,end="")
  print()



#Print list in reverse order using a loop
list1=[10,20,30,40,50]

for i in list1[::-1]:
  print(i)



#Display numbers from -10 to -1 using for loop
for i in range(-10,-1+1):
  print(i)



#Display a message “Done” after the successful execution of the for loop
for i in range(0,5):
  print(i)
print("Done")



#Print all prime numbers within a range
start=25
end=50
num=0
for i in range(start,end):
  if i>1:
    for j in range(2,int(i**0.5)+1):
      if i%j==0:
        break
    else:
      print(i)



#Display Fibonacci series up to 10 terms
n1=0
n2=1
print("Fibonacci Sequence")
print(n1)
print(n2)
for i in range(2,10):
  next=n1+n2
  print(next)
  n1,n2=n2,next




# Find the factorial of a given number
num=int(input("Number to be factorial : "))
fact=1
for i in range(1,num+1):
  fact*=i
print(f"Factorial of {num} in {fact}")



#Reverse a integer number
num=12345
for i in str(num)[::-1]:
  print(i,end="")



#Print elements from a given list present at odd index positions
my_list=[10,20,30,40,50,60,70,80,90,100]

for i in my_list[1::2]:
  print(i)



#Calculate the cube of all numbers from 1 to a given number
num=int(input())

for i in range(1,num+1):
  print("Current Number is :",i,"and the cube is",i*i*i)




#Find the sum of the series up to n terms
n=int(input())
series=0

for i in range(1,n+1):
  term=int("2"*i)
  series+=term
print(series)



# Print the following pattern

for i in range(1,6):
  print("*"*i)

for j in range(1,5):
  print("*"*(5-j))




