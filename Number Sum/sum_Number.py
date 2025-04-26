def numberSum(n):
    total = 0    
    #while loop to add digits in a number
    while n > 0:
        total += n % 10 #picks last digit to add to total
        n = n // 10 #drops the last digit
    return total

if __name__ == "__main__":
    #Taking input from the user
    numb = int (input("Enter number to sum :"))
    #Calling the function and printing the result
    print(f"The sum of the gits in {numb} is {numberSum(numb)}")
    