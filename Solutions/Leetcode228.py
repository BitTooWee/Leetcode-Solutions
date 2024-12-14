class Solution(object):
    def summaryRanges(self, nums):
        ranges = []
        if len(nums) > 0:
            currentLow = nums[0]
            currentHigh = nums[0]
            if len(nums) > 1:
                for i in range(0,len(nums)-1):
                    if nums[i] == nums[i+1] - 1:
                        currentHigh = nums[i+1]
                        if i == len(nums) - 2:
                            ranges.append([currentLow,currentHigh])
                    else:
                        ranges.append([currentLow,currentHigh])
                        currentLow = nums[i+1]
                        currentHigh = nums[i+1]
                        if i == len(nums) - 2:
                            ranges.append([nums[-1],nums[-1]])
            else:
                ranges = [[nums[0],nums[0]]]
            results = []
            for i in ranges:
                if i[0] == i[1]:
                    results.append(str(i[0]))
                else:
                    results.append(str(i[0]) + "->" + str(i[1]))
            return results
        else:
            return []
