# # #LOOPS RANGE and CODE BLOCKS
# # for item in list_of_items:
# #     #do somethings
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " PIE ")
#     print(fruits)
# #indentation is Important in python 

# student_scores = [150, 142, 185, 120, 171, 184, 190, 34, 78, 100]
# total_exam_score = sum(student_scores)
# sum = 0
# for score in student_scores:
#     sum += score
# print(sum)
# max_score = 0
# for score in student_scores:
#     if score > max_score:
#         max_score = score
# print(max_score)

#Range
# for number in range(a, b):
#     print(number)
#range function doesnot do anything by its own.
# for number in range(1, 11, 2):
#     print(number)
#2 here tell the computer to skip for 2
sum = 0
for number in range(1, 101):
    sum += number
    print(number)
print(sum)

for number in range(1, 101):
    number_three = (number % 3) == 0
    number_five = (number % 5) == 0
    divisible_by_both = number % 3 == 0 and number % 5 == 0
    if divisible_by_both:
        print("FizzBuzz")
    elif number_three:
           print("Fizz")
    elif number_five:
           print("Buzz")
    else:
        print(number)