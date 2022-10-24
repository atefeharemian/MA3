""" bst.py

Student:
Mail:
Reviewed by:
Date reviewed:
"""


import math
import random
from linked_list import LinkedList


class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Dicussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#
# height of the tree

    def _height(self, r):
        if r is None:
            return 0
        else:
            return 1 + max(self._height(r.left), self._height(r.right))

    def height(self):
        if self.root is None:
            return 0
        if self.root.left is None and self.root.right is None:
            return 1
        return self._height(self.root)

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _find_min(self, r):
        if r.left is None:
            return r.key
        else:
            return self._find_min(r.left)

    def _remove(self, r, k):                      # Compulsory
        if r is None:
            return None
        elif k < r.key:
            # r.left = left subtree with k removed
            r.left = self._remove(r.left, k)

        elif k > r.key:
            # r.right =  right subtree with k removed
            r.right = self._remove(r.right, k)
        else:  # This is the key to be removed
            if r.left is None:     # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:  # This is the tricky case.
                # Find the smallest key in the right subtree
                # Put that key in this node
                # Remove that key from the right subtree
                r.key = self._find_min(r.right)
                r.right = self._remove(r.right, r.key)
        return r  # Remember this! It applies to some of the cases above
# __str__ function using generator

    def __str__(self):
        if self.root is None:
            return '<>'
        return '<' + ', '.join(str(x) for x in self) + '>'
    # to_list function to trnsform the tree into a list

    def to_list(self):
        if self.root is None:
            return []
        return [x for x in self]
    # to_linked_list function to transform the tree into a linked list

    def to_LinkedList(self):
        if self.root is None:
            return LinkedList()
        else:
            l = LinkedList()
            for x in self:
                l.insert(x)
            return l

    # calculate the internal path length of the tree (sum of all nodes' level)
    def ipl(self):
        return self._ipl(self.root, 1)

    def _ipl(self, r, level):
        if r is None:
            return 0
        else:
            return level + self._ipl(r.left, level + 1) + self._ipl(r.right, level + 1)


def random_tree(n):                               # Useful
    bst = BST()
    while n > 0:
        bst.insert(random.random())
        n -= 1
    return bst


def main():
    t = BST()
    # t.insert(5)
    print("sdfscqqdszz", t.ipl())
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    t.print()
    print()

    print('size  : ', t.size())
    for k in [0, 1, 2, 5, 9]:
        print(f"contains({k}): {t.contains(k)}")
    t.print()

    print("sdsdf", t.ipl())

    n = 5000
    bst1 = random_tree(n)
    print("For n=", n)
    print("IPL/n is :", bst1.ipl()/n)
    print("the height is :", bst1.height())
    n = 10000
    bst2 = random_tree(n)
    print("For n=", n)
    print("IPL/n is :", bst2.ipl()/n)
    print("the height is :", bst2.height())
    n = 50000
    bst3 = random_tree(n)
    print("For n=", n)
    print("IPL/n is :", bst3.ipl()/n)
    print("the height is :", bst3.height())
    n = 100000
    bst4 = random_tree(n)
    print("For n=", n)
    print("IPL/n is :", bst4.ipl()/n)
    print("the height is :", bst4.height())

    n = 5000000
    k = 1.39*n*(math.log2(n))
    print("Approximated:", k)
    bst = random_tree(n)
    print(bst.ipl())


if __name__ == "__main__":
    main()


"""
What is the generator good for?
==============================
The generator is good for the following reasons:
1. It is a lazy evaluation. It does not evaluate the whole list at once.
2. It is a memory efficient. It does not store the whole list in memory.
3. It is a fast. It does not need to store the whole list in memory.
4. It is a simple. It is easy to write and easy to read.


1. computing size? Yes,
2. computing height? No, because it needs to store the whole list in memory.
3. contains? Yes, because it does not need to store the whole list in memory.
4. insert? No, because it needs to store the whole list in memory.
5. remove? No, because it needs to store the whole list in memory.




Results for ipl of random trees
===============================

For n= 50
IPL/n is : 6.28
the height is : 10
For n= 100
IPL/n is : 8.25
the height is : 15
For n= 200
IPL/n is : 8.46
the height is : 16
For n= 1000
IPL/n is : 12.171
the height is : 22
For n= 10001
IPL/n is : 16.25947405259474
the height is : 32
For n= 5000
IPL/n is : 14.6516
the height is : 26
For n= 10000
IPL/n is : 15.887
the height is : 28
For n= 50000
IPL/n is : 20.70042
the height is : 37
For n= 100000
IPL/n is : 21.39659
the height is : 39
141455012

Calculated IPL =2081812  n=100000     Approximated: 2308740.025946717
Calculated IPL=25642992  n=1000000      Approximated: 27704880.3113606
Calculated IPL=143258015 n=5000000    Approximated: 154661801.81627014






"""
