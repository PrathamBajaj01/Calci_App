import json
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



import json

def lambda_handler(event, context):
    a = event.get("a")
    b = event.get("b")
    operation = event.get("operation")
    
    if operation == "add":
        result = add(a, b)
    elif operation == "subtract":
        result = subtract(a, b)
    elif operation == "multiply":
        result = multiply(a, b)
    else:
        result = None

    # Return JSON string
    return {
        "statusCode": 200,
        "body": json.dumps({"result": result})
    }

   
    a = event.get('a', 0)
    b = event.get('b', 0)
    op = event.get('operation', 'add')

    try:
        if op == 'add':
            result = add(a, b)
        elif op == 'subtract':
            result = subtract(a, b)
        elif op == 'multiply':
            result = multiply(a, b)
        else:
            result = "Invalid operation"
    except Exception as e:
        result = str(e)

    return {"result": result}



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
