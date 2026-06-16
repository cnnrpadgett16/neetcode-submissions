class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mySet = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in mySet:
                return [mySet[diff], i]
            mySet[n] = i

        
        