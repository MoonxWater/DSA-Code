from typing import Optional

class Node:
    def __init__(self, val: int, parent = None):
        self.val = val
        self.parent = parent
        self.left_child: Optional['Node'] = None
        self.right_child: Optional['Node'] = None
    
    class ChildExistsError(Exception):
        pass

    def left(self, val: int):
        if not self.left_child:
            self.left_child = Node(val, self)
        else:
            raise self.ChildExistsError(f"child already exists at left branch.")
        
    def right(self, val: int):
        if not self.right_child:
            self.right_child = Node(val, self)
        else:
            raise self.ChildExistsError(f'child already exists at right branch.')
        
    def __str__(self):
        left_child = str(self.left_child.val) if self.left_child else 'None'
        right_child = str(self.right_child.val) if self.right_child else 'None'
        children = f"{left_child}     {right_child}"
        return f'{self.val:^20}\n{'/ \\':^20}\n{children:^20}'


tree = Node(1)
tree.left(2)
tree.right(3)
tree.left_child.left(4) if tree.left_child is not None else "T_T"
tree.left_child.right(5) if tree.left_child is not None else "T_T"
tree.right_child.left(6) if tree.right_child is not None else "T_T"
tree.right_child.right(7) if tree.right_child is not None else "T_T"

print(tree.left_child.__str__())

