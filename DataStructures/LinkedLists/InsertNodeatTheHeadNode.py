# Author - Amey Bhilegaonkar
# problem Statement - https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem

# Complete the insertNodeAtHead function below.
#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next

"""
My Solution
"""
def insertNodeAtHead(llist, data):
    # Create a new Node from data
    tempNode = SinglyLinkedListNode(data)

    # If the head is empty return Newly Created Node
    if (llist==None):
        llist = tempNode
    # Otherwise point headnode to head.next and point newly added node as Head
    else:
        new_node = tempNode
        new_node.next,llist = llist,new_node
    return llist
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')

    fptr.close()
