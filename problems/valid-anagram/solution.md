# 💡 Solution: Valid Anagram

## Approach 1: Hash Map

I thought about using a dictionary to count occurrences of each character in `s`, then decrement counts while iterating through `t`. If any character in `t` is missing or overused, the strings are not anagrams.

- **Idea:** Count how many times each character appears in `s` using a dictionary, then check if `t` has exactly the same characters with the same counts.

- **Steps:**
  1. if `s` and `t` have different lengths, return `False`.
  2. Create a dictionary `letters` to store counts of each character in `s`.
  3. Iterate through `s`, incrementing the count of each character in `letters`.
  4. Iterate through `t`, if a character is missing or its count is zero, return `False`.
  5. If all characters in `t` pass the check, return `True`
- **Code:** 
    ```python
    class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = {}
        for char in s:
            letters[char] = letters.get(char, 0) + 1

        for char in t:
            if letters.get(char, 0) == 0:
                return False
            letters[char] -= 1

        return True
    ```
- **Complexity:**
  - Time: **O(n)**
  - Space: **O(1)**
