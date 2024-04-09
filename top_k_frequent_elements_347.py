"""
:type nums: List[int]
:type k: int
:rtype: List[int]

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 
"""


def topKFrequent(nums, k):
        
    output = []
    my_dict = {}

    for i in range(1, len(nums) + 1):
        my_dict[i] = []

    for num in set(nums):
        count = nums.count(num)
        my_dict[count].append(num)

    for num in range(len(my_dict), -1, -1):
        if len(output) == k:
            break
        if len(my_dict[num]) != 0:
            output.extend(my_dict[num]) 

    return output

print(topKFrequent([1,1,1,2,2,3], 2))
print(topKFrequent([5,3,1,1,1,3,5,73,1], 3))
print(topKFrequent([3,0,1,0], 1))
print(topKFrequent([1,2], 2))