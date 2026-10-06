class Solution(object):
    def maxSubArray(self, nums):
       
        maxsum = nums[0]
        currentsum = 0

        for num in nums:
            currentsum = currentsum + num 


            if currentsum > maxsum:
                maxsum = currentsum


            if currentsum < 0:
                    currentsum = 0

        return maxsum 
                   
