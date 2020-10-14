def is_palindrome(head):
    if not head:
        return True
    fast, slow = head.next, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    second = slow.next
    node = None
    while second:
        nxt = second.next
        second.next = node
        node = second
        second = nxt
    while node:
        if node.val != head.val:
            return False
        node = node.next
        head = head.next
    return True


def is_palindrome_stack(head):
    if not head or not head.next:
        return True

    # Get the midpoint
    slow = fast = cur = head
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

    # Push the second half into the stack
    stack = [slow.val]
    while slow.next:
        slow = slow.next
        stack.append(slow.val)

    # Comparison
    while stack:
        if stack.pop() != cur.val:
            return False
        cur = cur.next

    return True


def is_palindrome_dict(head):
    if not head or not head.next:
        return True
    d = {}
    pos = 0
    while head:
        if head.val in d.keys():
            d[head.val].append(pos)
        else:
            d[head.val] = [pos]
        head = head.next
        pos += 1
    checksum = pos - 1
    middle = 0
    for v in d.values():
        if len(v) % 2 != 0:
            middle += 1
        else:
            step = 0
            for i in range(0, len(v)):
                if v[i] + v[len(v) - 1 - step] != checksum:
                    return False
                step += 1
        if middle > 1:
            return False
    return True
