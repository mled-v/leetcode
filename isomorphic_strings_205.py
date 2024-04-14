"""
:type s: str
:type t: str
:rtype: bool

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character 
while preserving the order of characters. No two characters may map to the same character,
but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true

"""

from collections import defaultdict 


def isIsomorphic(s, t):

    s_dict = {}
    d_dict = {}


    i = 0
    for letter in s:
        if letter not in s_dict:
            s_dict[letter] = [t[i]]
        else:
            s_dict[letter].append(t[i])
        i+=1

    j = 0
    for letter in t:
        if letter not in d_dict:
            d_dict[letter] = [s[j]]
        else:
            d_dict[letter].append(s[j])
        j+=1

    print(s_dict)
    print(d_dict)

    flag = 0

    for v in s_dict.values():
        if len(set(v)) > 1: 
            flag +=1
    
    for v in d_dict.values():
        if len(set(v)) > 1:
            flag+=1

    if flag == 2:
        return False
    
    return True

print(isIsomorphic("badc", "baba"))