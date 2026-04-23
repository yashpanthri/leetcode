from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Using defaultdict(list) removes the need for 'if key in answer' checks
        groups = defaultdict(list)
        
        for s in strs:
            # Create a character count array for 'a' through 'z'
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # Use the tuple version of the count as the dictionary key
            groups[tuple(count)].append(s)
            
        # Returning all the values in the dictionary as a list of lists
        return list(groups.values())