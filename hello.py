# Ask users for their name
# Remove white spaces and capitalize user's name
name = input("What's your name? ").strip().title()

print(f"Hello, {name}")

# Split user's name into first name and last name
first, last = name.split(" ")
print(f"Hello, {first} {last}")


# obj = {"Alex","eats","pasta"}
obj = ["Alex","eats","pasta"]
print(*obj, sep=' ', end='\n')