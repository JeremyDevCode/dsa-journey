# 💡 Solution: Contains Duplicate

## Approach 1: Brute Force (if applicable)

At first, I thought about using a set, but I like to start with the simplest solution I can think about, so I decided to try with `brute force` approach.

- **Idea:** I can iterate over `nums` and use a dictionary to save the elements. If I find a `num` that already exists in the dictionary, I return `True`. Otherwise I return `False`.

- **Steps:**
  1. Create a variable `saved_values` to store the previous values.
  2. Iterate over `nums` using a `for` loop.
  3. Check if the current value exists in `saved_values`. If it does, return `True`. Otherwise add it to `saved_values`
- **Code:** 
    ```python
    class Solution:
        def containsDuplicate(self, nums: List[int]) -> bool:
            saved_values = {}

            for num in nums:
                if num in saved_values:
                    return True
                saved_values[num] = True
            return False
    ```
- **Complexity:**
  - Time: **O(n)**
  - Space: **O(n)**
- **Why it’s not optimal:** Even though this solution works and passed all the tests, I want to try an implementation using set structure, because dictionaries store values in addition to keys, so in this case we use a bit more memory. A set is a better approach because it's designed specifically to store unique elements.

---

## Approach 2: Optimized (Preferred)
- **Idea:** We can use a set from the list, and compare the length of the original list and the length of our set. If there is a difference, it means there is at least one duplicate.
- **Steps:**
  1. Create a set from the list `nums`.
  2. Compare the length of the list and the length of the set.
  3. Return `False` if the lengths are equal, otherwise return `True`
- **Code:**

```python
    class Solution:
        def containsDuplicate(self, nums: List[int]) -> bool:
            if len(nums) == len(set(nums)):
                return False
            return True
```
- **Complexity:**
  - Time: **O(n)**
  - Space: **O(n)**