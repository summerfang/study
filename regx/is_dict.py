import re

str_columns = "(col1: int, col2: str)"

pattern_dict = r'\(([\s^,]+:[\s(?i)(int|string)]\s+?)\)'

if re.match(pattern_dict, str_columns):
    str_columns_definition = str_columns[1:-1]
    print(str_columns_definition)