class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr, prev = head, None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


def make_ll(list):
    head = None
    for i in list:
        if head == None:
            head = Node(i)
        else:
            curr = head
            while curr.next:
                curr = curr.next
            curr.next = Node(i)
    return head

def make_lst(head):
    if head == None:
        return []
    else:
        lst = []
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
    return lst


lst_1 = [1,2,3,4,5]
lst_2 = [1, 2]
lst_3 = []

ll_1 = make_ll(lst_1)
ll_2 = make_ll(lst_2)
ll_3 = make_ll(lst_3)


def test_solutions():
    solution = Solution()

    lst_1.reverse()
    assert make_lst(solution.reverseList(ll_1)) == lst_1, "Should be [5, 4, 3, 2, 1]"

    lst_2.reverse()
    assert make_lst(solution.reverseList(ll_2)) == lst_2, "Should be [2, 1]"

    lst_3.reverse()
    assert make_lst(solution.reverseList(ll_3)) == lst_3, "Should be []"


if __name__ == "__main__":
    test_solutions()
    print("All tests pass!")