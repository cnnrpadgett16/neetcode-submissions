class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
 
        hash1 = {}


        for i, value in enumerate(nums): 
            if target - value in hash1.keys():
                return [hash1[target - value], i]
            else:
                hash1[value] = i
        


        

