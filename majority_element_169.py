'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
 You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

'''

def majorityElement(self, nums: List[int]) -> int:
        
        my_dict = {}

        for i in range(len(nums)):
            if nums[i] not in my_dict:
                my_dict[nums[i]] = 1
            else:
                my_dict[nums[i]] += 1

        max_value = 0
        max_key = 0
        for k, v in my_dict.items():
            if my_dict[k] > max_value:
                max_value = my_dict[k]
                max_key = k


        return max_key
