# other way:
# response = input(
#     "Please place your order. Woild you like waffles or pancakes?\n").lower()
# if response == "waffles":
#     print("Waffles it is!")
# elif response == "pancakes":
#     print("Pancakes it is!")

# or:
# while True:
#     response = input(
#         "Please place your order. Would you like waffles or pancakes?\n").lower()
#     if response == "waffles":
#         print("Waffles it is!")
#         break
#     elif response == "pancakes":
#         print("Pancakes it is!")
#         break
#     else:
#         print("Sorry, I don't understand.")

print("Hello! I am Bob, the Breakfast Bot.")
print("Today we have two breakfasts available.")
print("The first is waffles with strawberries and whipped cream.")
print("The second is sweet potato pancakes with butter and syrup.")
response = ""
while response != "waffles" and response != "pancakes":
    response = input(
        "Please place your order. Would you like waffles or pancakes?\n")
    if "waffles" in response.lower():
        print("Waffles it is!")
        break
    elif "pancakes" in response.lower():
        print("Pancakes it is!")
        break
    else:
        print("Sorry, I don't understand.")
