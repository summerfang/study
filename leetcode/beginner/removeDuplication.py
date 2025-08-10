class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        unique_numbers = 0
        result = []

        if len(nums) == 0:
            return (unique_numbers, result)

        unique_numbers += 1
        result.append(nums[0])
        start = nums[0]
        for x in nums[1:]:
            if x != start:
                result.append(x)
                unique_numbers += 1
                start = x

        for y in range(len(result)):
            nums[y] = result[y]

        for y in range(len(nums) - unique_numbers):
            nums.append('_')            
                
        return unique_numbers
    
s = Solution()
s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])