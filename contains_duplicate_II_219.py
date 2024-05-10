'''
Given an integer array nums and an integer k, return true 
if there are two distinct indices i and j in the array such that 
nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

'''

def containsNearbyDuplicates(nums, k):

    window = set()
    left = 0

    for r in range(len(nums)):

        if r - left > k:
            window.remove(nums[left])
            left += 1

        if nums[r] in window:
            return True
        
        window.add(nums[r])

    return False


nums = [1, 2, 3, 4, 5, 6, 7, 8, 8]
k = 3
print(containsNearbyDuplicates(nums, k))