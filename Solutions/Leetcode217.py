class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        Prevvalues = {}
        for i in nums:
            if i not in Prevvalues:
                Prevvalues.update({i:0})
            else:
                return True
        return False
