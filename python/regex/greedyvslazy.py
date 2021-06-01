import re

greedy = r'a.*?c'
mo = re.search(greedy, "abcdefghijklmc")
if(mo is not None):
    print(mo.group(0))