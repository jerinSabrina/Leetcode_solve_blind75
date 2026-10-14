class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]*n


        #nums[i] = [1, 2, 3, 4]
        #ans[i]  = [1, 1, 2, 6]
        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        #nums[i] = [4,3,2,1]
        #suffix = 1*4, 4*3, 12*2, 24*1
        #ans[i] = [1*6, 4*2 , 12*1, 24*1]
        #ans[i] = [24, 12, 8, 6]
        suffix = 1
        for i in range(n-1, -1, -1):
            ans[i] *= suffix 
            suffix *= nums[i]  

        return ans