from typing import List

class Math4Leetcode(object):
    def __init__(self):
        pass

    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
    
        reversed_x = 0
        px = x
        while px != 0:
            remain = px % 10
            px = px // 10
            reversed_x = reversed_x*10 + remain

        return reversed_x == x

    def romanToInt(self, s: str) -> int:
        sum_of_s = 0

        for i in range(len(s)):
            if s[i] == 'I':
                if i + 1 < len(s) and (s[i+1] == 'V' or s[i+1] == 'X'):
                    sum_of_s -= 1
                else:
                    sum_of_s += 1
            if s[i] == 'V':
                sum_of_s += 5
            if s[i] == 'X':
                if i + 1 < len(s) and (s[i+1] == 'L' or s[i+1] == 'C'):
                    sum_of_s -= 10
                else:
                    sum_of_s += 10
            if s[i] == 'L':
                sum_of_s += 50
            if s[i] == 'C':
                if i + 1 < len(s) and (s[i+1] == 'D' or s[i+1] == 'M'):
                    sum_of_s -= 100
                else:
                    sum_of_s += 100
            if s[i] == 'D':
                sum_of_s += 500
            if s[i] == 'M':
                sum_of_s += 1000

        return sum_of_s

    def plusOne(self, digits: List[int]) -> List[int]:
        step_up = 0
        len_of_int = len(digits)
        plus_1 = []
        for i in range(len_of_int-1,-1,-1):
            if i == len_of_int-1:
                last = int(digits[i]) + 1
                if last == 10:
                    step_up = 1
                    last = 0
                plus_1.insert(0, last)
                continue
            last = int(digits[i]) + step_up
            if last >= 10:
                step_up = 1
                last = 0
            else:
                step_up = 0
            plus_1.insert(0, last)
        if step_up == 1:
            plus_1.insert(0, 1)

        return plus_1
    
    def longestPalindrome(self, s: str) -> int:
        len_of_s = len(s)
        dict_of_s = {}
        unique_in_s = []
        for i in range(len_of_s):
            if s[i] not in unique_in_s:
                unique_in_s.append(s[i])
                dict_of_s[s[i]] = 1
            else:
                dict_of_s[s[i]] += 1

        longest = 0
        num_odd = 0
        for x in dict_of_s.keys():
            if dict_of_s[x] % 2 == 0:
                longest += dict_of_s[x]
            else:
                num_odd += 1
                longest += (dict_of_s[x]-1)
        
        if num_odd > 0:
            longest += 1   
        return longest
    
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        len_of_g = len(g)
        len_of_s = len(s)

        num_child_content = 0
        start_cookie = 0

        for x in range(len_of_g):
            for y in range(start_cookie, len_of_s):
                if s[y] >= g[x]: 
                    num_child_content += 1
                    start_cookie = y + 1
                    break
            # if num_child_content == len_of_s:
            #     break
        return num_child_content
    
    def arrayPairSum(self, nums: List[int]) -> int:
        # The key is about how to choose pair. When you have one number, you should choose its pair as small as possible if it is bigger than itself, or it will be waist.
        # So sort original list and choose from 0 and add every two number is the final answer
        nums.sort()
        
        sum_of_nums = 0;

        for i in range(0, len(nums), 2):
            sum_of_nums += nums[i]

        return sum_of_nums