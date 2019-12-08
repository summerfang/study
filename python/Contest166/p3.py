class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """

        min_division = 1
        max_division = max(nums)

        divisor = max_division

        while divisor <= max_division:
            sum_of_nums = 0
            for x in nums:
                division = 1 if x <= divisor else x // divisor if x % divisor == 0 else x // divisor + 1          
                sum_of_nums = sum_of_nums + division
    
            if sum_of_nums > threshold:
                min_division = divisor
                divisor = (max_division + min_division) // 2

                sum_of_nums = 0
                for x in nums:
                    division = 1 if x <= divisor else x // divisor if x % divisor == 0 else x // divisor + 1          
                    sum_of_nums = sum_of_nums + division

            else:
                max_division = divisor
                divisor = (max_division + min_division) // 2

        return divisor

a = Solution()
print(a.smallestDivisor([1,2,5,9], 6))
print(a.smallestDivisor([2,3,5,7,11],11))
print(a.smallestDivisor([19], 5))