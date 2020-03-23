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


import time


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


print_pause("Hello! I am Bob, the Breakfast Bot.")
print_pause("Today we have two breakfasts available.")
print_pause("The first is waffles with strawberries and whipped cream.")
print_pause("The second is sweet potato pancakes with butter and syrup.")


response = ""
while response != "waffles" and response != "pancakes":
    response = input(
        "Please place your order. Would you like waffles or pancakes?\n")
    if "waffles" in response.lower():
        print("Waffles it is!")
        time.sleep(2)
        break
    elif "pancakes" in response.lower():
        print("Pancakes it is!")
        time.sleep(2)
        break
    else:
        print("Sorry, I don't understand.")
        time.sleep(2)
print("Your order will be ready shortly.")
time.sleep(2)
