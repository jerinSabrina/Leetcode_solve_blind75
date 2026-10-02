class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        h_map = {}

        for i in range(len(nums)):
            sub = target - nums[i]

            if sub in h_map:
                return [i,h_map[sub]]
                     
            h_map[nums[i]] = i 