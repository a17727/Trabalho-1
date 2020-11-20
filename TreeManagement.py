'''
Tree



'''

from treelib import Node, Tree
from utils import GetTreeLevel
import pickle

class TreeNode:
    def __init__(self, status = "", comment = ""):
        self.status = status
        self.comment = comment
        self.output = str(status) + " " + str(comment)


class TreeManagement:
    def __init__(self):
        self.nodeList = [None] * 100
        self.node = None
        self.subTree = Tree()
        self.mainTree = Tree()
        self.node_root = self.mainTree.create_node(tag = "Root", identifier= "root", data=TreeNode("root", "root"))

    def CreateTestOkNode(self, value):

        if self.subTree != None:
            self.node = self.mainTree.create_node(value, value, parent= self.node_root, data = TreeNode("OK", ""))
            self.mainTree.merge(value, self.subTree)
        else:
            self.mainTree.create_node(value, value, parent= self.node_root, data = TreeNode("OK", ""))

    def CreateSubtestOkNode(self, value):
        n = GetTreeLevel(value)
        if n == 1:
            if self.subTree != None:
                self.node = self.subTree.get_node("aux")
            if self.node == None:
                self.subTree = Tree()
                self.nodeList[n-1] = self.subTree.create_node("aux", "aux", data = TreeNode("OK", ""))
        self.nodeList[n] = self.subTree.create_node(value, value, parent=self.nodeList[n-1], data = TreeNode("OK", ""))

    def CreateTestNotOkNode(self, value):
        if self.subTree != None:
            self.node = self.mainTree.create_node(value, value, parent= self.node_root, data = TreeNode("OK", ""))
            self.mainTree.merge(value, self.subTree)
        else:
            self.mainTree.create_node(value, value, parent= self.node_root, data = TreeNode("OK", ""))

    def CreateSubtestNotOkNode(self, value):
        n = GetTreeLevel(value)
        if n == 1:
            if self.subTree != None:
                self.node = self.subTree.get_node("aux")
            if self.node == None:
                self.subTree = Tree()
                self.nodeList[n-1] = self.subTree.create_node("aux", "aux", data = TreeNode("NOT OK", ""))
        self.nodeList[n] = self.subTree.create_node(value, value, parent=self.nodeList[n-1], data = TreeNode("NOT OK", ""))
    
    '''def AddComment(self, nodeID, value):
        n = GetTreeLevel(nodeID)
        if n == 0:
            self.mainTree.update_node(nodeID, "comment" :  value)
        elif n >= 1:
            self.subTree.update_node(nodeID, "comment" : value)'''







