from q1480 import *

testcases = [
    ([1,2,3,4],[1,3,6,10]),
    ([1,1,1,1,1],[1,2,3,4,5]),
    ([3,1,2,10,1],[3,4,6,16,17])
]

def test_runningSum():
    for testcase in testcases:
        assert runningSum(testcase[0]) == testcase[1]
