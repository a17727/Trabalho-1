import time
import json
import os


class FileInfo:

    '''
    Each "FileInfo" Class stores file information about tests and subtests
    The class is composed by the following attributes:
         - id: file number (sequential);
         - name: file name;
         - dateTime: date and time of file processment;
         - ok_tests: number of tests with "ok" status;
         - nok_tests: number of tests with "nok" status;
         - ok_subtests: - number of subtests with "ok" status;
         - nok_subtests: - number of subtests with "nok" status;
    '''
    def __init__(self):
        self.id = None
        self.name = None
        self.dateTime = None
        self.ok_tests = None
        self.nok_tests = None
        self.ok_subtests = None
        self.nok_subtests = None

    def UpdateFileInfo(self, filesNo, filePath, okTests, notOkTests, okSubtests, notOkSubtests):
        '''
        This method adds each file info (attributes) to a class instance.

        Arguments:
            - filesNo: total number of files proccessed (sequential number);
            - filePath: path of file processed, used to get file name;
            - okTests: number of tests with "ok" status;
            - notOkTests: number of tests with "nok" status;
            - okSubtests: - number of subtests with "ok" status;
            - notOkSubtests: - number of subtests with "nok" status;
        
        "dateTime" attribute's value is equal to the local machine date and time

        '''
        
        self.id = filesNo
        self.name = os.path.basename(filePath)
        self.dateTime = time.asctime()
        self.ok_tests = okTests
        self.nok_tests = notOkTests
        self.ok_subtests = okSubtests
        self.nok_subtests = notOkSubtests


    def SaveToJSON(self, filePath):
        '''
        This method saves/appends the class instance to a JSON file:
            - if the file does not exist, it creates a JSON with information of the 1st file;
            - if the file exists, appends the information to the JSON file.

        Arguments:
            -   filePath: contains the path of the file to be created/appended.
        '''
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


