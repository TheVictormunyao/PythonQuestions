#Fuction to reverse a string input
def reverse_String(myString):
    reverse = "" #Start with an empty string
    for i in myString: #Iterate through each character in the string
        reverse = i + reverse #Add each character to the reverse string 
    return reverse #Return the reversed string

#Taking input String and reversing 
if __name__  == "__main__":
    string = input ("Enter any String : ")
    print(f"The reverse of {string} is {reverse_String(string)}")