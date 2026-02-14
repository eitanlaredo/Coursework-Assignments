class Node:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.child = None
        self.parent = None
        self.sibling = None

    def get_key(self):
        return self.key

class BinomialHeap:
    
    def __init__(self):
        self.root = None


    def make_heap(self):
        return BinomialHeap()

    def union(self, H2):
        # First sort roots 



    def union(self, H1, H2):
        # H1 = Heap 1, H2 = Heap 2
        def binomial_heap_merge(H1, H2):
            head = None
            tail = None
            x = H1.head
            y = H2.head
            while x and y:
                if x.degree <= y.degree:
                    if not head:
                        head = x
                        tail = x
                    else:
                        tail.sibling = x
                        tail = x
                    x = x.sibling
                else:
                    if not head:
                        head = y
                        tail = y
                    else:
                        tail.sibling = y
                        tail = y
                    y = y.sibling
            if x:
                if not head:
                    head = x
                else:
                    tail.sibling = x
            if y:
                if not head:
                    head = y
                else:
                    tail.sibling = y
            return head

        def binomial_link(y, z):
            y.parent = z
            y.sibling = z.child
            z.child = y
            z.degree += 1

        H = self.make_heap()
        H.head = binomial_heap_merge(H1, H2)
        
        if not H.head:
            return H
        
        prev_x = None
        x = H.head
        next_x = x.sibling

        while next_x:
            if x.degree != next_x.degree or (next_x.sibling and next_x.sibling.degree == x.degree):
                prev_x = x
                x = next_x
            elif x.key <= next_x.key:
                x.sibling = next_x.sibling
                binomial_link(next_x, x)
            else:
                if not prev_x:
                    H.head = next_x
                else:
                    prev_x.sibling = next_x
                binomial_link(x, next_x)
                x = next_x
            next_x = x.sibling

        return H
    
    def insert(self, key):
        # create new heap with new node
        new_node = Node(key)
        new_heap = BinomialHeap()
        new_heap.head = new_node
        # merge this new single node heap with self.heap
        self.head = self.union(self, new_heap).head
    
    def extract_min(self):
        # check if head is none, i.e. if heap exists
        if not self.head:
            return None
        
        # now find the binomial tree with the minimum key
        min_node = self.head # set current min to the head
        min_node_prev = None
        current_node = self.head
        prev = None
        
        while current_node is not None:
            if current_node.get_key() < min_node.get_key(): # if inspected node is < min_node, set current node as new min
                min_node = current_node
                min_node_prev = prev

            prev = current_node
            current_node = current_node.sibling

        # Remove min_node from the root list
        if min_node_prev:
            min_node_prev.sibling = min_node.sibling
        else:
            self.head = min_node.sibling

        # Reverse the order of the children of min_node
        child = min_node.child
        new_heap = BinomialHeap()
        
        while child:
            next_child = child.sibling
            child.sibling = new_heap.head
            child.parent = None
            new_heap.head = child
            child = next_child

        # Merge the new heap with the existing heap
        self.head = self.union(self, new_heap).head

        return min_node
    
    def decrease_key(self, node, new_key):
        # continuously decrease 
        if new_key > node.get_key():
            print(f"You can not decrease {node.get_key()} to a value greater than it")

        # set node's key to new key
        node.key = new_key
        # iterate through heap until either node's parent is None, or node key < parent key
        while node.parent and node.get_key() < node.parent.get_key():
            # swap parent and current node
            node.key, node.parent.key = node.parent.key, node.key
            # move to next node, by setting node to its parent
            node = node.parent
    
    def delete(self, node):
        # Decrease the key of the node to negative infinity to remove it
        self.decrease_key(node, float('-inf'))
        # Extract the minimum (which is the node we want to delete)
        self.extract_min()

    def min(self):
        if self.head is None:
            return None

        min_node = self.head
        current = self.head.sibling
        
        while current is not None:
            if current.get_key() < min_node.get_key():
                min_node = current
            current = current.sibling
        
        return min_node

def make_heap_from_array(input_array):
    new_heap = BinomialHeap()
    for each in input_array:
        new_heap.insert(each)
    return new_heap

def main():
    input_heap = [20, 4, 5, 20, 39, 19, 12]
    heap = make_heap_from_array(input_heap)
    heap.insert(2)

    print("Printing min element in heap:", heap.min().get_key())
    
    print("removing min element:", heap.extract_min().get_key())
    
    print("printing new min element:", heap.min().get_key())

if __name__ == "__main__":
    main()
