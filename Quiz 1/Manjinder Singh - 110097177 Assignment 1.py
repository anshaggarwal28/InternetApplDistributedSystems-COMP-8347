"""
Name - Manjinder Singh
Student ID - 110097177
"""
def is_prime(n):
    # Checking the input number as prime number is always +ve.
    if n <= 1: # Number less than 1 and 1 is not prime.
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    try:
        user_input = int(input("Input any number: "))
        if is_prime(user_input):
            print(f"{user_input} is a valid prime number.")
        else:
            print(f"{user_input} is not a prime number.")
    except ValueError:
        print("Your input is invalid. Please enter a valid number.")

if __name__ == "__main__":
    main()