class Solution:
    def isPalindrome(self, x: int) -> bool:
        rn = 0
        temp = abs(x)
        while not (temp==0):
            d = temp%10
            temp=temp//10
            rn = rn*10+d
        if rn == x:
            return True
        else:
            return False