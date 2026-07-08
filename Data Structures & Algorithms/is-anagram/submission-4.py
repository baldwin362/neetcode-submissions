class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hash_s = {}
        hash_t = {}
        for i in range(len(t)):
            if t[i] not in hash_t:
                hash_t[t[i]]=0
            if s[i] not in hash_s: 
                hash_s[s[i]]=0
            hash_t[t[i]]+=1
            hash_s[s[i]]+=1
        for i in range(len(s)):
            if s[i] not in hash_t:
                return False
            if hash_s[s[i]]!=hash_t[s[i]]:
                return False
        return True
