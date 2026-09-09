def main():
    x = float(input("What's x? "))
    y = float(input("What's y? "))

    print(square(x))
    print(sum2nums(x,y))

def sum2nums(x, y):
    z = round(x + y, 2)
    return z

def square(n):
    n = float(n)
    return n**2

main()