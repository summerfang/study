import re

pattern_string = "\w \w"
string_be_search = "An Lee is a famous director"

if re.search(pattern_string, string_be_search):
    print("String patter is found!")
else:
    print("String patter is not found!")
