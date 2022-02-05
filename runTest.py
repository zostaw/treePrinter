
from MyTree import MyTree as MyTree
from anytree import Node, RenderTree, PreOrderIter
import numpy as np
import copy

def runTest():
    bigA()

def basic():

    #initiate nodes
    a = MyTree("node a")
    
    b = MyTree("node b", parent=a)
    #b.setAliases('aliases')
    #b.setDescription('description')
    
    c = MyTree("node c", parent=a)
    #c_aliases = ['physics', 'chemistry', 'whatever']
    #c.setAliases(c_aliases)
    #c_description = ['this is description', 'for c']
    #c.setDescription(c_description)
    
    d = MyTree("node d", parent=c)
    e = MyTree("node e", parent=d)
    f = MyTree("node f", parent=c)
    g = MyTree("node g", parent=d)
    h = MyTree("node h", parent=d)
    
    # run the program
    a.print_schema()
    
def conversations():
    A = MyTree("CONVERSATIONS")
    Aa = MyTree("Body Language", parent=A)
    Aaa = MyTree("expressions", parent=Aa)
    Aab = MyTree("Body posture", parent=Aa)
    Aaba = MyTree("confidence", parent=Aab)
    Aabb = MyTree("charisma", parent=Aab)
    Aabc = MyTree("warmth", parent=Aab)
    Aabd = MyTree("old wise", parent=Aab)
    Aac = MyTree("emotions", parent=Aa)
    Aad = MyTree("rezonant throat speech", parent=Aa)
    Ab = MyTree("Favorites list", parent=A)
    Aba = MyTree("Topic", parent=Ab)
    Abb = MyTree("Topic", parent=Ab)
    Ac = MyTree("SmallTalk", parent=A)
    Aca = MyTree("Co słychać?", parent=Ac)
    Acaa = MyTree("(Kim jest rozmówca)", parent=Aca)
    Acb = MyTree("How are you?", parent=Ac)
    Acc = MyTree("(1) Small talk survival guide", parent=Ac)
    Ad = MyTree("Focus", parent=A)
    Ada = MyTree("Acknowledgment", parent=Ad)
    Adaa = MyTree("consider other person's opinions and feelings", parent=Ada)
    Adaaa = MyTree("always ADD", parent=Adaa)
    Adaab = MyTree("never crucify", parent=Adaa)
    Adb = MyTree("Speech template", parent=Ad)
    Adba = MyTree("conclusion first", parent=Adb)
    Adbb = MyTree("then argumentation", parent=Adb)
    Ae = MyTree("Key concepts", parent=A)
    Aea = MyTree("parafraze", parent=Ae)
    Aeb = MyTree("be curious", parent=Ae)
    Aec = MyTree("be empathetic", parent=Ae)
    Aeca = MyTree("yes and...", parent=Aec)
    Aed = MyTree("listen for what is NOT being said", parent=Ae)
    Aee = MyTree("search for meaning", parent=Ae)
    Aeea = MyTree("EVERYTHING depends on IT", parent=Aee)
    Aef = MyTree("try to figure out what is this humans main problem in life", parent=Ae)
    Aefa = MyTree("values", parent=Aef)
    Aefb = MyTree("thought patterns", parent=Aef)
    Aefc = MyTree("aspirations", parent=Aef)
    Aefd = MyTree("(2) Human's story", parent=Aef)
    Aeg = MyTree("(3) Build your scripts", parent=Ae)
    
    # run the program
    A.print_schema()



def bigA():
    A = MyTree("A")
    Aa = MyTree("Aa", parent=A)
    Aaa = MyTree("Aaa", parent=Aa)
    Aab = MyTree("Aab", parent=Aa)
    Aaba = MyTree("Aaba", parent=Aab)
    Aabb = MyTree("Aabb", parent=Aab)
    Aabc = MyTree("Aabc", parent=Aab)
    Aabd = MyTree("Aabd", parent=Aab)
    Aac = MyTree("Aac", parent=Aa)
    Aad = MyTree("Aad", parent=Aa)
    Ab = MyTree("Ab", parent=A)
    Aba = MyTree("Aba", parent=Ab)
    Abb = MyTree("Abb", parent=Ab)
    Ac = MyTree("Ac", parent=A)
    Aca = MyTree("Aca", parent=Ac)
    Acaa = MyTree("Acaa", parent=Aca)
    Acb = MyTree("Acb", parent=Ac)
    Acc = MyTree("Acc", parent=Ac)
    Ad = MyTree("Ad", parent=A)
    Ada = MyTree("Ada", parent=Ad)
    Adaa = MyTree("Adaa", parent=Ada)
    Adaaa = MyTree("Adaaa", parent=Adaa)
    Adaab = MyTree("Adaab", parent=Adaa)
    Adb = MyTree("Adb", parent=Ad)
    Adba = MyTree("Adba", parent=Adb)
    Adbb = MyTree("Adbb", parent=Adb)
    Ae = MyTree("Ae", parent=A)
    Aea = MyTree("Aea", parent=Ae)
    Aeb = MyTree("Aeb", parent=Ae)
    Aec = MyTree("Aec", parent=Ae)
    Aeca = MyTree("Aeca", parent=Aec)
    Aed = MyTree("Aed", parent=Ae)
    Aee = MyTree("Aee", parent=Ae)
    Aeea = MyTree("Aeea", parent=Aee)
    Aef = MyTree("Aef", parent=Ae)
    Aefa = MyTree("Aefa", parent=Aef)
    Aefb = MyTree("Aefb", parent=Aef)
    Aefc = MyTree("Aefc", parent=Aef)
    Aefd = MyTree("Aefd", parent=Aef)
    Aeg = MyTree("Aeg", parent=Ae)
    
    # run the program
    A.print_schema()


if __name__ == '__main__':
    runTest()
