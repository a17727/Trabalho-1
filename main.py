from TAPParser import TAPLexer
from treelib import Node, Tree
import json
from globalstats import GlobalStats
from filesinfo import FileInfo

 #Intializing Class Instances
 #
a = TAPLexer()
b = GlobalStats()
c = FileInfo()

a.build()

a.inputFile("inputs/teste3.t")

a.execute()

b.LoadFile("globalstats.json")
b.UpdateStats(a.n_tests, a.n_ok_subtests , a.n_nok_tests, a.n_subtests, a.n_ok_subtests, a.n_nok_subtests)
c.UpdateFileInfo(b.totalFiles, "inputs/teste3.t", a.n_ok_tests, a.n_nok_tests, a.n_ok_subtests, a.n_nok_subtests)
c.SaveToJSON("fileInfo.json")
b.SaveToFile("globalstats.json")

a.tree_manager.mainTree.show()
print(b.__dict__)


data = a.tree_manager.mainTree.to_json()

with open('data.json', 'w') as outfile:
    outfile.write(data)
