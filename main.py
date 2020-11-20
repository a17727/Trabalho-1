import	ply.lex as lex
from utils import slurp
from TAPParser import TAPLexer
from treelib import Node, Tree
import json
from globalstats import GlobalStats
import os


a = TAPLexer()
b = GlobalStats()

a.build()

a.inputFile("inputs/teste3.t")



a.execute()

b.LoadFile("globalstats.json")
print(b.totalTests)
b.UpdateStats(a.n_tests, a.n_ok_subtests , a.n_nok_tests, a.n_subtests, a.n_ok_subtests, a.n_nok_subtests)

#Retorno ao utilizador - Informação dos testes por ficheiro
print(a.n_tests, a.n_ok_subtests , a.n_nok_tests, a.n_subtests, a.n_ok_subtests, a.n_nok_subtests)
b.SaveToFile("globalstats.json")

a.tree_manager.mainTree.show()


data = a.tree_manager.mainTree.to_json()

with open('data.json', 'w') as outfile:
    outfile.write(data)
