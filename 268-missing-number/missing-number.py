class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n= len(nums)
        expected_sum = int(n*(n+1)/2)
        total_sum = sum(nums)
        return expected_sum - total_sum