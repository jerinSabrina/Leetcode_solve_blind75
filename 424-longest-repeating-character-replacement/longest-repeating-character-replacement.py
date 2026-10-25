class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        max_win = 0
        h_map = {}

        while(r < len(s)):
            if s[r] in h_map:
                h_map[s[r]]+=1
            else:
                h_map[s[r]] = 1

            # for invalid window for exam : AABABB -> A=3, B=3 while(6-3) > 2 if k =2
            while (r-l+1) - max(h_map.values()) > k:
                h_map[s[l]] -= 1
                l +=1
            max_win = max(r-l+1, max_win)
            r+=1

        return max_win