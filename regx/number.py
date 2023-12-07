import re

def is_number(num_str: str)->bool:
    number_pattern = r'^[0-9].*?$'

    mo = re.match(number_pattern, num_str)
    print(mo)
    # mo = re.findall(number_pattern, num_str)
    # mo = re.search(number_pattern, num_str)
    # mo = re.finditer(number_pattern, num_str)
    # mo = re.fullmatch(number_pattern, num_str)

    if mo:
        return True
    else:
        return False

def is_real_number(num_str: str)->bool:
    real_num_ptn = '[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?'
    mo = re.match(real_num_ptn, num_str)
    
    return mo != None