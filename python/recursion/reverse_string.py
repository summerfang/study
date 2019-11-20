def reverseString(s, first=0, last=-1):
        if first >= len(s)/2:
            return
        else:
            s[first], s[last] = s[last], s[first]
            reverseString(s, first+1, last -1)

s = ['A','B','C','D','E','F']
reverseString(s)
print(s)

def reverse_string(s):
    if len(s) <= 1:
        return
    else:
        s[0], s[-1] = s[-1], s[0]
        s_tmp = s[1:-1]
        reverse_string(s_tmp)
        s[1:-1] = s_tmp

s = ['A','B','C','D','E','F']
reverse_string(s)
print(s)