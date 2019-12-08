class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        product_sum = 1
        sum_sum = 0
        sn = str(n)
        if len(sn) == 1:
            return 0
        for x in sn:
            product_sum = product_sum * int(x)
            sum_sum = sum_sum + int(x)
        return product_sum - sum_sum

a = Solution()
print(a.subtractProductAndSum(234))
print(a.subtractProductAndSum(4421))