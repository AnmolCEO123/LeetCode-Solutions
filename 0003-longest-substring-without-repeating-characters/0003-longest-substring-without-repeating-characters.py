class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = set()
        first = 0
        max_len = 0
        
        for second in range(len(s)):
            while s[second] in seen:
                seen.remove(s[first])
                first += 1
            seen.add(s[second])
            max_len = max(max_len, second - first + 1)
            
        return max_len