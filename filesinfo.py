import time
import json
import os



'''


'''

class FileInfo:
    def __init__(self):
        self.id = None
        self.name = None
        self.dateTime = None
        self.ok_tests = None
        self.nok_tests = None
        self.ok_subtests = None
        self.nok_subtests = None

    def UpdateFileInfo(self, filesNo, filePath, okTests, notOkTests, okSubtests, notOkSubtests):
        
        self.id = filesNo
        self.name = os.path.basename(filePath)
        self.dateTime = time.asctime()
        self.ok_tests = okTests
        self.nok_tests = notOkTests
        self.ok_subtests = okSubtests
        self.nok_subtests = notOkSubtests

    '''def SaveToFile(self, filePath):
        jsonified_object = self.__dict__
        try:
            with open(filePath) as f:
                data = json.load(f)
            data.update(jsonified_object)
        except:
            print("hdkjhfkf")

        with open(filePath, 'w') as f:
            json.dump(data, f)
        #with open(filePath, 'a+') as output:
        #    output.write("[" + x + "," + "]")'''

    def SaveToJSON(self, filePath):
        jsonified_object = self.__dict__
        try:
            with open(filePath) as f:
                data = json.load(f)
        except:
            data = {"files":[]}
        
        temp = data["files"]
        temp.append(jsonified_object)
        with open(filePath, 'w') as f:
            json.dump(data, f)


