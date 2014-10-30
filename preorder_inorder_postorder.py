
from collections import namedtuple
from sys import stdout

Node = namedtuple('Node', 'data, left, right')

tree = Node(1,
            Node(2,
                 Node(4,
                      Node(8,
                           None,
                           None),
                      Node(9,
                           Node(12, None, None),
                           None)),
                 Node(5,
                      None,
                      None)),
            Node(3,
                 Node(6,
                      Node(10,
                           Node(13, None, None),
                           Node(14, None, None)),
                      Node(11,
                           None,
                           None)),
                 Node(7,
                      None,  
                      None)))
 
 
def printwithspace(i):
    stdout.write("%i " % i)
 
def preorder(node, visitor = printwithspace):    # root, left, right
    if node is not None:
        visitor(node.data)
        preorder(node.left, visitor)
        preorder(node.right, visitor) 

def inorder(node, visitor = printwithspace):   # left, root, right 
    if node is not None:
        inorder(node.left, visitor)
        visitor(node.data)
        inorder(node.right, visitor)

def postorder(node, visitor = printwithspace):   # left, right, root 
    if node is not None:
        postorder(node.left, visitor)
        postorder(node.right, visitor)
        visitor(node.data)



stdout.write(" preorder: ")
preorder(tree)
stdout.write("\n inorder: ")
inorder(tree)
stdout.write("\n postorder: ")
postorder(tree) 


