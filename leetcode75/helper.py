def assert_linkedlist(list1, list2) -> bool:
    '''
    Assumes that your linkedlist uses .val to represent the node's value.
    Does the following checks for assertion:

    1. Length of both linkedlist are equal
    2. Each node in both lists have the same value at each point
    '''

    while list1 != None and list2 != None:
        if list1.val != list2.val:
            return False
        list1 = list1.next
        list2 = list2.next

    if list1 != None or list2 != None:
        return False
    
    return True
