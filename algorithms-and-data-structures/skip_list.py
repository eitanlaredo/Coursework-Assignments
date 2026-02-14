
import random

class Node:
    def __init__(self, key, left=None, right=None, top=None, bot=None):
        self.key = key
        self.left = left
        self.right = right
        self.top = top
        self.bot = bot

    def get_key(self):
        return self.key

# Define max_level globally
max_level = 50

def get_levels():
    count = 0
    flip = 1  # 1 = heads, 0 = tails

    while flip == 1:
        flip = random.randint(1, 2) % 2
        if flip == 1:  # heads
            count += 1

    return count

class SkipList:
    def __init__(self):
        self.level = 0
        self.sentinel_list = [Node(float('-inf')) for _ in range(max_level)]
        # Initialize right pointers of the sentinel nodes to float('inf')
        for i in range(max_level):
            self.sentinel_list[i].right = Node(float('inf'))

    def get_level(self):
        return self.level

    def list_insert(self, key, list_level):
        new_node = Node(key)
        head = self.sentinel_list[list_level]

        current_node = head
        node_found = False
        while node_found is False:
            if key < current_node.get_key():
                if current_node.left is None:
                    print(f"Prepending new head as {key} at level {list_level}")
                    new_node.right = current_node
                    current_node.left = new_node
                    if list_level == 0:
                        self.sentinel_list[list_level] = new_node
                    new_node.right = float('inf')
                    return new_node

            if current_node.right is float('inf') or key < current_node.right.get_key():
                print(f"Inserting {key} between {current_node.get_key()} and {current_node.right.get_key() if current_node.right else 'None'} at level {list_level}")
                new_node.right = current_node.right
                new_node.left = current_node

                if current_node.right is not float('inf'):
                    current_node.right.left = new_node
                current_node.right = new_node
                return new_node

            current_node = current_node.right


    def add_levels(self, node):
        levels = get_levels()
        if levels == 0:
            print(f"Flipped 0 heads, no levels added for key {node.get_key()}")
            return
        print(f"Adding {levels} levels for key {node.get_key()}")
        if levels > self.level:
            self.level = levels

        current_node = node # the node we jsut inserted at the base level
        for i in range(1, levels + 1):

            inserted_node = self.list_insert(node.get_key(), i)

            inserted_node.bot = current_node
            current_node.top = inserted_node
            current_node = inserted_node

    def insert(self, key):
        node = self.list_insert(key, 0)
        self.add_levels(node)

    def lookup(self, value):
        level = self.get_level()

        current_node = self.sentinel_list[level]  # start at highest level in sentinel list
        print(f"Starting at level {level}")
        

        # print(f"the node one lower is {current_node.bot.right.get_key()} ")
        if current_node.right is None or current_node.right.key == float('inf'):  # If the list is empty
            print("List is empty")
            return None

        initial_level_found = False
        while level >= 0 and initial_level_found is False:
            if current_node.right and current_node.right.key != float('inf') and value >= current_node.right.key:
                current_node = current_node.right  # Move right in the current level
                initial_level_found = True

            else:
                level -= 1
                current_node = self.sentinel_list[level]

        while level >= 0:
            while current_node.right and current_node.right.key != float('inf') and value >= current_node.right.key:
                current_node = current_node.right  # Move right in the current level

            if current_node.key == value:
                print(f"Found value {value} in skip list at level {level}")
                return current_node

            if level > 0 and current_node.bot:  
                current_node = current_node.bot  # Move down to the next lower level
            level -= 1

        print("Value not in skip list")
        return None

    def delete(self, key):
        node = self.lookup(key)
        
        if node is None:
            print(f"Key {key} not found. No deletion performed.")
            return

        # Move to the top level of the node
        while node.top is not None:
            node = node.top

        # Iterate downwards and delete the node, fixing links in each level
        while node is not None:
            # Fix the left and right links
            if node.left:
                node.left.right = node.right
            if node.right:
                node.right.left = node.left

            # Move down to the next level
            node = node.bot


    def print_skip_list(self):
        for level in reversed(range(self.level + 1)):
            print(f"Level {level}: ", end="")
            current_node = self.sentinel_list[level].right
            while current_node is not None:
                print(current_node.get_key(), end=" -> ")
                current_node = current_node.right
            print("None")

def main():
    sl = SkipList()
    sl.insert(5)
    sl.insert(8)
    sl.insert(7)
    sl.insert(10)
    sl.insert(10)
    sl.insert(15)
    sl.print_skip_list()
    sl.delete(10)
    sl.lookup(7)
    sl.print_skip_list()





if __name__ == "__main__":
    main()
