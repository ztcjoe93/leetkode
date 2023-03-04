from q205 import *

testcases = [
    ("egg", "add", True),
    ("foo", "bar", False),
    ("paper", "title", True),
    ("baba", "badc", False)
]

def test_isIsomorphic():
    for testcase in testcases:
        assert isIsomorphic(testcase[0], testcase[1]) == testcase[2]
