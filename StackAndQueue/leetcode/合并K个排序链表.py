class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        header = ListNode(-1)
        prev = header
        lists = [ln for ln in lists if ln is not None]

        while len(lists) > 0:
            min_index = 0
            for i in range(len(lists)):
                if lists[min_index].val > lists[i].val:
                    min_index = i
            header.next = lists[min_index]
            header = header.next
            lists[min_index] = lists[min_index].next
            lists = [ln for ln in lists if ln is not None]
        return prev.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    l3 = ListNode(2)
    l3.next = ListNode(6)

    print(Solution().mergeKLists([None, None]))

