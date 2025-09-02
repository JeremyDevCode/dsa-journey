import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

@pytest.mark.parametrize("s, t, expected", [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("listen", "silent", True),
    ("a", "a", True),
    ("ab", "ba", True),
    ("abc", "def", False),
    ("", "", True),
    ("a", "ab", False),
    ("ab", "a", False),
])

def test_is_anagram(solution, s, t, expected):
    assert solution.isAnagram(s, t) == expected
