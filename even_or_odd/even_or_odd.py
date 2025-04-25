def even_or_odd(number):
    if number%2 == 0:
        return "Even"
    else:
        return "odd"
    
if __name__ == "__main__":
    
    #Taking input from the user
    number = int(input("Enter a number: "))
    result = even_or_odd(number)
    print(f"The number {number} is {result}.")
