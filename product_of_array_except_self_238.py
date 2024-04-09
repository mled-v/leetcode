"""
    :type nums: List[int]
    :rtype: List[int]

    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the division operation.

    

    Example 1:

    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]
    Example 2:

    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]
    """

def productExceptSelf(nums):
    
    # output = [1] * len(nums)
    
    # count = 0


    # for i in range(len(nums)):
    #     left = 1
    #     right = 1

    #     #calculate left
    #     for i in range(0, count):
    #         left = nums[i] * left


    #     #calculate right
    #     for i in range(count + 1,len(nums)):
    #         right = nums[i] * right

    #     output[count] = left * right

    #     count += 1


    output = []

    prefix = [1]
    suffix = [1]
    count = 0

    for i in range(len(nums) - 1):
        ans = nums[i] * prefix[i]
        prefix.append(ans)

    
    for i in range(len(nums) - 1, 0, -1):
        ans = nums[i] * suffix[count]
        suffix.append(ans)
        count += 1

    
    suffix.reverse()

    for i in range(len(nums)):
        ans = prefix[i] * suffix[i]
        output.append(ans)


    return output

print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))