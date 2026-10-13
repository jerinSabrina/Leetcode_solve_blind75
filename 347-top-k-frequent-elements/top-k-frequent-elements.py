class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h_map = {}

        for i in range(len(nums)):
            if nums[i] not in h_map:
                for j in range(i, len(nums)): 
                    if nums[i] == nums[j]:
                        if nums[i] not in h_map:
                            h_map[nums[i]] = 1
                        else:
                            h_map[nums[i]] += 1

        sorted_dict = dict(sorted(h_map.items(), key=lambda item: item[1], reverse=True))

        return list(sorted_dict.keys())[:k]