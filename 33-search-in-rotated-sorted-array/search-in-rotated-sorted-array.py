class Solution:
    def search(self, nums: List[int], target: int) -> int:
        b = 0
        e = len(nums) - 1
        
        while b <= e:
            m = (b + e) // 2
            
            if nums[m] == target:
                return m
            
            # Left half is sorted
            if nums[m] > nums[e]:
                if target > nums[m]:  # Target in right half
                    b = m + 1
                elif target < nums[b]:  # Target in right half (wrapped around)
                    b = m + 1
                else:  # Target in left half
                    e = m - 1
            # Right half is sorted
            else:
                if target < nums[m]:  # Target in left half
                    e = m - 1
                elif target > nums[e]:  # Target in left half (wrapped around)
                    e = m - 1
                else:  # Target in right half
                    b = m + 1
        
        return -1