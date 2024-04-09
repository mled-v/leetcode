'''
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
'''

def uniqueOccurrences(arr):

    my_dict = dict.fromkeys(arr,0)
    my_list = []
 

    for i in arr:
        if i in my_dict.keys():
            my_dict[i] += 1


    for k,v in my_dict.items():
        my_list.append(v)

    

    return len(arr) != len(set(my_list))

    

print(uniqueOccurrences([1,2,2,1,1,3]))