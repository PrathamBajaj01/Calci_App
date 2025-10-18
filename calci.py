def add(a, b):
    
    if a < 0 or b < 0:
        raise ValueError("Only positive integers are allowed.")
    return a + b


def subtract(a, b):

    if a < 0 or b < 0:
        raise ValueError("Only positive integers are allowed.")
    return a - b


def multiply(a, b):
    
    if a < 0 or b < 0:
        raise ValueError("Only positive integers are allowed.")
    return a * b


if __name__ == "__main__":
    print("Simple Calculator")
    print("1. Add\n2. Subtract\n3. Multiply")
    choice = input("Enter choice (1/2/3): ")

    a = int(input("Enter first positive integer: "))
    b = int(input("Enter second positive integer: "))

    if choice == "1":
        print("Result:", add(a, b))
    elif choice == "2":
        print("Result:", subtract(a, b))
    elif choice == "3":
        print("Result:", multiply(a, b))
    else:
        print("Invalid choice!")
