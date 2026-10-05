#randomization
import random
# # import my_module
# # random_integer = random.randint(1,10)
# # print(random_integer)
# # print(my_module.myfavourite_number)

# # random_number_0_to_1 = random.random()*10
# # print(random_number_0_to_1)
# # random_float = random.uniform(1,10)
# # print(random_float)

# # heads and tails randomization example
# random_heads_or_tails = random.randint(0,1)
# # print(random_heads_or_tails)
# if random_heads_or_tails == 0:
#     print("Heads")
# else:
#     print("Tails")

# #lists: storing the data
# fruits = ["Cherry", "Apple", "Grapes"]
# states_of_america = ["Delaware", "Virginia", "Georgia"]
# #order of the list is important because as you store it you print it.
# print(states_of_america [-1])
# #-1 is the last thing in the list.
# states_of_america[1] = "Viriiginai"
# #you can edit the list like this.
# print(states_of_america [-2])
# states_of_america.append("Agelaland")
# #for adding somethings at the end of the list we can do this "Append function"
# print(states_of_america)
# #states_of_america.extend() adds multiple things in list
# states_of_america.extend(["India", "Canada"])
# print(states_of_america)

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(random.choice(friends))

# dirty_dozen = [
#     ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes"],
#     ["Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
# ]
fruits = [
    "Strawberries",
    "Nectarines",
    "Apples",
    "Grapes",
    "Peaches",
    "Cherries",
    "Pears"
]
vegetables = [
    "Spinach",
    "Kale",
    "Tomatoes",
    "Celery",
    "Potatoes"
]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen [0][1])
#nested list: list in list
#so when you seee the print list for the dirty dozen you will see two lists 
