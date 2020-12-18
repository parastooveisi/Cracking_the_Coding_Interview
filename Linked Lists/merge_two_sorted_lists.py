class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def merge_lists(self, llist):
        temp = dummy = LinkedList()
        l1 = llist.head
        l2 = self.head
        while l1 and l2:
            if l1.data <= l2.data:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 or l2

        return dummy.next


llist1 = LinkedList()
llist1.append(1)
llist1.append(5)
llist1.append(7)
llist1.append(9)
llist1.append(10)

llist2 = LinkedList()
llist2.append(2)
llist2.append(3)
llist2.append(4)
llist2.append(6)
llist2.append(8)

llist1.merge_lists(llist2)
llist1.print_list()
