
class regex:
    
    def __init__(self, inFix):
        self.inFix = inFix
        self.posFix = ""
        __outputCode = self.__infixToPosfix()
        self.__checkError(__outputCode)
    
    # check if the infix to postfix worked
    def __checkError(self, errorCode):
        if(errorCode == -1):
            print("-1: closing of parentheses without opening")
        elif(errorCode == 0):
            print("0: opening of parentheses without closing")
        elif(errorCode == 1):
            print("1: operator without operand")
        else:
            print("2: EVERYTHING OK!!! :D", end="\n\n")

    # check the precedence between two operands
    def __precedence(self, op1, op2):
        if op1 == op2 :
            return True

        if op1 != '+' and op2 != '+' :
            if op1 == '*' :
                return True
            else:
                return False
        
        if op1 != '+' :
            return True
        
        return False

    # check if a character is an operator
    def __isOperator(self, character):
        if character == '*' or character == '+' or character == '.':
            return True
        return False

    # convert infix to postfix
    def __infixToPosfix(self):
        aux = 0
        stack = []
        op = ''
        temp_posFix = []

        i = 0
        # for i in range(len(self.inFix)):
        while(i < len(self.inFix)):
            print(i)
            # if(i == 8):
            #     print(f"current: {self.inFix[i]}")
            #     print(f"stack: {stack}")
            #     print(f"output: {temp_posFix}")
            #     print(f"aux: {aux}")

            # operator
            if(self.__isOperator(self.inFix[i]) or (aux and not self.__isOperator(self.inFix[i]) and self.inFix[i] != ')')):
                if(aux and not self.__isOperator(self.inFix[i])):
                    op = '.'
                    aux = 0
                    i = i - 1
                else:
                    op = self.inFix[i]
            
                while(stack and stack[len(stack) - 1] != '(' and self.__precedence(stack[len(stack) - 1], op)):
                    temp_posFix.insert(len(temp_posFix), stack.pop())

                stack.insert(len(stack), op)

                aux = 1 if op == '*' else 0

            # opening of parentheses
            elif (self.inFix[i] == '('):
                stack.insert(len(stack), self.inFix[i])

            # closing of parentheses
            elif (self.inFix[i] == ')'):
                while(stack[len(stack) - 1] != '(' and stack):
                    temp_posFix.insert(len(temp_posFix), stack.pop())
                
                # closing of parentheses without opening
                if(not stack):
                    return -1

                stack.pop()
                aux = 1

            # operand
            else:
                temp_posFix.insert(len(temp_posFix), self.inFix[i])
                aux = 1
        
            # print("stack")
            # print(stack)
            # print("output")
            # print(temp_posFix)
            i += 1
        
        while(stack):
            if (stack[len(stack) - 1] == '('): # opening of parentheses without closing
                return 0

            temp_posFix.insert(len(temp_posFix), stack.pop())
        
        self.posFix = "".join(temp_posFix)
        return 2

    # check if the postfix regex is valid
    def isValid(self):
        stack = []

        for i in range(len(self.posFix)):
            if (not self.__isOperator(self.posFix[i])):
                stack.insert(len(stack), self.posFix[i])
            else: # is an operator
                if (stack):
                    if (self.posFix[i] == '*'):
                        continue
                    else:
                        stack.pop()
                        if(stack):
                            continue
                        else:
                            return False
                else:
                    return False
        
        if (not stack):
            return False

        stack.pop()

        if(stack):
            return False
        
        return True