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

response = ""
while response != "waffles" and response != "pancakes":
    response = input(
        "Please place your order. Would you like waffles or pancakes?\n")
    if response.lower() == "waffles":
        print("Waffles it is!")
    elif response.lower() == "pancakes":
        print("Pancakes it is!")
    else:
        print("Sorry, I don't understand.")
