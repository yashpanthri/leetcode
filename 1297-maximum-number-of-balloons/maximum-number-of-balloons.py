class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = [0]*26
        for i in range(len(text)):
            count[ord(text[i])-ord('a')] += 1
        return min(count[0], count[1], count[11]//2, count[13], count[14]//2)