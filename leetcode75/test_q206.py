from q206 import *
from helper import *

testcases = [
    (ListNode(val=1,next=ListNode(val=2,next=ListNode(val=3,next=ListNode(val=4,next=ListNode(val=5,next=None))))), ListNode(val=5,next=ListNode(val=4,next=ListNode(val=3,next=ListNode(val=2,next=ListNode(val=1,next=None)))))),
    (ListNode(val=1, next=ListNode(val=2, next=None)), ListNode(val=2, next=ListNode(val=1, next=None))),
    (None, None)
]

def test_reverseList():
    for testcase in testcases:
        assert assert_linkedlist(reverseList(testcase[0]), testcase[1]) == True
