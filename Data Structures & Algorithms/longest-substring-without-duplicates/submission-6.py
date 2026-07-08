class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set() #hash containing only unique elements
        l = 0
        length = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            length = max(length, r-l+1)
        return length
