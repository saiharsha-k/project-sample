print("Hello, world!")

print("This is a sample Python script.")


# This function checks if a number is prime.
def check_prime(name):
    if name < 2:
        return False
    for i in range(2, int(name**0.5) + 1):
        if name % i == 0:
            return False    
    return True

number = 29
if check_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

if __name__ == "__main__":
    print("This code is running as the main program.")