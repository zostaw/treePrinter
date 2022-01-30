
from treePrinter import MyNode as MyNode
#from treePrinter import Schema as Schema
from anytree import Node, RenderTree, PreOrderIter
import numpy as np
import copy





A = MyNode("CONVERSATIONS")
Aa = MyNode("Body Language", parent=A)
Aaa = MyNode("expressions", parent=Aa)
Aab = MyNode("Body posture", parent=Aa)
Aaba = MyNode("confidence", parent=Aab)
Aabb = MyNode("charisma", parent=Aab)
Aabc = MyNode("warmth", parent=Aab)
Aabd = MyNode("old wise", parent=Aab)
Aac = MyNode("emotions", parent=Aa)
Aad = MyNode("rezonant throat speech", parent=Aa)
Ab = MyNode("Favorites list", parent=A)
Aba = MyNode("Topic", parent=Ab)
Abb = MyNode("Topic", parent=Ab)
Ac = MyNode("SmallTalk", parent=A)
Aca = MyNode("Co słychać?", parent=Ac)
Acaa = MyNode("(Kim jest rozmówca)", parent=Aca)
Acb = MyNode("How are you?", parent=Ac)
Acc = MyNode("(1) Small talk survival guide", parent=Ac)
Ad = MyNode("Focus", parent=A)
Ada = MyNode("Acknowledgment", parent=Ad)
Adaa = MyNode("consider other person's opinions and feelings", parent=Ada)
Adaaa = MyNode("always ADD", parent=Adaa)
Adaab = MyNode("never crucify", parent=Adaa)
Adb = MyNode("Speech template", parent=Ad)
Adba = MyNode("conclusion first", parent=Adb)
Adbb = MyNode("then argumentation", parent=Adb)
Ae = MyNode("Key concepts", parent=A)
Aea = MyNode("parafraze", parent=Ae)
Aeb = MyNode("be curious", parent=Ae)
Aec = MyNode("be empathetic", parent=Ae)
Aeca = MyNode("yes and...", parent=Aec)
Aed = MyNode("listen for what is NOT being said", parent=Ae)
Aee = MyNode("search for meaning", parent=Ae)
Aeea = MyNode("EVERYTHING depends on IT", parent=Aee)
Aef = MyNode("try to figure out what is this humans main problem in life", parent=Ae)
Aefa = MyNode("values", parent=Aef)
Aefb = MyNode("thought patterns", parent=Aef)
Aefc = MyNode("aspirations", parent=Aef)
Aefd = MyNode("(2) Human's story", parent=Aef)
Aeg = MyNode("(3) Build your scripts", parent=Ae)



# run the program
A.print_schema()



