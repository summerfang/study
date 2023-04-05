original_list =[['rishav', 10 , 'a'], ['akash', 5, 'c'], ['ram', 6, 'b'], ['gaurav', 15, 'd']]

def sort_by_value(x):
    return x[1]

# Sorted by a function
original_list.sort(key=sort_by_value)
print(original_list)

# Sorted by lambda
original_list.sort(key=lambda x: (x[2], x[1], x[0]))
print(original_list)

# Covert from dictionary to list
# Dictionary can be always transfered to a list. But a list doesn't necessary transfer to a dictionary
d = {"a": 3, "b": 1, "c": 4}
print(d.items())

d = {"a": [3, {"OK": 8}], "b": [1], "c": [4, {'John': 109}]}
print(d.items())

l = [('a',1),('b',2),(3,'c')]
dic = dict(l)
print(dic)

# Access content of a dictionary
print(d["c"][1]['John'])
print(dic[3])

# Do a function to calculate fibonacci

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
# Do a function to calculate decimal to binary
def decimal_to_binary(n):    
    if n == 0:
        return 0
    else:
        return n%2 + 10 * decimal_to_binary(int(n/2))
    

# test
print(decimal_to_binary(83))

# 