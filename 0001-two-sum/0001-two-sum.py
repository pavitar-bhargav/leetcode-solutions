class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        oxford = {}
        for index in range(len(nums)):
            num1 = nums[index]  
            num2 = target - num1  # needed number , or difference 

            if num2 in oxford:
                num2_index = oxford[num2]
                return [num2_index, index]

            oxford[num1] = index



                








        

            
            
            

        
                
        

                


            