

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
        #if the Linked List is Empty
        if self.head is None:
            self.head = new_node
            return
        #if the linked list is Not Empty
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):

        cur_node = self.head

        if cur_node and cur_node.data == key:
            cur_node.next = self.head
            cur_node = None
            return

        Prev = None
        while cur_node and cur_node.data != key:
            Prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        Prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):

        if self.head:
            cur_node = self.head
            if pos == 0:
                cur_node = cur_node.next
                cur_node = None
                return


        Prev = None
        count = 0
        while cur_node and count != pos:
            Prev = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return

        Prev.next = cur_node.next
        cur_node = None

    def len_iterative(self):
        cur_node = self.head
        length = 0
        while cur_node:
            length += 1
            cur_node = cur_node.next

        return length

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap(self, key1, key2):
        if key1 == key2:
            return

        prev_1 = None
        cur_node1 = self.head
        while cur_node1 and cur_node1.data != key1:
            prev_1 = cur_node1
            cur_node1 = cur_node1.next

        prev_2 = None
        cur_node2 = self.head
        while cur_node2 and cur_node2.data != key2:
            prev_2 = cur_node2
            cur_node2 = cur_node2

        if not cur_node1 or not cur_node2:
            return

        # Case for head nodes:
        if prev_1:
            prev_1.next = cur_node2
        else:
            self.head = cur_node2

        if prev_2:
            prev_2.next = cur_node1
        else:
            self.head = cur_node1

        cur_node1.next, cur_node2.next = cur_node2.next, cur_node1.next

    def reverse_iterative(self):
        prev = None
        cur_node = self.head
        while cur_node:
            nxt = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node =nxt

        self.head = prev

    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):

            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(self.head, None)

    def merge_two_sorted_arrays(self, llist):

        p = self.head
        s = None
        q = llist.head

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next

        new_head = s

        while p or q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s = q
        else:
            s = p

        self.head = new_head
        return self.head

    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_dict = dict()

        while cur:

            if cur.data in dup_dict:
                prev.next = cur.next
                cur = None
            else:
                dup_dict[cur.data] = 1
                prev = cur
            cur = prev.next

    def N_to_last(self, n):
        total_len = self.len_iterative()

        cur = self.head
        while cur:

            if total_len == n:
                print(cur.data)
                return cur.data
            total_len -= 1
            cur = cur.next

        if cur == None:
            return

    def count_occurences(self, data):
        cur = self.head
        count = 0
        while cur:
            if cur.data == data:
                count += 1

            cur = cur.next

        return count

    def rotate(self, pivot):

        p = self.head
        q= self.head
        prev = None
        counter = 0
        while p and count < pivot:
            prev = p
            p = p.next
            q = q.next
            counter += 1

        p = prev
        while q:
            prev = q
            q = q.next

        q = prev

        q.next = self.head
        self.head = p.next
        p.next = None

    def sum_two_lists_mine(self, llist):

            if not self.head:
                return llist

            if not llist.head:
                return self

            llist1 = self.head
            llist2 = llist.head

            multiplier = 1
            product1 = 0
            while llist1:
                product1 += llist1.data * multiplier
                multiplier *= 10
                llist1 = llist1.next

            multiplier = 1
            product2 = 0
            while llist2:
                product2 += llist2.data * multiplier
                multiplier *= 10
                llist2 = llist2.next

            print(multiplier)
            sums = product1 + product2
            divider = sums
            result = LinkedList()

            while divider // 10 != 0:
                remainder = divider % 10
                result.append(remainder)
                divider = divider // 10

            node = Node(divider)
            result.append(divider)

            # node.next = result.head
            # result.head = node

            return result

    def sum_two_lists(self, llist):
        p = self.head
        q = llist.head
        sumllist = LinkedList()
        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data

            if not q:
                j = 0
            else:
                j = q.data

            sum = i + j + carry
            if sum >= 10:
                carry = 1
                remainder = sum % 10
                sumllist.append(remainder)
            else:
                carry = 0
                sumllist.append(remainder)

            if p:
                p = p.next
            if q:
                q = q.next

        return sumllist





llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)

llist.rotate(4)
llist.print_list()





# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")
# llist.prepend("E")


#llist.print_list()
