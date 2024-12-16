class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currentsum = 0
        for i in range(0, k):
            currentsum += nums[i]
        maxsum = currentsum
        for i in range(k, len(nums)):
            currentsum -= nums[i-k]
            currentsum += nums[i]
            if currentsum > maxsum:
                maxsum = currentsum
        return maxsum / k
