import re

name = "Summer Fang Ann Lee Smith Johnson"
pattern = 'Fang'
print("---------Python regular expression-------")
print(re.match('n', name))
print("re.match(pattern, name) =" , re.match(pattern, name))
print("re.findall(pattern, name) =", re.findall(pattern, name))
print("re.search(pattern, name) =", re.search(pattern, name))
print("re.split(pattern, name) =", re.split(pattern, name))
print("re.sub(pattern, '<Found>', name) =", re.sub(pattern, '<Found>', name))