class MinHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    def add(self, element):
        self.heap_list.append(element)
        self.count += 1
        self.heapify_up()

    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return (idx * 2) + 1

    def heapify_up(self):
        idx = self.count 
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]

            if parent < child:
                print('Swapping {parent} with {child}'.format(parent=parent, child=child))
                self.heap_list[idx] = parent 
                self.heap_list[self.parent_idx(idx)] = child 
            
            idx = self.parent_idx(idx)
        
        print('Heap restored {}'.format(self.heap_list))

    def retrieve_min(self):
        if self.count == 0:
            print('The heap is empty')
            return None 
        else:
            minimum = self.heap_list[1]
            print("Removing {min} from {heap}".format(min=minimum, heap=self.heap_list))
            self.heap_list[1] = self.heap_list[-1]
            self.count -= 1
            self.heap_list.pop()
            self.heapify_down()
            return minimum 
    
    def get_smaller_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            print("There is only a left child")
            return self.left_child_idx(idx)
        else:
            left_child = self.heap_list[self.left_child_idx(idx)]
            right_child = self.heap_list[self.right_child_idx(idx)]

            if left_child < right_child:
                print("The left child is smaller than the right child")
                return self.left_child_idx(idx)
            else:
                print("The right child is smaller than the left child")
                return self.right_child_idx(idx)

    def child_present(self, idx):
        if self.left_child_idx(idx) <= self.count:
            return True 

    def heapify_down(self):
        idx = 1
        while self.child_present(idx):
            smaller_child_idx = self.get_smaller_child_idx(idx)
            child = self.heap_list[smaller_child_idx]
            parent = self.heap_list[idx]

            if parent < child:
                self.heap_list[idx] = child 
                self.heap_list[smaller_child_idx] = parent
            
            idx = smaller_child_idx

        print("Heap restored {}".format(self.heap_list))

    def traverse(self):
        found = False
        number = input("Please input a number you want to find: ")
        level = 1
        while found != True:
            try:
                if len(self.heap_list) == 0:
                    print('The heap is empty')
                    return 
                else:
                    for i in range(len(self.heap_list)):
                        print('Level {}'.format(level))
                        
                        if i % 2 == 0:
                            level += 1

                        if self.heap_list[i] == int(number):
                            print('The value has been found: {}'.format(self.heap_list[i]))
                            print()
                            found = True 
                            return
                            break
                        else:
                            print('Value: {}'.format(self.heap_list[i]))
                            print()
            except ValueError:
                pass
                
                
            if found == False:
                print("The value inputted is not valid! ")
                print()
                prompt = input('Would you like to find another valid value? (type yes or no): ')

                if prompt == "yes" or prompt == "yes ":
                    number = input("Please input a number you want to find: ")
                    level = 1
                else:
                    break 
            
                
        
### Test ### 

test = MinHeap()
lst = range(7)
for i in range(1, len(lst)):
    test.add(i)
print(test.heap_list)
print()
test.retrieve_min()
print()
print(test.heap_list)
test.traverse()