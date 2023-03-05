from helper import *
from q21 import *

testcases = [
    (
        ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4, next=None))),
        ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4, next=None))),
        ListNode(val=1, next=ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=4, next=None)))))),
    ),
    (
        None,
        None,
        None
    ),
    (
        None,
        ListNode(val=0, next=None),
        ListNode(val=0, next=None)
    )
]

def test_mergeTwoLists():
    for testcase in testcases:
        assert assert_linkedlist(mergeTwoLists(testcase[0], testcase[1]), testcase[2]) == True

