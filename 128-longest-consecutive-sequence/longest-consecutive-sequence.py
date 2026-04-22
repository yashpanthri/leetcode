class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for num in nums_set:
            if (num-1) in nums_set:
                continue
            else:
                length = 0
                curr = num
                while curr in nums_set:
                    length+=1
                    curr+=1
                if longest<length:
                    longest = length
        return longest