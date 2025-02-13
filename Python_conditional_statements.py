#Write a program that assigns grades to students based on their scores.

mark=int(input("Enter your mark : "))

if mark>=90:
  print("Outstanding")
elif mark>=70 and mark<90:
  print("A")
elif mark>=50 and mark<70:
  print("B")
elif mark>=30 and mark<50:
  print("C")
else:
  print("Sorry! You are failed")



#Write a program that checks if a person is eligible to vote.
age=int(input("Enter your age : "))
if age>=18:
  print("You are eligible for voting")
else:
  print("You are not eligible for voting")


#Write a program that calculates the final price after applying a discount.
amount=int(input("Amount : "))
discount=0
if amount>=10000 and amount<50000:
  disc=amount*0.2
  final_price=amount-disc
  discount+=disc
  print(discount)
  print(final_price)
elif amount<10000:
  disc1=amount*0.1
  final_price=amount-disc1
  discount+=disc1
  print(discount)
  print(final_price)
elif amount<=0:
  print("Price can't be negative")
else:
  disc2=amount*0.5
  discount+=disc2
  final_price=amount-disc2
  print(discount)
  print(final_price)


#Write a program that converts temperature from Celsius to Fahrenheit.
#formula (°C × 9/5) + 32
while True:
  a=input("Input Degree/Farenheit Or You want to Exit : ")
  if(a=="Degree"):
    fah=int(input("Enter degree value = "))
    fahrenheit=(fah*9/5)+32
    print("Fahrenheit = ",fahrenheit)
  elif(a=="Fahrenheit"):
    cel=int(input("Enter fahrenheit value = "))
    celsius=(cel-32)*5/9
    print("Celsius = ",celsius)
  elif(a=="Exit"):
    print("Exiting the program")
    break
else:
  ("Invalid option")



# Write a program that checks if a number is even or odd.
a=int(input("Enter a value to be check : "))

if a%2==0:
  print("Even")
else:
  print("Odd")



#Write a program that checks if a number is positive, negative, or zero.
num=int(input("Enter a number to check : "))

if num>0:
  print("Positive")
elif num<0:
  print("Negative")
else:
  print("Zero")



#Write a program that checks if a student is admitted based on their test score.
test_score=int(input("Enter your score : "))

if test_score>=50:
  print("You are admitted")
else:
  print("Sorry, you missed!")



#Write a program that checks if a customer is eligible for a discount based on their purchase amount.
amount_purchased=int(input("Enter the amount purchased : "))

if amount_purchased>=10000:
  print("You are eligible for discount")
else:
  print("Purchase above 10,000 to get discount")



#Write a program that calculates the Body Mass Index (BMI) and categorizes it.
weight=float(input("Enter your weight : "))
height=float(input("Enter your height in meters : "))

bmi=weight//height**2
print("Your BMI is : ",bmi)

if bmi<18.5:
  print("Under weight")
elif 18.5<=bmi<24.9:
  print("Normal weight")
elif 25<=bmi<29.9:
  print("Over weight")
elif bmi>=30:
  print("Obese")
else:
  print("Invalid input")



# Write a Python program that checks if a number is divisible by 3, 5, or both.
num=int(input("Enter a number : "))

if num%3==0 and num%5==0:
  print(num," is divisible by both 3 and 5")
elif num%3==0:
  print(num," is divisible by 3")
elif num%5==0:
  print(num," is divisible by 5")
else:
  print("Enter a positive value")




#Write a Python program that solves quadratic equations (ax^2 + bx + c = 0) and displays the roots.

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
x=int(input("x:"))

equ=a*x**2+b*x+c

if equ==0:
  print("The equation satisfies the condition.")
else:
  print("For the provided number the equation is not satisfied.")




#Write a Python program that checks if a given number lies within a certain range [10, 20].

num=int(input("Enter a number "))

if num>10 and num<20:
  print(num," lies between 10 and 20")
else:
  print(num," not between 10 and 20")



#Write a Python program to check whether a triangle is valid or not given its three sides.
a=int(input())
b=int(input())
c=int(input())

if a+b>c and a+c>b and b+c>a:
  print("Triangle is possible")
else:
  print("Triangle is not possible")



#Write a Python program to check the strength of a password. It should have at least 8 characters, include at least one number, and at least one uppercase letter.
password=input("Password : ")

has_upper=False
has_digit=False

if len(password)>=8:
  for i in password:
    if i.isupper():
      has_upper=True
    if i.isdigit:
      has_digit=True
  if has_upper and has_digit:
    print("Password is strong")
  else:
    print("Password is not strong enough")
else:
  print("Password must have atleast 8 characters")



#Write a Python program to determine the season based on the given month.
mon=input("")
month=mon.capitalize()
if month=="March" or month=="April" or month=="May":
  print(month,": Summer")
elif month=="June" or month=="July" or month=="August":
  print(month,": Spring")
elif month=="September" or month=="October" or month=="November":
  print(month,": Rainy")
elif month=="December" or month=="January":
  print(month,": Winter")
else:
  print("Invalid Input")



#Write a Python program that maps a number (1-7) to a day of the week.

date=int(input("Date : "))

if date==1:
  print("It's Sunday")
elif date==2:
  print("It's Monday")
elif date==3:
  print("It's Tuesday")
elif date==4:
  print("It's Wednesday")
elif date==5:
  print("It's Thursday")
elif date==6:
  print("It's Friday")
elif date==7:
  print("It's Saturday")
else:
  print("Invalid input")



#Check Vowel or Consonant:: Write a Python program that checks whether a given character is a vowel or consonant.
char=input("Enter a character to be check : ")

if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
  print("Vowels")
else:
  print("Consonants")



#Employee Bonus Calculation
exp=int(input("Years of Experience : "))
sal=int(input("Salary : "))

if exp>10:
  sal+=sal*0.1
  print("For",exp,"years of experience your bonus is 10%. Now your salary+bonus for this month is Rs.",sal)
elif exp>=5 and exp<=10:
  sal+=sal*0.05
  print("For",exp,"years of experience your bonus is 5%. Now your salary+bonus for this month is Rs.",sal)
else:
  sal+=sal*0.02
  print("For",exp,"years of experience your bonus is 2%. Now your salary+bonus for this month is Rs.",sal)



#Palindrome
value=input()
rev_value=value[::-1]
if value==rev_value:
  print("Palinrome")
else:
  print("Not a palindrome")