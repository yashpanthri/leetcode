class Solution:
    def search(self, nums: List[int], target: int) -> int:
        b=0
        e = len(nums)-1
        while(b<=e):
            m=(b+e)//2
            if nums[m] > target:
                e=m-1
            elif nums[m]<target:
                b=m+1
            else:
                return m
        return -1