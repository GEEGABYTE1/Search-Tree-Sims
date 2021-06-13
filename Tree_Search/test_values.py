from Search_Binary_Tree import TreeNode


#### Test Inputs #####

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