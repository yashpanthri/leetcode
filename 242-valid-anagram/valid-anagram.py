class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arrs = [0]*26
        arrt = [0]*26
        for i in s:
            arrs[ord(i)-ord('a')] += 1
        for i in t:
            arrt[ord(i)-ord('a')] += 1
        if (arrs == arrt):
            return True
        else:
            return False