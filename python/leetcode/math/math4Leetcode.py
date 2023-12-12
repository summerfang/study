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
        pass