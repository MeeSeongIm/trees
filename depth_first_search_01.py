
# depth first search algorithm.  
 
class node(object):
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

    def search(self, st):
        if self.value == st:
            return True
        for i in self.children:
             if i.search(st):
                 return True
        return False

def search(self,st):
    if self.value==st:
        return True
    else:
        return any(i.search(st) for i in self.children)

tree = node("risk management",[
        node("portfolio",[
            node("NASDAQ"),
            node("NYSE")]),
        node("stock",[
            node("AMEX"),
            node("ABT"),
            node("SLX"),[
                node("SONC")]
        ])
       ])

print(tree.search("SLX"))
 
 
 
 
 
 
