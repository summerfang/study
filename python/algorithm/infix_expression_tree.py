OPERATORS_LIST = ['(',')','and','or','!=','=','<','<=','>','>=']

def precedence(operator):
    if operator in ['and', 'or']:
        return 1
    elif operator in ['=', '<', '<=', '>', '>=']:
        return 2
    return 0

def is_valid_infix_expression(lst):
    operators = []
    output = []

    operand_count = 0
    operator_count = 0
    for item in lst:
        if item == '(':
            operators.append(item)
        elif item == ')':
            while operators and operators[-1] != '(':
                op = operators.pop()
                output.append(op)
            
            if not operators:
                return False
            
            operators.pop()

        elif item in OPERATORS_LIST:
            if operators and precedence(operators[-1]) >= precedence(item):
                op = operators.pop()
                output.append(op)

            operators.append(item)

            operator_count += 1
        else:
            output.append(item)
            operand_count += 1
            if operand_count <= operator_count:
                return False
    while operators:
        op = operators.pop()
        output.append(op)

    
    if operand_count != operator_count + 1:
        return False
    
    return not operators

import re

def split_string_with_separators(input_string):
    # Create a regular expression pattern that captures the separators
    pattern = '|'.join(map(re.escape, OPERATORS_LIST))

    # Use re.split with capturing parentheses to split the string while preserving separators
    tokens = re.split(f'({pattern})', input_string)

    # Filter out empty strings from the resulting list of tokens
    tokens = [token.strip() for token in tokens if token.strip() != '']

    return tokens

def is_conditions_valid(input_string):
    result = split_string_with_separators(input_string)
    return is_valid_infix_expression(result)

#input_string = "City='NY' and (Popu>10) and (age < 20) or gender='female'"
input_string = "City='NY' > and Popu>10 and age < 20 or gender='female'"

#input_string = "City='NY'"
result = split_string_with_separators(input_string)
print(result)

# Example usage:
infix_expression = result
is_valid = is_valid_infix_expression(infix_expression)
print(is_valid)

