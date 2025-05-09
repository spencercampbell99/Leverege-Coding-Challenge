#!/usr/bin/env python3
"""
Leverege Coding Challenge - Main Module
This script provides a modular framework for running different coding challenge solutions.
"""

class Node:
    """
    A class representing a node in a graph or tree structure.
    Each node can have multiple nodes.
    """
    def __init__(self, value, parent=None):
        self.value = value
        self.nodes = []
        self.parent = parent

    def add_child(self, child_node):
        """
        Add a child node to the current node.
        """
        self.nodes.append(child_node)
        
    def add_child_with_value(self, value):
        """
        Add a child node with a specific value to the current node.
        """
        child_node = Node(value, parent=self)
        self.add_child(child_node)
        return child_node
    
    def add_list_of_children_with_values(self, values):
        """
        Add a list of child nodes with specific values to the current node.
        """
        for value in values:
            self.add_child_with_value(value)
        return self.nodes
    
    def __repr__(self):
        """
        Full representation of the tree (including nodes)
        """
        return f"Node({self.value}, children={self.nodes})"
    
    def __str__(self):
        """
        String representation of the node.
        """
        return f"Node({self.value})"

def build_tree(depth = 2, breadth = 2):
    """
    Build a tree structure with a specified depth and breadth.
    """
    root = Node(1)
    iter = 2
    def build_tree_helper(node, current_depth):
        nonlocal iter
        
        """
        Helper function to recursively build the tree.
        """
        if current_depth < depth:
            for i in range(breadth):
                child_node = node.add_child_with_value(iter)
                iter += 1
                build_tree_helper(child_node, current_depth + 1)
        
    build_tree_helper(root, 1)
    
    return root

def question_1():
    """
    Given a list of Nodes where each Node can have a list of Nodes, how would you visit all the Nodes?
    """
    
    # Build testing Nodes (tree)
    root = build_tree(depth=5, breadth=2)
    
    def visit_nodes(node):
        """
        Visit all nodes in the tree structure.
        """
        print(node)
        for child in node.nodes:
            visit_nodes(child)
    
    print("Visiting all nodes in the tree:")
    visit_nodes(root)
    exit(0)

def question_2():
    """
    Given two nodes in a tree, how would you calculate the distance between them? (feel free to modify the data structures involved if it makes the calculation easier)
    """
    
    depth = 5
    breadth = 2
    
    # build testing Nodes (tree)
    root = build_tree(depth=depth, breadth=breadth)
    
    def pick_random_node(root):
        """
        Pick a random node from the tree.
        """
        import random
        
        random_depth = random.randint(0, depth - 1)
        random_breadth = random.randint(0, breadth - 1)
        
        node = root
        for i in range(random_depth):
            node = node.nodes[random_breadth]

        return node
    
    node1 = pick_random_node(root)
    node2 = pick_random_node(root)
    
    # override for testing
    # node1 = root.nodes[0].nodes[0].nodes[0]
    # node2 = root.nodes[1].nodes[1].nodes[1].nodes[1]
    
    # correct answer is 7 steps
    
    print(str(node1), str(node2))

    def find_distance(node1, node2, root):
        """
        Calculate the distance between two nodes in the tree.
        """
        
        steps_taken = 0
        
        def find_path_from_root(root, target):
            """
            Find the path from the root to the target node. Returns path of children indexes to go from root to target.
            """
            path = []
            if root == target:
                return path
            
            for i, child in enumerate(root.nodes):
                if child == target:
                    path.append(i)
                    return path
                else:
                    sub_path = find_path_from_root(child, target)
                    if sub_path is not None:
                        path.append(i)
                        path.extend(sub_path)
                        return path
            return None
        
        path1 = find_path_from_root(root, node1)
        path2 = find_path_from_root(root, node2)
        
        if path1 is None or path2 is None:
            print("One of the nodes is not in the tree.")
            return
        
        node1_depth = len(path1)
        node2_depth = len(path2)
        
        # maximum steps would be up to root then back down, so we can remove later
        steps_taken = node1_depth + node2_depth
        
        for i in range(min(node1_depth, node2_depth)):
            if path1[i] == path2[i]:
                steps_taken -= 2
            else:
                break
        
        print(f"Distance between {node1} and {node2}: {steps_taken} steps")
    
    find_distance(node1, node2, root)
    
    exit(0)


def display_menu():
    """
    Display the available challenges to run.
    """
    print("\n=== Leverege Coding Challenge Menu ===")
    print("1. Question 1")
    print("2. Question 2")
    print("0. Exit")
    print("=======================================")


def main():
    """
    Main function to control program flow and user interaction.
    """
    challenges = {
        '1': question_1,
        '2': question_2,
    }
    
    while True:
        display_menu()
        choice = input("Enter your choice (0-3 or A for all): ").strip().upper()
        
        if choice == '0':
            print("Exiting program. Goodbye!")
            break
        elif choice in challenges:
            challenges[choice]()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    """
    Entry point of the program.
    """
    print("Welcome to the Leverege Coding Challenge Solutions!")
    main()