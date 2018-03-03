class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        longest_LIS = [0] * len(nums)
        
        for i in range(len(nums)):
            longest_LIS[i] += 1
            longest_prev_LIS = 0
            for j in range(0, i):
                if nums[j] < nums[i] and longest_LIS[j] > longest_prev_LIS:
                    longest_prev_LIS = longest_LIS[j]
            longest_LIS[i] += longest_prev_LIS
                    
                    
        return max(longest_LIS)