string = input("Enter a string ")
string = string.casefold() 
reversed_string = reversed(string)
if list(string) == list(reversed_string):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")