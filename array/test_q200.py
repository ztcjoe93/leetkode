from q200 import *

testcases = [ 
    ([["1","1","1","1","0"], ["1","1","0","1","0"], ["1","1","0","0","0"], ["0","0","0","0","0"]], 1),
    ([["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"]], 3)
]

def test_numIslands():
    for testcase in testcases:
        assert numIslands(testcase[0]) == testcase[1]
