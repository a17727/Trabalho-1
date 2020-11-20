import	ply.lex as lex
from utils import slurp
from TAPParser import TAPLexer
from treelib import Node, Tree
import json

a = TAPLexer()

a.build()

a.inputFile("inputs/teste3.t")



a.execute()

a.tree_manager.mainTree.show(data=)