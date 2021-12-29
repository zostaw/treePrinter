
from treePrinter import MyNode as MyNode
#from treePrinter import Schema as Schema
from anytree import Node, RenderTree, PreOrderIter
import numpy as np
import copy



#initiate nodes
a = MyNode("node a")

b = MyNode("node b", parent=a)
#b.setAliases('aliases')
#b.setDescription('description')

c = MyNode("node c", parent=a)
#c_aliases = ['physics', 'chemistry', 'whatever']
#c.setAliases(c_aliases)
#c_description = ['this is description', 'for c']
#c.setDescription(c_description)

d = MyNode("node d", parent=c)
e = MyNode("node e", parent=d)
f = MyNode("node f", parent=c)
g = MyNode("node g", parent=d)
h = MyNode("node h", parent=d)



# run the program
a.print_schema()



