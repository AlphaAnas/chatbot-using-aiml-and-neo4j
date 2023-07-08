'''steps :
 code in progress right now
'''

import math
import re
import nltk
import re
def isoperand(inp):
    if inp.isdigit():
        return 1
    elif any(func in inp for func in ['sin', 'cos', 'tan']):
        return 1
         
    return 0

def isoperator(inp):
    lst=['+','-','/','*','%']
    if inp in lst:
        return True
    else:
        return False

def infix_to_postfix(exp):
   
    precedence={"+":1,"-":1,"*":2,"/":2,"^":3,"**":3}
    output = ''
    stack = []
    for ele in exp:
        if not(ele)==' ':
 
            if ele ==')':
                while stack and stack[-1] != '(':
                        output += stack.pop(-1)
                if stack and stack[-1] =='(':
                        stack.pop(-1)
        
            elif ele == '(':
                stack.append(ele)
        
            elif isoperand(ele):
                output += str(ele)
            else: # precedence is higher of the operator
              
              
                while not(ele)==' ' and stack and precedence.get(ele,0) <= precedence.get(stack[-1],0):
                    output += stack.pop(-1)
                stack.append(ele)
    # empty the stack
    while stack:
        output += stack.pop(-1)
    return output

        


def callCalculate(name,exp): 
    if 'calculate' in exp:
        exp = exp[9:]
    print(exp, 'previous expressino')
    mode ='radians'
    print(f'Hello {name}')
    print('Mode : radians')
    parts = re.split(r'([+\-*^/])',exp)
    parts = [part.strip().lower() for part in parts if part.strip()] 
    #remove one sided brackets:
    for i, ele in enumerate(parts):
        if len(ele) >1:
            if ele[-1]==')' and not(ele[0] == '('):
                bracket = ele[-1]
                no =ele[:-1]
                parts[i]= no
                parts.insert(i+1,bracket) 
            elif ele[0]=='(' and not(ele[-1]==')'):
                bracket =ele[0]
                no =ele[1:]
                parts[i] = bracket
                parts.insert(i+1,no)
 
  
           
    postfix = infix_to_postfix(parts)

    print(postfix,'the expression ')

    ans = evaluatePostfix(postfix)
    print(ans, 'final')

def evaluatePostfix(postfix):
    ans = []
    operators = ['+', '-', '*' ,'/', '^']
    Spostfix = split(postfix)

   
    for ele in Spostfix:

        # If the scanned character is an operand
        # (number here) push it to the stack
        if ele.isdigit():
            ans.push(ele)
        elif any(func in ele for func in ['sin', 'tan', 'cos']):
            ans.push(ele)

        elif ele in operators:
            val1 = ans.pop()
            val2 = ans.pop()
            if any(func in val1 for func in ['sin', 'tan', 'cos']):
                val1 = calc_trig(ele)
            if any(func in val2 for func in ['sin', 'tan', 'cos']):
                val2 = calc_trig(ele)
        
            ans.append(str(eval(val2 + ele + val1)))

    return ans


       
def split(postfix):
    out =[]
    for i,ele in enumerate(postfix):
        if ele.isalpha():
            out.append(postfix[i:i+7]) # extract the "sin(angle)"
        e       
        
#         print(parts, 'bd wala')

        
#         operator = '+'
#         temp = []
#         ans = [0]
#         for element in (parts):
#             print(element)

#             if element.isnumeric():
#                 number= float(element)
#                 previous = ans[-1]
#                 exp = 'number operator previous'
#                 result = eval(number)
#                 ans.append(result)
#             elif element.startswith('sin') or element.startswith('cos') or element.startswith('tan'):
#                 theta = float(element[4:-1])
#                 if mode == 'degree':
#                     theta =math.radians(theta)
#                 opr = element[:3]
#                 result = calc_trig( theta , opr)
#                 ans.append(result)
#             elif element.startswith('(') :
            
#                 number = float(element [1:]) # remove the bracket
#                 previous = ans[-1]
#                 exp = str(number)+str(operator)+str(previous)
#                 result = eval(exp)
#                 ans.append(result)
        
#             else : 
#                 operator = element
#         sum1 =sum(ans)
#         return sum1





      
            
#         # return eval(exp)
#     # else:
#     #     exp = exp[5:] # after solve_
#     #     return eval(exp)
    
def calc_trig(theta,opr):
    if opr.lower() =='sin':
        return math.sin(theta) 
    elif opr.lower() =='cos':
        return math.cos(theta) 
    elif opr.lower() =='tan':
        return math.tan(theta)# arc tan etc 'll be added
    


        
expression = "calculate (sin(45) + 2) * (3^2 - cos(30))"

name = 'Anas'
result = callCalculate(name,expression)
print("Result:", result)


