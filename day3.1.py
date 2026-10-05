# print("Welcome to Python Pizza Deliveries!")
# size = (input("What size of pizza do you want? S, M or L: "))
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# if size == "S":
#     # print("Your Pizza size is small.")
#     bill = 15
#     if pepperoni == "Y":
#         bill += 2
#         # print(f"Your total bill is {bill}")
#     if extra_cheese == "Y":
#         bill += 1
#         print(f"Your final bill is ${bill}")
#     else:
#         print(f"Your total bill is ${bill}")
# elif size == "M":
#     # print("Your Pizza size is medium.")
#     bill = 20
#     if pepperoni == "Y":
#             bill += 3
#     if extra_cheese == "Y":
#             bill += 1    
#             print(f"Your final bill is ${bill}")    
#     else:
#         print(f"Your total bill is ${bill}")
# elif size == "L":
#     # print("Your Pizza size is large.")
#     bill = 25
#     if pepperoni == "Y":
#             bill += 3
#     if extra_cheese == "Y":
#             bill += 1
#             print(f"Your final bill is ${bill}")
#     else:
#         print(f"Your total bill is ${bill}")
# else:
#     print("Not applicable.")


# teacher code.
print("Welcome to Python Pizza Deliveries!")
size = (input("What size of pizza do you want? S, M or L: "))
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill +=25
else:
    print("You typed the wrong inputs.")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is ${bill}")
