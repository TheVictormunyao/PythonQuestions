def factorial(n):
    result=1
    for i in range (1, n+1):
        result *= i
    return result

if __name__ == "__main__":
    #Taking input from the user
    number = int(input("Enter a number:"))
    print(f"The factorial of {number} is {factorial(number)}")