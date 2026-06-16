class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        table1, table2 = {}, {}

        for i in range(len(s)):
            table1[s[i]] = 1 + table1.get(s[i], 0)
            table2[t[i]] = 1 + table2.get(t[i], 0)

        return table1 == table2
        