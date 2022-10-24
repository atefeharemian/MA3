""" linked_list.py

Student:
Mail:
Reviewed by:
Date reviewed:
"""


class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):           # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented
    # function to return the length of the list using while loop
    def length(self):
        if self.first is None:
            return 0
        else:
            count = 0
            f = self.first
            while f:
                count += 1
                f = f.succ
            return count

    # calculate the mean of the list
    def mean(self):
        if self.first is None:
            return 0
        else:
            sum = 0
            f = self.first
            while f:
                sum += f.data
                f = f.succ
            return sum / self.length()
    # Write a method which removes the last node from the list. The method should return the value in the deleted node.

    def remove_last(self):
        if self.first is None:
            return None
        if self.first.succ is None:
            x = self.first.data
            self.first = None
            return x
        else:
            f = self.first
            while f.succ.succ:
                f = f.succ
            last = f.succ
            f.succ = None
            return last.data
    # delete the first node containing x and return True if x is in the list, otherwise return False

    def remove(self, x):
        if self.first is None:
            return False
        if self.first.data == x:
            self.first = self.first.succ
            return True
        else:
            f = self.first
            while f.succ:
                if f.succ.data == x:
                    f.succ = f.succ.succ
                    return True
                f = f.succ
            return False

    def count(self, x):
        if self.first is None:
            return 0
        else:
            count = 0
            f = self.first
            while f:
                if f.data == x:
                    count += 1
                f = f.succ
            return count
    # convert the tuple to a list

    def to_list(self):
        if self.first is None:
            return []
        else:
            l = []
            f = self.first
            while f:
                l.append(f.data)
                f = f.succ
            return l
    # delete all nodes containing x and return a list of remaining nodes

    def remove_all(self, x):
        if self.first is None:
            return []
        if self.first.data == x:
            self.first = self.first.succ
            return self.remove_all(x)
        else:
            f = self.first
            while f.succ:
                if f.succ.data == x:
                    f.succ = f.succ.succ
                else:
                    f = f.succ
            return self.to_list()
    # __str__ with generator and yield

    def __str__(self):
        if self.first is None:
            return '()'
        return '(' + ', '.join(str(x) for x in self) + ')'

    # def copy(self):               # Compulsary
    #     result = LinkedList()
    #     for x in self:
    #         result.insert(x)
    #     return result
    ''' Complexity for this implementation: 
    complexity for copy is O(n^2) because for each element in the list, we have to traverse the whole list again to insert the element

      


    '''
    # More efficient implementation of copy

    def copy(self):
        if self.first is None:
            return LinkedList()
        else:
            result = LinkedList()
            f = self.first
            result.first = LinkedList.Node(f.data, None)
            r = result.first
            while f.succ:
                r.succ = LinkedList.Node(f.succ.data, None)
                r = r.succ
                f = f.succ
            return result

    # def copy(self):               # Compulsary
    #     pass                      # Should be more efficient
    ''' Complexity for this implementation:
    complexity for copy is O(n) because we only have to traverse the list once to copy the elements

    '''
    # index operator for linked list

    def __getitem__(self, ind):   # Compulsory
        if ind < 0:
            ind = self.length() + ind
        f = self.first
        while ind > 0 and f:
            f = f.succ
            ind -= 1
        if f:
            return f.data
        else:
            raise IndexError


class Person:                     # Compulsory to complete
    def __init__(self, name, pnr):
        self.name = name
        self.pnr = pnr

    def __str__(self):
        return f"{self.name}:{self.pnr}"

    def __setitem__(self, key, value):
        if key == 'name':
            self.name = value
        elif key == 'pnr':
            self.pnr = value
        else:
            raise KeyError

    def __getitem__(self, key):
        if key == 'name':
            return self.name
        elif key == 'pnr':
            return self.pnr
        else:
            raise KeyError

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.pnr == other.pnr
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Person):
            return self.pnr < other.pnr
        else:
            return False

    # greater than
    def __gt__(self, other):
        if isinstance(other, Person):
            return self.pnr > other.pnr
        else:
            return False


def main():
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        lst.insert(x)
    lst.print()

    # print(lst.__getitem__(-2))

    # print(lst.length())
    # print(lst.mean())
    # lst.print()
    # print(lst.remove_last())
    # lst.print()
    # print("1:", lst.to_list())
    # print(lst.remove(0))
    # print(lst.count(1))
    print("0:", lst.to_list())
    print("1", lst.remove_all(1))
    print("3:", lst.to_list())
    print("4", lst.remove_all(7))
    print("5", lst.to_list())
    print("6", lst.remove_all(2))
    print("7", lst.to_list())
    sajad = Person("Sajad", 123)
    print(sajad)
    sajad['name'] = 'Sajjad'
    print(sajad)
    print(sajad['name'])
    print(sajad['pnr'])
    ali = Person("Ali", 123)
    print(sajad == ali)
    print(sajad < ali)
    print(sajad > ali)

    # Test code:


if __name__ == '__main__':
    main()
