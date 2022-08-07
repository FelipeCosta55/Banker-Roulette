import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

names_len = len(names)

random_names = random.randint(0, names_len - 1)

sorted_name = names[random_names] 
print(f"{sorted_name} is going to buy the meal today!")