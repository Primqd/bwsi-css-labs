"""
tests_1c.py

tests for maximum subarray
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_leetcode(): # testcases provided on LC
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert max_subarray_sum([1]) == 1
    assert max_subarray_sum([5, 4, -1, 7, 8]) == 23

def test_other(): # testcases from own thinking
    assert max_subarray_sum([-1,-1,-1,-1,-1]) == -1 # don't expand
    assert max_subarray_sum([1 for _ in range(1_000_000)]) == 1_000_000 # arbitrarily large n, ok not that large but i don't want it take half an hour
    assert max_subarray_sum([5, -1, -1, -1, -1, 9999]) == 10_000

if __name__ == "__main__":
    pytest.main()