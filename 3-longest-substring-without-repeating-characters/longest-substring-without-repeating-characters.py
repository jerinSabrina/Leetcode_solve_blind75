class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h_map = {}
        l = r = 0
        temp_len = 0

        while (l <= r and r < len(s)):
            if s[r] not in h_map:
                h_map[s[r]] = 1
            else:
                h_map[s[r]] +=1

            while(h_map[s[r]]> 1):
                h_map[s[l]] -= 1
                l+=1
            temp_len = max(temp_len, r-l +1)
            r+=1
        return temp_len

