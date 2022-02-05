# treePrinter
This repo is drawing a tree with data, it assigns the positions of the nodes based on their spread size
1. Run:
python ./runTest.py


# CODE
1. MyTree contains the main class MyTree. It inherits from Node class

Building the tree:
Each new instance represents a new node. The first one created is a root.
The tree can be initiated by creating Grant parent for all nodes, for example:
parent_node = MyTree("root name")
New nodes can be added by building up the branches, for example first child:
first_child = MyTree("first child name", parent=parent_node)

Printing the tree:
The tree is automaticaly saved as figure.png when function is requested:
root.print_schema()
additionaly a plot will be printed



2. runTest provides a couple of examples of trees
