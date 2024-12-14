class Solution(object):
    def merge(self, intervals):
        amount_reduced = 0
        intervals.sort()
        for n in range(0,len(intervals)-1):
            i = n - amount_reduced
            if intervals[i][1] >= intervals[i+1][0]:
                if intervals[i][1] < intervals[i+1][1]:
                    intervals[i:i+2] = [[intervals[i][0],intervals[i+1][1]]]
                else:
                    intervals[i:i+2] = [[intervals[i][0],intervals[i][1]]]
                amount_reduced += 1
        return intervals
