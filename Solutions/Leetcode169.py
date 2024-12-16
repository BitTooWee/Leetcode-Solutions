class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        currentCandidate = None
        sumCandidate = 1
        for i in nums:
            if i == currentCandidate:
                sumCandidate += 1
            else:
                sumCandidate -= 1
                if sumCandidate == 0:
                    currentCandidate = i
                    sumCandidate = 1
        return currentCandidate
