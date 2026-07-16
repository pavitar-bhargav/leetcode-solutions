class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        oxford = {}
        for i in range(len(numbers)):
            num = numbers[i]
            diff = target - num
            if diff in oxford:
                return [oxford[diff] , i+1]
            else:
                oxford[num] = i+1

                
        