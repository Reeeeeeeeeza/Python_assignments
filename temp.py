def compare(top,bottom):                 #This function does the comparing of top and bottom of the stack
    if top == '(' and bottom == ')':     #and returns true if condition meets
        return True                      
    if top == '[' and bottom == ']':
        return True
    if top == '{' and bottom == '}':
        return True  
    return False                         #else returns false
TOP=-1
def fun(BR):                             #this function takes the string of braces as argument
    stack=[]                             #declaring an empty stack
    for i in range(len(BR)):             #using for loop to append the braces
        if BR=='[' or BR=='(' or BR=='{':
            stack.append(BR[i])
        elif BR==']' or BR==')' or BR=='}': 
            if len(stack)==0:#this line chexs if you enter ]or)or} without appending any bracket then it will return false
                return False
            if not compare(TOP,BR[i]):
                stack.pop()
            else:
                return False  
    if len(stack)==0:
        return True
    else: return False
       




BR=str(input("Enter the set of brackets "))
print(fun(BR))

