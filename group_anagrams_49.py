"""
:type strs: List[str]
:rtype: List[List[str]]

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""


def groupAnagrams(word):
        
    output = []
    dict = {}
    x = []

    for i in word:
        output.append(''.join(sorted(i)))

    for i in range(len(output)):
        if output[i] not in dict:
            dict[output[i]] = [word[i]]
        else:
            dict[output[i]].append(word[i])

    for i in dict:
        x.append(dict[i])


    

    return x




word = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(word))
word = ["a"]
print(groupAnagrams(word))
        