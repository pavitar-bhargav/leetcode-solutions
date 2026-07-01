class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        obj ={}
        for i,num in enumerate (nums):
            diff= target - num
            if diff in obj:
                return [obj[diff], i]
            else :
                  obj[num]= i