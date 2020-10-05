"""
    This is an efficient algorithm to find the size of a subtree from every node in O(n) time.
    The idea is to use one dfs and first calculate the size of subtree of children of a node recursively.
    Then add the size of each subtree of its children to get the size of its subtree.
"""
from collections import defaultdict as dd


def dfs(source, parent):
    # Initial size of root is 1
    size[source] = 1
    for child in graph[source]:
        if child != parent:
            # Recursively calculate size of subtree of children nodes
            dfs(child, source)
            # Adding size of each child's subtree.
            size[source] += size[child]


size = dd(int)
graph = dd(set)
n = int(input())
for i in range(n-1):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)
dfs(1, 0)
print(size)
