class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)      
        print(numset) 
        count = 0
        for i in numset:
            if (i - 1) not in numset:
                length = 1
                while (i+length) in numset:
                    length += 1
                count = max(length, count)
                print (count)

        return count