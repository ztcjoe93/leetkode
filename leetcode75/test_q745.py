from q745 import *

testcases = [
    ([1,7,3,6,5,6],3),
    ([1,2,3],-1),
    ([2,1,-1],0)
]

def test_pivotIndex():
    for testcase in testcases:
        assert pivotIndex(testcase[0]) == testcase[1]
