# -*- coding: UTF-8 -*-
#
# Lowest Common Ancestor
# The All ▲lgorithms library for python
#
# Contributed by: Anish Narkhede
# Github: @anish03
#
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self,data):
        if not self.root:
            self.root = Node(data)
        else:
            self._add(data,self.root)

    def _add(self,data,node):
        if data <= node.data:
            if node.left:
                self._add(data,node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self._add(data,node.right)
            else:
                node.right = Node(data)

    def find(self,data):
        if self.root:
            self._find(data,self.root)
        else:
            return None

    def _find(data,node):
        if data == node.data:
            return node
        elif node.left and data <= node.data:
            return self._find(data,node.left)
        elif node.right and data > node.data:
            return self._find(data,node.right)

    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print node.data
            self.inorder(node.right)

    def get_height(self,node):
        if not node:
            return 0
        else:
            i = max(self.get_height(node.left),self.get_height(node.right)) + 1
        return i

    def find_path(self,root,path,k):
        if not root:
            return False

        path.append(root.data)

        if root.data == k:
            return True

        if (root.left and self.find_path(root.left,path,k) or root.right and self.find_path(root.right,path,k)):
            return True

        path.pop()
        return False

    def Driver(self,root,n1,n2):
        path1,path2 = [],[]

        if (not self.find_path(root,path1,n1) or not self.find_path(root,path2,n2)):
            return -1

        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i] != path2[i]:
                break
            i += 1
        return path1[i-1]

def main():

    B = BST()

    B.add(8)
    B.add(3)
    B.add(10)
    B.add(1)
    B.add(6)
    B.add(14)
    B.add(4)
    B.add(7)
    B.add(13)

    print B.Driver(B.root,1,6)

if __name__ == '__main__':
    main()
