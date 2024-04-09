"""
:type nums: List[int]
:rtype: int
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

"""

def longestConsecutive(nums):
        
    count = 1
    curr_count = 1
    nums.sort()

    if len(nums) == 0:
        return 0
    
    for i in range(len(nums) - 1):
        


        if nums[i] != nums[i + 1]:
            if nums[i] == nums[i + 1] - 1:
                curr_count += 1
            else:
                count = max(count, curr_count)
                curr_count = 1
                



    return max(count, curr_count)


#1,2,3,4,100,200


nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))
