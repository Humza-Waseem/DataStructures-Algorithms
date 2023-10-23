import math
import os
import sys

class Stack:
    def __init__(self):
        self.stack = []
    def push(self,val):
        self.stack.append(val)

    def isEmpty(self):
        if(len(self.stack) == 0):
            return True
        else:
            return False
        
    def pop(self):

        if not self.isEmpty():
            return self.stack.pop()
        else:
            return 0
    
    
    def peek(self):
        if  self.isEmpty() != True:
            return self.stack[-1]
        else:
            return "stack is Empty"

    def CalculateOperation(self,num1,num2,operator):
            self.push(num1)
            self.push(num2)
       
            if(operator == '+'):
                        print(f"You have entered '{operator}' operator")
                        num2 = self.stack.pop()
                        num1 = self.stack.pop()
                        result = int(num1)+int(num2)
                        return result
                    
            if(operator == '-'):
                        print(f"You have entered '{operator}' operator")
                        num2 = self.stack.pop()
                        num1 = self.stack.pop()
                        result = int(num1)-int(num2)
                        return result
                    
            if(operator == '*'):
                        print(f"You have entered '{operator}' operator")
                        num2 = self.stack.pop()
                        num1 = self.stack.pop()
                        result = int(num1)*int(num2)
                        return result
            if(operator == '/'):
                        print(f"You have entered '{operator}' operator")
                        num2 = self.stack.pop()
                        num1 = self.stack.pop()
                        result = int(num1)/int(num2)
                        # print("result = " ,result)
                        return math.floor(result)
            if(operator == '%'):
                        print(f"You have entered '{operator}' operator")
                        num2 = self.stack.pop()
                        num1 = self.stack.pop()
                        result = int(num1)%int(num2)
                        # print("result = " ,result)
                        return result

            if (operator == '?'):
                       print(f"You have entered '{operator}' operator")
                       self.toString()

            if (operator == '^'):
                       print(f"You have entered '{operator}' operator")
                       top = self.stack.pop()
                       print(f"TOP : {top}")
                       print(" ")
                       sys.exit()

                
            if (operator == '!'):
                print(f"You have entered '{operator}' operator")
                sys.exit()


            else:
                print("Invalid Input")     
                
    def  toString(self):
        i = 1
        while(self.stack):
            elements = stack.pop()
            print(f" {i}: element in the stack : {elements}")
            i+=1

    
##########    INPUT    ############
stack = Stack()
num1 = input("Enter First Character: ")
num2 = input("Enter second Character: ")


operator  = input("Enter the Operator: ")


if(len(operator)== 1):
  result = stack.CalculateOperation(num1,num2,operator)
  print(f"Result of {num1} {operator}  {num2}  = {result}")

else:
    os.system('cls')
    print("   #############    Invalid Operator Entered !!    ##############")



