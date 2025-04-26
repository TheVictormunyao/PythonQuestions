def recursive (n):
    if n==0 or n==1:
        return 1
    else :
        return n * recursive(n-1)
    
if __name__ == "__main__":
        #Taking input from the user
        number = int(input("Enter a number : "))
        print(f"The factorial of {number} is : {recursive(number)}")