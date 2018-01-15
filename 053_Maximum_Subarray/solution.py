class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        max_sum = nums[0]
        current_sum = nums[0]

        for i,num in enumerate(nums):
            if i == 0:
                pass
            else:
                current_sum = max(current_sum+num,num)
                max_sum = max(current_sum,max_sum)
            
        return max_sum