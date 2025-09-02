import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

@pytest.mark.parametrize("nums, expected", [
    ([1,2,3,1], True),
    ([1,2,3,4], False),
    ([1,1,1,3,3,4,3,2,4,2], True),
    ([1], False),
    ([], False),
    ([1,1], True),
])

def test_contains_duplicate(solution, nums, expected):
    assert solution.containsDuplicate(nums) == expected
