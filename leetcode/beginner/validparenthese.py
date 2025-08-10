class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
                continue

            if c == ')':
                if(len(stack) > 0 and stack[-1] == '('):
                    stack.pop()
                else:
                    return False
            if c == ']':
                if(len(stack) > 0 and stack[-1] == '['):
                    stack.pop()
                else:
                    return False
            if c == '}':
                if(len(stack) > 0 and stack[-1] == '{'):
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
    
if __name__ == "__main__":
       s = Solution()
       print(s.isValid("([])"))  # True
       print(s.isValid("()[]{}"))  # True
       print(s.isValid("(]"))  # False
       print(s.isValid("([)]"))  # False
       print(s.isValid("{[]}"))  # True