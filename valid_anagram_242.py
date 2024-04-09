"""
:type s: str
:type t: str
:rtype: bool

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

def isAnagram(s, t):

    my_dicts = {}
    my_dictt = {}


    for letter in s:
        if letter not in my_dicts:
            my_dicts[letter] = 1
        else:
            my_dicts[letter] += 1

    for letter in t:
        if letter not in my_dictt:
            my_dictt[letter] = 1
        else:
            my_dictt[letter] += 1

    
    return my_dicts == my_dictt



print(isAnagram("people", "people"))




        