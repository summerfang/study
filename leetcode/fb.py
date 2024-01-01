class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        s = []
        for i in range(1, n + 1):
            b_3 = i % 3 == 0
            b_5 = i % 5 == 0

            if b_3 and b_5:
                s.append("FizzBuzz")
                continue
            
            if b_3:
                s.append("Fizz")
                continue
            
            if b_5:
                s.append("Buzz")
                continue
            
            s.append(str(i))

        return s

    

if __name__ == "__main__":
    s = Solution()
    print(s.fizzBuzz(3))