def slurp(filePath):
    '''
    Method used to read file into the lexer.
    Arguments:
        - filePath: path of the file to be processed
    '''
    fh = open(filePath, mode="r")
    contents = fh.read()
    fh.close()
    return contents

def GetTreeLevel(nodeID):
    '''
    This auxuliar method is used o get the tree level to add a subtest node, based on the identation.
    Each 4 spaces corresponds to 1 level.

    Argument:
        - nodeID: idented id of the subtest node used to get tree level, based on identation. 
    '''
    return int((len(nodeID) - len(nodeID.lstrip()))/4)



    
