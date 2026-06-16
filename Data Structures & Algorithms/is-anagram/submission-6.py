class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash_1, hash_2 = {}, {}

        for i in range(len(s)):
            hash_1[s[i]] = 1 + hash_1.get(s[i], 0)
            hash_2[t[i]] = 1 + hash_2.get(t[i], 0)
        
        return hash_1 == hash_2