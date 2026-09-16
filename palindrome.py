# Program to check whether a string is a palindrome using recursion

def palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return palindrome(s[1:-1])


string = input("Enter a string: ")

if palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")