def main():
    name = input("What's your name? ").strip().title()
    hello(name)

# Ask users for their name
def hello(to="Alex"):
    # Remove white spaces and capitalize user's name

    print(f"Hello, {to}")

# Split user's name into first name and last name
# first, last = name.split(" ")
# print(f"Hello, {first} {last}")


# obj = {"Alex","eats","pasta"}
# obj = ["Alex","eats","pasta"]
# print(*obj, sep=' ', end='\n')

main()