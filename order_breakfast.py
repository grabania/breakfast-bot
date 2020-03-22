# other way:
# response = input(
#     "Please place your order. Woild you like waffles or pancakes?\n").lower()
# if response == "waffles":
#     print("Waffles it is!")
# elif response == "pancakes":
#     print("Pancakes it is!")

response = input(
    "Please place your order. Would you like waffles or pancakes?\n")
if response.lower() == "waffles":
    print("Waffles it is!")
elif response.lower() == "pancakes":
    print("Pancakes it is!")
