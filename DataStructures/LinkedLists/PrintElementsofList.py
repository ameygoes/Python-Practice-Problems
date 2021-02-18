# Author - Amey Bhilegaonkar
# Problem Statement Link - https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem

# Complete the printLinkedList function below.
#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next

"""
My Solution function
"""
def printLinkedList(head):
    while(head!=None):
        print(head.data)
        head = head.next

if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    printLinkedList(llist.head)
