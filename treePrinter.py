# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 09:59:43 2021

@author: mkowalko
"""
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
from anytree import Node, RenderTree, PreOrderIter



class MyNode(Node):
    'This class contains specifics of a node, the name, aliases and description.\
    They are representing single table between which which relations can be defined.'
    # name should be string
    # aliases should be list of names
    # description should consist of list of strings

    nodeCount = 0
    treeRoot = None
    SchemaRMax = 0


    def __init__(self, name, parent=None):
        if (MyNode.nodeCount == 0):
            MyNode.treeRoot = self
        elif parent == None:
            parent = MyNode.treeRoot
        super().__init__(name, parent)
        #data
        self.name = name
        self.aliases = None
        self.description = None
        self.nodeId=MyNode.nodeCount
        #positions
        self.theta = 0
        self.r = 0
        #ratio of cake it ocupies among the siblings and predecesors
        self.ratio = 0
        self.olderSiblingsRatios = 0
        self.leftLimit = 0
        self.rightLimit = 0

        self.recalculatePositions()
        MyNode.nodeCount+=1


# get/set data
    def setName(self, name):
        self.name = name

    def setAliases(self, aliases):
        self.aliases = aliases

    def description(self):
        return self.description

    def displayEverything(self):
        print ("Total MyNodes %d" % MyNode.nodeCount)
        print ("The nodeId %d" % self.nodeId)
        print ("The name %s" % self.name)
        print ("The aliases %s" % self.aliases)
        print ("The description %s" % self.description)

    def recalculatePositions(self):
        if MyNode.nodeCount == 0:
            return None
        #for pre, fill, node in RenderTree(MyNode.treeRoot):
        #    print("%s%s" % (pre, node.name))
        
        #set root position
        root = MyNode.treeRoot
        root.ratio = 1
        root.theta = 0
        root.r = 0
        #print(str(root))

        parent=root
        #recursive function
        self.calculateChildren(parent)

        return


    def calculateChildren(self, parent):
        children=parent.children
        # children
        for child in children:
            child.olderSiblingsRatios=0
            prevChild=None
            for sibling in range(0, len(children)):
                if parent.children[sibling] is child:
                    break
            #    print(c.parent.children[sibling].ratio)
                prevChild=parent.children[sibling]
                child.olderSiblingsRatios = child.olderSiblingsRatios + parent.children[sibling].ratio
                #print(str(child.name) + "'s olderSiblingsRatios: " + str(child.olderSiblingsRatios))
                #print("times *(2*np.pi)/2: " + str(child.olderSiblingsRatios*(2*np.pi)/2))
            # set positions - first descendants level: b, c
            child.ratio=(len(child.descendants)+1)/(len(parent.descendants))
            generationalRatio=1
            for ancestor in child.ancestors:
                generationalRatio *= ancestor.ratio
            if prevChild:
                child.leftLimit=prevChild.rightLimit
                child.rightLimit=child.leftLimit + generationalRatio*child.ratio*np.pi*2
            else:
                child.leftLimit=parent.leftLimit
            child.rightLimit=child.leftLimit + generationalRatio*child.ratio*np.pi*2
            print(str(child.name) + "'s ratio: " + str(child.ratio) + " limits: " + str(child.leftLimit) + ":" + str(child.rightLimit))
            #print("times *(2*np.pi)/2: " + str(child.ratio*(2*np.pi)/2))
            #theta is in the middle
            thetaFormula = child.leftLimit + 0.5*(child.rightLimit - child.leftLimit)
            child.theta = thetaFormula
            child.r = child.depth*child.depth*800
            bufferR=200
            if child.r+bufferR > MyNode.SchemaRMax:
                MyNode.SchemaRMax = child.r + bufferR
            #print(str(child.name) + ": " + str(child))
            self.calculateChildren(child)
        return

    def print_schema(self):
        figure, ax = plt.subplots(subplot_kw={'projection': 'polar'}, frameon=False)
        #ax.set_rticks([MyNode.SchemaRMax/2, MyNode.SchemaRMax])
        ax.set_rticks([])
        ax.set_thetagrids([0, 45, 90, 135, 180, 225, 270, 315], labels=[])
        ax.set_rmax(MyNode.SchemaRMax)
        #ax.grid(False)

        for node in MyNode.treeRoot.descendants:
            self.printNode(node, ax)

            self.printLimits(node, ax)

        # print and save
        #imgplot = plt.imshow(img)
        plt.savefig('figure.png', transparent=True)
        plt.show()

    def printNode(self, node, ax):
        text=node.name
        if node.aliases:
            text = text + '\n' + str(node.aliases)
        if node.description:
            text = text + '\n' + str(node.description)

        #print data
        ax.text(node.theta,node.r,
            text,
            fontsize=8, ha="center", va="center",
            bbox=dict(boxstyle='round',
                          ec=(.1, .5, .5),
                          fc=(.1, .8, .8),
                          )
            )

        #print link parent->child
        if node.r > 0:
            noPoints=10
            #parent is starting point
            radsStart=node.parent.theta
            radsEnd=node.theta
            radsdt=(radsEnd-radsStart)/noPoints
            if radsStart == radsEnd:
                rads = node.theta*np.ones(noPoints)
            else:
                rads = np.arange(radsStart, radsEnd, radsdt)
            rStart=node.parent.r
            rEnd=node.r
            rdt=(rEnd-rStart)/noPoints
            r = np.arange(rStart, rEnd, rdt)
            ax.plot(rads, r, 'g.', alpha=0.5)

        
    def printLimits(self, node, ax):
        #print node's spacial influence
        colors = ['b', 'r', 'g', 'm', 'y', 'bisque', 'lightcoral', 'limegreen', 'lavender', 'indigo']
        noPoints=100
        radsLeft = node.leftLimit*np.ones(noPoints)
        radsRight = node.rightLimit*np.ones(noPoints)
        radsdt=(node.rightLimit-node.leftLimit)/(noPoints)
        rads=np.arange(node.leftLimit, node.rightLimit, radsdt)
        r = node.r*np.ones(noPoints)
        #colors are iterated, the rads are cut to overcome the situation where +/- 1 is created
        ax.plot(rads[2:noPoints-2], r[2:noPoints-2], color=colors[node.nodeId%len(colors)], alpha=0.75)
        #ax.fill(radsLeft, r, radsRight, r,  facecolor=colors[node.nodeId], alpha=0.25)

        

    def print_descendants(self):
        for i in range(0, len(self.nodes)):
            #print(self.nodes[i].name + str(self.nodes[i].descendants.count()))
            #print(self.nodes[i])
            print(self.nodes[i].name + "has " + str(len(self.nodes[i].descendants)) + " descendants" )




