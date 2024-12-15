class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numcopy = nums.copy()
        nums.sort()
        frontindex = 0
        endindex = len(nums) - 1
        while nums[frontindex] + nums[endindex] != target:
            if nums[frontindex] + nums[endindex] < target:
                frontindex += 1
            elif nums[frontindex] + nums[endindex] > target:
                endindex -= 1
        FrontFound = False
        EndFound = False
        for i in range(0,len(numcopy)):
            if numcopy[i] == nums[frontindex] and not FrontFound:
                frontindex = i
                FrontFound = True
            elif numcopy[i] == nums[endindex] and not EndFound:
                endindex = i
                EndFound = True
        return [frontindex, endindex]
