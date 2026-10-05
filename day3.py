# if condition:
#    do this
# else:
#    do this

# if condition1:
#     do this
# elif condition2:
#     do this
# else:
#     do this

# example
# water_level = 50
# if water_level > 80:
#    print("Drain water")
# else:
#    print("Continue")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
   print("You can ride the rollercoaster")
   age = int(input("What is your age? "))
  
   if age <= 12:
       print("Child ticket is for $5.")
       bill = 5
   elif age <= 18:
       print("Youth ticket is for $7")
       bill = 7
   elif age >= 45 and age <= 55:
       bill = 0
       print("Everything is going to be ok. have a free ride on us!")
   else:
       print("Adult ticket is for $12. ")
       bill = 12
   wants_photo = input("Do you want to have a photo take? Type y for yes and n for no.")
   if wants_photo == "y":
       #add $3 to their bill
       bill += 3
   print(f"Your final ticket price is {bill}")    
else:
    print("Sorry you have to grow taller before you can ride.")

# exercise
# weight = 85
# height = 1.85

# bmi = weight / (height ** 2)

# # 🚨 Do not modify the values above
# # Write your code below 👇
# if bmi >= 25:
#     print("Overweight")
# elif bmi >= 18.5:
#     print("Normal Weight") 
# else:
#     print("Underweight")      

# Even number 12 % 2 == 0

# print("Checking the number entered by you is Even or Odd")
# num = int(input("Enter the number of your choice... "))
# if num % 2 == 0:
#     print("Your number is Even")
# else:
#     print("You entered an Odd number")

#logical operators
# A and B
# c or d
# not E
