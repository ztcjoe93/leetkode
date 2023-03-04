from q392 import *

testcases = [
    ("abc", "ahbgdc", True),
    ("", "ahbgdc", True),
    ("axc", "ahbgdc", False)
]

def test_isSubsequence():
    for testcase in testcases:
        assert isSubsequence(testcase[0], testcase[1]) == testcase[2]
