"""
:type nums: List[int]
:type target: int
:rtype: int

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

"""

def search(nums, target):
    
    output = -1

    left = 0
    right = len(nums) - 1
    middle = (left + right) // 2

    while left <= right:
        if nums[middle] == target:
            return middle
        if nums[middle] < target:
            left = middle + 1
            middle = (left + right) // 2
        else:
            right = middle - 1
            middle = (left + right) // 2
    return output
    

list = [5]
print(search(list, 5))


