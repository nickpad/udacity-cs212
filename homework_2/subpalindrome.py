# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

import itertools

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    if len(text) <= 1: return (0, len(text))

    text = text.lower()

    letter_map = {}
    candidates = []

    for i, key in enumerate(text):
        value = letter_map.get(key, [])
        value.append(i)
        letter_map[key] = value

    for key in letter_map:
        indices = letter_map[key]
        if len(indices) >= 2:
            for x, y in itertools.combinations(indices, 2):
                length = (y - x) + 1
                candidates.append((length, x, y + 1))

    candidates.sort(reverse=True)

    for _, start, end in candidates:
        candidate = text[start:end]
        if candidate == candidate[::-1]: return (start, end)

def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8, 21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print(test())