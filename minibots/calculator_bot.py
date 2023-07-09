import math
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
        if not ele == ' ':
            if ele == ')':
                while stack and stack[-1] != '(':
                    output += stack.pop(-1)
                    output += ' '
                # pop out the opening bracket
                if stack and stack[-1] == '(':
                    stack.pop(-1)
            elif ele == '(':
                stack.append(ele)
            elif isoperand(ele):
                output += str(ele)
                output += ' '
            else: # precedence is higher for the operator
                while stack and precedence.get(ele,0) <= precedence.get(stack[-1],0):
                    output += stack.pop(-1)
                    output += ' '
                stack.append(ele)
    # empty the stack
    while stack:
        output += stack.pop(-1)
        output += ' '
    return output

def callCalculate(name, exp):
    if 'calculate' in exp:
        exp = exp[9:]
    print(exp, 'previous expression')
    mode ='radians'
    print(f'Hello {name}')
    print('Mode: radians')
    parts = re.findall(r'[+/*^()-]|[a-z]+\(\d+\)|\d+', exp.lower())
    print(parts, 'check')       
    postfix = infix_to_postfix(parts)
    print(postfix, 'the expression ')
    ans = evaluatePostfix(postfix)
    return ans

def evaluatePostfix(postfix):
    ans = []
    operators = ['+', '-', '*', '/', '^']
    Spostfix = re.findall(r'[+/*^()-]|[a-z]+\(\d+\)|\d+', postfix)
    print(Spostfix, 'jjj')
    for ele in Spostfix:
        if ele.isdigit():
            ans.append(ele)
        elif any(func in ele for func in ['sin', 'tan', 'cos']):
            if ele[0].isalpha():
                ans.append(ele)
            else:
                ans.append(ele[1:-1])
        elif ele in operators:
            val1 = str(ans.pop())
            val2 = str(ans.pop())
            if any(func in val1 for func in ['sin', 'tan', 'cos']):
                value = val1[:3]
                theta = float(val1[4:-1]) 
                val1 = str(calc_trig(theta, value))
            if any(func in val2 for func in ['sin', 'tan', 'cos']):
                value = val2[:3]
                theta = float(val2[4:-1]) 
                val2 = str(calc_trig(theta, value))
            if ele == '^' :
                ans.append(int(math.pow(int(val2), int(val1))))
                continue
            ans.append((eval(val2 + ele + val1)))
    return ans

def calc_trig(theta, opr):
    if opr.lower() == 'sin':
        return math.sin(math.radians(theta)) 
    elif opr.lower() == 'cos':
        return math.cos(math.radians(theta)) 
    elif opr.lower() == 'tan':
        return math.tan(math.radians(theta)) # arc tan etc 'll be added

expression = "calculate (sin(30) + 40) * (3^2 - cos(30))"
name = 'Anas'
result = callCalculate(name, expression)
print("Result:", result)
