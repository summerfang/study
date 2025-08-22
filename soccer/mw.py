class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
`        len_of_t = len(t)
        len_of_s = len(s)
        
        for j in range(len_of_t, len_of_s + 1):

            for i in range(len_of_s - j + 1):

                str_2_check = s[i: i + j]
                print(f"Checking substring: {str_2_check}")
                b_exist = True
                for k in range(len_of_t):
                    
                # for j in range(len_of_t):
                #     if t[j] not in str_2_check:
                #         b_exist = False
                #         break
                # if b_exist:
                #     return str_2_check

                # len_of_t += 1`

s = "ABCD"
t = "ABC"

sol = Solution()
print(sol.minWindow(s, t))