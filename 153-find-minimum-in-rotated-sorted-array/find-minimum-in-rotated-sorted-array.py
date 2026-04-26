class Solution:
    def findMin(self, nums: List[int]) -> int:
        b=0 
        e = len(nums) -1
        mini = nums[0]
        while(b<=e):
            m= (b+e)//2
            mini = min(mini, nums[m])
            if (nums[m]>nums[e]):
                b= m+1
            else:
                e= m-1
        return mini