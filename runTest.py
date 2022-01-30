
from treePrinter import MyNode as MyNode
#from treePrinter import Schema as Schema
from anytree import Node, RenderTree, PreOrderIter
import numpy as np
import copy



def basic():

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
    
def conversations():
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



def bigA():
    A = MyNode("A")
    Aa = MyNode("Aa", parent=A)
    Aaa = MyNode("Aaa", parent=Aa)
    Aab = MyNode("Aab", parent=Aa)
    Aaba = MyNode("Aaba", parent=Aab)
    Aabb = MyNode("Aabb", parent=Aab)
    Aabc = MyNode("Aabc", parent=Aab)
    Aabd = MyNode("Aabd", parent=Aab)
    Aac = MyNode("Aac", parent=Aa)
    Aad = MyNode("Aad", parent=Aa)
    Ab = MyNode("Ab", parent=A)
    Aba = MyNode("Aba", parent=Ab)
    Abb = MyNode("Abb", parent=Ab)
    Ac = MyNode("Ac", parent=A)
    Aca = MyNode("Aca", parent=Ac)
    Acaa = MyNode("Acaa", parent=Aca)
    Acb = MyNode("Acb", parent=Ac)
    Acc = MyNode("Acc", parent=Ac)
    Ad = MyNode("Ad", parent=A)
    Ada = MyNode("Ada", parent=Ad)
    Adaa = MyNode("Adaa", parent=Ada)
    Adaaa = MyNode("Adaaa", parent=Adaa)
    Adaab = MyNode("Adaab", parent=Adaa)
    Adb = MyNode("Adb", parent=Ad)
    Adba = MyNode("Adba", parent=Adb)
    Adbb = MyNode("Adbb", parent=Adb)
    Ae = MyNode("Ae", parent=A)
    Aea = MyNode("Aea", parent=Ae)
    Aeb = MyNode("Aeb", parent=Ae)
    Aec = MyNode("Aec", parent=Ae)
    Aeca = MyNode("Aeca", parent=Aec)
    Aed = MyNode("Aed", parent=Ae)
    Aee = MyNode("Aee", parent=Ae)
    Aeea = MyNode("Aeea", parent=Aee)
    Aef = MyNode("Aef", parent=Ae)
    Aefa = MyNode("Aefa", parent=Aef)
    Aefb = MyNode("Aefb", parent=Aef)
    Aefc = MyNode("Aefc", parent=Aef)
    Aefd = MyNode("Aefd", parent=Aef)
    Aeg = MyNode("Aeg", parent=Ae)
    
    
    
    # run the program
    A.print_schema()


bigA()
