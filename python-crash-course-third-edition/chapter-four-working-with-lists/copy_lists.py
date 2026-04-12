my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

my_foods.append("ice cream")
friend_foods.append("burger")

print("My favority foods are:")

for food in my_foods:
    print(food)

print("\nMy friend's favority foods are:")

for food in friend_foods:
    print(food)