print("This is a sample Python script for even number checking.")

def check_even(name):
    if name % 2 == 0:
        return True    
    return False

number = 28
if check_even(number):
    print(f"{number} is an even number.")
else:    print(f"{number} is not an even number.")                    
if __name__ == "__main__":
    print("This code is running as the main program.")
    