class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        alpha_s = [letter for letter in s.lower() if letter.isalnum()]
        l, r = 0, len(alpha_s) - 1
        print(alpha_s)
        while l < r:
            if alpha_s[l] == alpha_s[r]:
                r-=1
                l+=1
            else:
                return False
        return True
            
        