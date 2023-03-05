from typing import Optional

# https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    '''
    Some scenarios to consider here:
    
    1. Either node-list is empty
    We will return the other node-list as there's no need to do comparison -- i.e other list is the already arranged.
    
    2. Length of both node-lists are not the same
    We will reach the end of a list first, thereafter it should link to the rest of the other list.
    
    Do a comparison to start from the lower value of the 2 lists.
    Move node to next linked node if it's linked.
    '''
    
    if list1 == None:
        return list2
    elif list2 == None:
        return list1

    dummy = ListNode()
    
    if list1.val <= list2.val:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next
        
    dummy.next = head
    
    while list1 != None and list2 != None:
        if list1.val <= list2.val:
            head.next = list1
            list1 = list1.next
        else:
            head.next = list2
            list2 = list2.next
        head = head.next
        
    if list1 != None:
        head.next = list1
    elif list2 != None:
        head.next = list2
        
    return dummy.next
