class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = 1
        prod_pre = [1]*len(nums)
        prod_post = [1]*len(nums)
        for i in range(len(nums)):
            prod_pre[i] = nums[i] * pro
            pro = prod_pre[i]
        pro = 1
        for i in range(len(nums)-1, -1, -1):
            prod_post[i] =  pro * nums[i]
            pro = prod_post[i]

        answer=[]
        for i in range(len(nums)):
            if i == 0:
                answer.append(prod_post[i+1])
            elif i == len(nums)-1:
                answer.append(prod_pre[i-1])
            else:
                answer.append(prod_post[i+1]*prod_pre[i-1])
        
        return answer