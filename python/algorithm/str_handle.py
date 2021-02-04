from typing import no_type_check


def str_handle(s):
    c_start = s[0]
    r = dict()
    r[c_start] = 0
    l_r = list()

    for c in range(len(s)):
        if s[c] == c_start:
            r[c_start] += 1
        else:
            tp_pair = (c_start, r[c_start])
            l_r.append(tp_pair)
            r.clear()
            c_start = s[c]
            r[c_start] = 1
            if c == len(s) - 1:
                tp_pair = (c_start, r[c_start])
                l_r.append(tp_pair)
        
    return l_r

st = "aaaabbbcca"
print(str_handle(st))