def merge_sort(l):
    if len(l) < 2: return
    pivot = len(l)//2
    left, right = l[:pivot], l[pivot:]
    merge_sort(left)
    merge_sort(right)

    k = 0
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            l[k] = left.pop(0)
        else:
            l[k] = right.pop(0)
        k += 1

    rest = left + right
    while len(rest) > 0:
        l[k] = rest.pop(0)
        k += 1

