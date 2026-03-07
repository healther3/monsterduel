import random

class Node:
    def __init__(self,val,next=None):
        self.next = next
        self.val = val
        
class List:
    def __init__(self,head):
        self.head = head
        self.tail = head

    def push_back(self,node):
        self.tail.next = node
        self.tail = self.tail.next
    
    @staticmethod
    def create_random_list(n):
        if n == 0:
            return Node(random.randint(1,100))
        else:
            return Node(random.randint(1,100),List.create_random_list(n-1))
    def rev(self):
        cur = self.head
        self.tail = cur
        prev = None
        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        self.head = prev

    def print_list(self):
        cur = self.head
        while cur:
            print(f"{cur.val},",end="")
            cur = cur.next
    
def main():
    l = List(List.create_random_list(100))
    l.print_list()
    l.rev()
    print("")
    print("rev")
    l.print_list()

if __name__ == "__main__":
    main()
        