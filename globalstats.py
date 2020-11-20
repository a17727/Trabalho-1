import os
import json

class GlobalStats():
    def __init__(self):
       
        self.totalFiles = 0
        self.totalTests = 0
        self.totalOkTests = 0 #só dos testes
        self.totalNotOktests = 0 #só dos testes
        self.totalSubtests = 0
        self.totalOkSubtests = 0
        self.totalNotOkSubtests = 0

    def UpdateStats(self, tests, okTests, notOkTests, subTests, okSubtests, notOkSubtests):
        self.totalFiles += 1
        self.totalTests += tests
        self.totalOkTests += okTests
        self.totalNotOktests += notOkTests
        self.totalSubtests += subTests
        self.totalOkSubtests += okSubtests
        self.totalNotOkSubtests += notOkSubtests

    
    def LoadFile(self,filePath):
        try:
            with open(filePath, 'r') as f:
                obj_dict = json.loads(f.read())
                self.totalFiles = obj_dict["totalFiles"]
                self.totalTests = obj_dict["totalTests"]
                self.totalOkTests = obj_dict["totalOkTests"]
                self.totalNotOktests = obj_dict["totalNotOkTests"]
                self.totalSubtests = obj_dict["totalSubtests"]
                self.totalOkSubtests = obj_dict["totalOkSubtests"]
                self.totalNotOkSubtests = obj_dict["totalNotOkSubtests"]
        except:
            exit
            

    def SaveToFile(self, filePath):

        jsonified_object = self.__dict__
        with open(filePath, 'w') as output:
            json.dump(jsonified_object, output)
