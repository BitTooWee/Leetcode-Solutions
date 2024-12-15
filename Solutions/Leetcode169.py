class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = {}
        for i in nums:
            if i in elements:
                elements.update({i:elements[i] + 1})
            else:
                elements.update({i:1})
        for i in elements:
            if elements[i] > math.floor(len(nums)/2):
                return i
