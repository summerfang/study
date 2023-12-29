from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = []
        for i in range(len(nums)):
            if 0 == i:
                sums.append(nums[0])
            else:
                sums.append(nums[i] + sums[i-1])
        return sums
    

s = Solution()
print(s.runningSum([1,2,3,4]))
print(s.runningSum([1,1,1,1,1]))
print(s.runningSum([3,1,2,10,1]))