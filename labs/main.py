# No starter code provided — write the full program yourself.
#
# Prompts must be exactly: "Age: " and "Day type (weekday/weekend): "
# Final output must be exactly: "Price: {price}"
age = int(input("Age: "))
day = input("Day type (weekday/weekend): ")

if age < 5:
    price = 0
    print(f"Price: {price}")
elif age >= 5 and age <= 12 and day == "weekday":
    price = 1500
    print(f"Price: {price}")
elif age >= 5 and age <= 12 and day == "weekend":
    price = 2000
    print(f"Price: {price}")
elif age >= 13 and age <= 59 and day == "weekday":
    price = 2500
    print(f"Price: {price}")
elif age >= 13 and age <= 59 and day == "weekend":
    price = 3500
    print(f"Price: {price}")
elif age >= 60 and day == "weekday":
    price = 1200
    print(f"Price: {price}")
elif age >= 60 and day == "weekend":
    price = 1800
    print(f"Price: {price}")