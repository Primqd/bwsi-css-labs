"""
tests_1d.py

tests for twosum
"""

import pytest
from labs.lab_1.lab_1d import two_sum

# set to get rid of order per problem statement
def test_leetcode(): # testcases provided on LC
    assert set(two_sum([2,7,11,15], 9)) == set([0,1]) 
    assert set(two_sum([3,2,4],6)) == set([1,2]) 
    assert set(two_sum([3,3],6)) == set([0,1])

def test_other():
    assert set(two_sum([0,0],0)) == set([0,1]) # 0
    assert set(two_sum([1,2,3,5], 7)) == set([1,3])
    assert set(two_sum([-1,5,3], 2)) == set([0,2])
    assert set(two_sum([10,1,2,3], 5)) == set([2,3])
    assert set(two_sum([100,200], 300)) == set([0,1])
    assert set(two_sum([i for i in range(1001)], 1999)) == set([999, 1000])
    

if __name__ == "__main__":
    pytest.main()