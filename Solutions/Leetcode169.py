class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        currentCandidate = nums[0]
        sumCandidate = 1
        for i in range(1,len(nums)):
            if nums[i] == currentCandidate:
                sumCandidate += 1
            else:
                sumCandidate -= 1
                if sumCandidate == 0:
                    currentCandidate = nums[i]
                    sumCandidate = 1
        return currentCandidate
