'code in progress' 
import math
import re
import nltk
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
    mode ='radians'
    print(f'Hello {name}')
    print('Mode : radians')
    # if any(func in exp for func in ['sin', 'cos', 'tan']):
    #     inp = input('Press \'d\' to covert in degrees ')
    #     print('------- Press any key to continue --------')
    #     if inp =='d':
    #         mode = 'degree'
 
    parts = re.split(r'([+\-*^/])',exp)
    parts = [part.strip().lower() for part in parts if part.strip()] 
    #remove one sided brackets:
    for i, ele in enumerate(parts):
        if ele[-1]==')':
            bracket = ele[-1]
            no =ele[:-1]
            parts.insert(i,no)
            parts.insert(i+1,bracket) 
        elif ele[0]=='(':
            bracket =ele[0]
            no =ele[1:]
            parts.insert(i, bracket)
            parts.insert(i+1,no)
  
           
    # exp = infix_to_postfix(parts)

    print(parts,'the expression ')
#     if "calculate" in exp:
#         exp = exp[9:] #after calculate_
#         parts = re.split(r'([+\-*/])',exp) #splits the expression
#         print(parts,'fjfj')

       
     
        
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
    
# def calc_trig(theta,opr):
#     if opr.lower() =='sin':
#         return math.sin(theta) 
#     elif opr.lower() =='cos':
#         return math.cos(theta) 
#     elif opr.lower() =='tan':
#         return math.tan(theta)# arc tan etc 'll be added
    


        
expression = "calculate (sin(45) + 2) * (3^2 - cos(30))"

name = 'Anas'
result = callCalculate(name,expression)
print("Result:", result)


