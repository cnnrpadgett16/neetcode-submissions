class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashT = {}

        for i, num in enumerate(nums):
        
            if target - num in hashT:
                return [min(i, hashT[target - num]), max(i, hashT[target - num])]
            hashT[num] = i
        return None

             