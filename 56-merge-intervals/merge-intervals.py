class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        M = []
        for i in range(len(intervals)):
            if (len(M)==0 or M[-1][1]<intervals[i][0]):
                M.append(intervals[i])
            else:
                M[-1][1]=max(M[-1][1], intervals[i][1])
        return M