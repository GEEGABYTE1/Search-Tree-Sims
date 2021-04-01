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







