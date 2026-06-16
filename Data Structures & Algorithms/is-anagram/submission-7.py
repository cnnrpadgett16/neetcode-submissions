class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        my_dict = {}
        for letter in s:
            if letter in my_dict.keys():
                my_dict[letter] += 1
            else:
                my_dict[letter] = 1
        
        your_dict = {}
        for letter in t: 
            if letter in your_dict.keys():
                your_dict[letter] += 1
            else:
                your_dict[letter] = 1
        
        return my_dict == your_dict
            