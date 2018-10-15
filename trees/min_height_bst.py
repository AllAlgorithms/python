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


    def create_min_bst(self,arr,start,end):
        if end < start:
            return
        mid = (start+end) / 2
        node = Node(arr[mid])
        self.add(node.data)
        print 'adding node: ',node.data
        node.left = self.create_min_bst(arr,start,mid-1)
        node.right = self.create_min_bst(arr,mid+1,end)

    def get_height(self,node):
        if not node:
            return 0
        else:
            i = max(self.get_height(node.left),self.get_height(node.right)) + 1 
        return i

    def validate_bst(self):
        root = self.root
        diff = abs(self.get_height(root.left) - self.get_height(root.right))
        return diff

def main():
    B = BST()
    nodes = [1,2,3,4,5,6,7]
    B.create_min_bst(nodes,0,len(nodes)-1)
    B.inorder(B.root)
    
    print B.validate_bst()

if __name__ == '__main__':
    main()
