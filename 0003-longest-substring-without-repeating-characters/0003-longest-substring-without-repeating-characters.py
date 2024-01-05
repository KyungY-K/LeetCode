class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        used = {}
        
        for right, char in enumerate(s):
            if char in used and left <= used[char]:
                left = used[char] + 1
            else:
                max_length = max(max_length, right - left + 1)
            
            used[char] = right
        
        return max_length