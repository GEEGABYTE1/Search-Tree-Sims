class TreeNode:
    def __init__(self, value):
        self.value = value 
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, child_node):
        self.children = [i for i in self.children if i != child_node]

    def traverse(self):
        node = self 
        level = 1
        number = int(input('Please enter a number: '))
        while len(node.children) > 0:
            try:
                level += 1
                if number <= node.value:
                    if number == node.children[0].value:
                        print('Level {}'.format(level))
                        print(node.children[0].value)
                        break 
                    else:
                        print('Level {}'.format(level))
                        print(node.value)
                        node.value = node.children[0].value 
                        node.children = node.children[0].children 
                    
                elif number >= node.value:
                    if number == node.children[-1].value:
                        print('Level {}'.format(level))
                        print(node.children[-1].value)
                        break 
                    else:
                        print('Level {}'.format(level))
                        print(node.value)
                        node.value = node.children[-1].value 
                        node.children = node.children[-1].children 

            except IndexError:
                print('That value does not seem to be in the tree')            








test = TreeNode(8)
test2 = TreeNode(3)
test3 = TreeNode(10)
test4 = TreeNode(1)
test5 = TreeNode(6)
test6 = TreeNode(14)
test7 = TreeNode(4)
test8 = TreeNode(7)
test9 = TreeNode(13)

test.add_child(test2)
test.add_child(test3)
test2.add_child(test4)
test2.add_child(test5)
test3.add_child(test6)
test6.add_child(test9)
test5.add_child(test7)
test5.add_child(test8)
test.traverse()
print()



