text = input('Please enter the string: ')
text=text.casefold() 
x=list(text)

stack = []
istack= []
for i in range(len(x)):
    stack.append(x[i])
#print("Printing the stack "+ str(stack))

stering=""
for i in range(len(x)):
    istack.append(stack.pop())
if x==istack:
    print(" The string you entered is a Palindrome")
else:
    print(" The string you entered is Not a palindrome")
    