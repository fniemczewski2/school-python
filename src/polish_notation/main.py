 
def is_operand(c):
    return c.isdigit()
 
def evaluate(expression):
    stack = []

    for c in expression[::-1]:
 

        if is_operand(c):
            stack.append(int(c))
 
        else:

            o1 = stack.pop()
            o2 = stack.pop()
 
            if c == '+':
                stack.append(o1 + o2)
 
            elif c == '-':
                stack.append(o1 - o2)
 
            elif c == '*':
                stack.append(o1 * o2)
 
            elif c == '/':
                stack.append(o1 / o2)
 
    return stack.pop()
 
 
if __name__ == "__main__":
    test_expression = "-+8/632"
    print(evaluate(test_expression))

    test_expression = "-+7*45+20"
    print(evaluate(test_expression))
 

