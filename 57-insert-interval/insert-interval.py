class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        M = []
        for i in range(len(intervals)):
            if(newInterval[1]<intervals[i][0]):
                M.append(newInterval)
                return M + intervals[i:]
            elif newInterval[0]>intervals[i][1]:
                M.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1],intervals[i][1])]
        M.append(newInterval)
        return M