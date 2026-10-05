#this will give a TypeError
#print(len(1234))
print(len("Hello"))
#Subscripting
#print("hello"[0])
#print("Hello"[-5])

# Strings
#print("123" + "345") #concatenation

# Integers - Whole Numbers
#print(123 + 345)

#Large Integers
#print(123_123_123)

#Float - Floating Point Number
#print(3.1415)
#print(123_456.789)

#boolean
#print(True)
#print(False)

#Quiz Question
#street_name = "Abbey Road"
#print(street_name[4] + street_name[7])

#print(type(4424.2))
#print(type(234))
#print(type("Dishita"))
#print(type(True))

#print(int("123") + int("345"))
#name_of_the_user = input("Enter you name ")
#len_of_username = len(name_of_the_user)
#print("Number of letters in your name: " + str(len_of_username))

#print(3 * 3 + 3 / 3 - 3)
#print((3 * (3 + 3) / 3) - 3)


#This was the activity in the course

height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = (weight/(height**2))

print(bmi)
print(int(bmi))
print(round(bmi))
print(round(bmi, 2))

#User scores a point
score = 0
score += 1
print(score)

#f strings
#print("Your score is " + str(score))

score = 0 
height = 1.8
is_winning = True
print(f"Your score is = {score}, your height is {height}. Your winnings are {is_winning}")