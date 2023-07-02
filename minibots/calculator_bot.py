'''steps :
 1. split the given expression into parts like : cosine(45)+45 = > 'cosine(45)', '+', '45'
 2. send each element to its respective function.
 3. First calculate trignometric functions and get their answers.
 4. Then perform add/ sub or any other operation to the answers and elements.
 5. Generate a final answer to return.
'''

import math
import re

def callCalculate(name,exp):
    print(f'Hello {name}')
    if "calculate" in exp:
        exp = exp[9:] #after calculate_
        parts = re.split(r'([+\-*/()])',exp) #splits the expression

        parts = [part.strip() for part in parts if part.strip()]

        result =0
        operator = '+'
        arr = []
        for element in (parts):

            if element.isnumeric():
                number= float(element)
                result = calculate(result, operator, number)
            elif element.startswith('sin(') or element.startswith('cos(') or element.startswith('tan('):
                theta = float(element[4:-1])
                opr = element[:3]
                result = calc_trig(result, theta, number , opr)
            elif element =='(':
                arr.append((result, operator)) # store the result and opr before the bracket to use after
                result =0 
                operator = '+'
            elif element == ')':
                pr_result, pr_opr = arr.pop()
                result = calculate(pr_result, pr_opr, result)
            else : 
                operator = element





      
            
        return eval(exp)
    else:
        exp = exp[5:] # after solve_
        return eval(exp)
    
def calc_trig(result, theta, num, opr):
    if opr.lower() =='sin':
        return math.sin(theta) +result
    elif opr.lower() =='cos':
        return math.cos(theta) +result
    elif opr.lower() =='tan':
        return math.tan(theta) +result # arc tan etc 'll be added
    

def calculate(num1, opr, num2):
    if opr == '+':
        return num1 + num2
    elif opr == '-':
         return num1 - num2
    elif opr == '*':
         return num1 * num2
    elif opr == '/':
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero.")
        
expression = "calculate sin(30) + sin(30)"
name = 'Anas'
result = callCalculate(name,expression)
print("Result:", result)


