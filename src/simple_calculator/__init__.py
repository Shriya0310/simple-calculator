def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

def divide(a,b):
    if(b==0):
        return "Cannot divide by zero"
    return a/b;
def main():
    print("===== SIMPLE CALCULATOR =====")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("1. Addition")
    print("2. Subtraction")
<<<<<<< HEAD
    print("4. Division")
=======
    print("3. Multiplication")
>>>>>>> origin/main
    choice = input("Choose operation: ")
    if choice == "1":
        print("Result:", add(a, b))
    elif choice == "2":
        print("Result:", subtract(a, b))
<<<<<<< HEAD
    elif choice=="4":
        print("Result: ",divide(a,b))
=======
    elif choice == "3":
        print("Result:", multiply(a, b))
        
>>>>>>> origin/main
    else:
        print("Invalid choice!")


def multiply(a, b):
    return a * b


if __name__ == "__main__":
    main()