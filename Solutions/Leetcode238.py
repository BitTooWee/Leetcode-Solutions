class Solution(object):
    def productExceptSelf(self, nums):
        prod = 1
        exists_zero = 1
        zero_amount = 0
        for i in nums:
            if i != 0:
                prod = prod * i
            else:
                exists_zero = 0
                zero_amount += 1
                if zero_amount > 1:
                    prod = 0
        result = []
        for i in nums:
            if i != 0:
                result.append(int(prod*exists_zero*(i**(-1))))
            else:
                result.append(int(prod))
        return result
        
