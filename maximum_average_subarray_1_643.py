def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float

    You are given an integer array nums consisting of n elements, and an integer k.

    Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
    Any answer with a calculation error less than 10-5 will be accepted.

    

    Example 1:

    Input: nums = [1,12,-5,-6,50,3], k = 4
    Output: 12.75000
    Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
    Example 2:

    Input: nums = [5], k = 1
    Output: 5.00000

    """
    
    current = max_array = sum(nums[:k])

    x = 0
    y = k 

    for i in range(k, len(nums)):
        current += nums[i] - nums[i - k]
        max_array = max(max_array, current)


    return max_array / k

print(findMaxAverage([4,0,4,3,3], 5))

        