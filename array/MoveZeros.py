# Move Zeroes

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = 0
        j = 1
        
        while j < len(nums):
            if nums[i] == 0 and nums[j] == 0:
                j+=1
                
            elif nums[i] != 0 and nums[j] !=0:
                i+=1
                j+=1
                
            elif nums[i] == 0 and nums[j]!=0:
                nums[j],nums[i] = nums[i],nums[j]
                i+=1
                j+=1    
                
            elif nums[i]!=0 and nums[j] == 0:
                i+=1
                j+=1
        return nums