#Define Variables in programming
a=10
b=7

#Print a value from variable
a=9
print(a)

#Concatenation of 3 strings from variable
a="Hello"
b=" Good "
c="day!"
d=a+b+c
print(d)

#Build calculator with 2 variables
#Python Operators - Addition and Subtraction and mul and division and modulus
a=int(input("Enter a value for a:"))
b=int(input("Enter a value for b:"))
add=a+b
sub=a-b
mul=a*b
div=a/b
mod=a%b
print("Addition : ",add)
print("Subtraction : ",sub)
print("Multiplication : ",mul)
print("Division : ",div)
print("Modulo : ",mod)

#"Welcome" - Extract the 4th value from the given string.
a="Welcome"
print(a[4])

#Calculate the length of this word “Python”.
a="Python"
print(len(a))


#“I’m doing great‘ -. Write a python code to convert this to upper case
statement="I’m doing great"
print(statement.upper())

#Check “learn” is exist in the given string - “I’m learning python”
a="I'm learning Python"
print("learn" in a)

#Check “Python” is not present in the given string “i’m learning NodeJs”
a="I’m learning NodeJs"
print("Python" not in a)

#Get the character at position 1 of a string
a="Welcome to library"
print(a[0])

# Remove whitespace from the beginning or at the end of a string
a="  Welcome to library    "
print(a)
print(a.strip())

#Return the length of a string
a="Welcome to library"
print("Length of a string is:",len(a))

# Replace a string with another string (Welcome Raja - Replace Raja with Roja)
greet="Welcome Raja"
print(greet)
new_greet=greet.replace("Raja","Roja")
print(new_greet)

#Split a string into different (‘hello,world’)
a="Hello world"
print(a.split())

#Calculate the multiplication and sum of two numbers
a=int(input("Enter a value for a : "))
b=int(input("Enter a value for b : "))
add=a+b
mul=a*b
if mul<=1000:
  print(mul)
else:
  print(add)

#Print the Sum of a Current Number and a Previous number
for i in range(10):
  print("Current number ",i+1,"  Previous Number ",i," Sum:",(i+1)+i)

#Print the datatype of a data
a=90
b="Afrin"
c=10.5
print(type(a))
print(type(b))
print(type(c))

# Print characters present at an even index number
string="PYnative"

odd=[]
even=[]

for i in range(len(string)):
  if i%2==0:
    even.append(string[i])
print("even : ",even)


# Print characters present at an even index number - using indexing method
string="PYnative"
print("Odd characters :",string[1::2])
print("Even Characters : ",string[::2])

#Remove first n characters from a string & Remove last n characters
string="Alphabet"
print(string[4:])
print(string[:4])

#Check if the first and last numbers of a list are the same
x=[10,20,30,40,10]
if x[0]==x[-1]:
  print("True")
else:
  print("False")

#Display numbers divisible by 5
a=[30,50,66]
for i in a:
  if i%5==0:
    print(i)

# Find the number of occurrences of a substring in a string
x="Afrin is PG Student. Afrin completed UG"
y=x.count("Afrin")
print(y,"times Afrin occurred in the sentence")

#Print the pattern
a=['1','2','3','4','5']
for i in a:
  print(i)

Name=input("Name:")
score=int(input("Score: "))
dept=input("Department: ")
calculated_score=score/10

print("Your name is ",Name)
print("Your score is ",calculated_score)
print("Your department is",dept)

print(10/3)
print(10//3) #Floor division
print(10%3)  #Modulus
print(10**3) #Power

#Assignment operators
x=2
x += 2
print(x)
x -= 2
print(x)
x *= 2
print(x)
x /= 2
print(x)
x //= 2
print(x)
x **= 2
print(x)
x %= 2
print(x)

# Check Palindrome Number
def palindrome(s):
  return s==s[::-1]

s="545"
ans=palindrome(s)

if ans:
  print("Yes, the given number is palindrome number")
else:
  print("No, the given number is not a palindrome")


#Merge two lists using the following condition
a=[10,20,25,30,35]
b=[40,45,60,75,90]
c=[]

for i in a:
  if i%2!=0:
    c.append(i)
for j in b:
  if j%2==0:
    c.append(j)

print(c)

#Get each digit from a number in the reverse order
a=12345
reversed_num=int(str(a)[::-1])
print(reversed_num)


#Calculate income tax
a=int(input("Enter your salary"))
tax=0

if a>=20000:
  tax+=(a-20000)*0.2
  print(tax)
elif a>=10000 and a<20000:
  tax+=(a-10000)*0.1
  print(tax)
elif a<=10000:
  tax+=a*0.0
  print(tax)
else:
  print("Enter a proper value")


#Print multiplication table from 1 to 10
for i in range(1,11):
  print(i,i*2,i*3,i*4,i*5,i*6,i*7,i*8,i*9,i*10)


#Print a downward half-pyramid pattern of stars
for i in range(1,5+1):
  print("*"*i)

#Get an int value of base raises to the power of exponent
def exponent(base,exp):
  res=base**exp
  return res

print(exponent(5,4))