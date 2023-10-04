from Call import *

class Run:
    def __init__(self, folderName, threshold, type):
        self.type = type
        self.folderName = folderName
        self.threshold = threshold

    def setType(self, type):
        self.type = type

    
    def run(self):
        self.type.call(self.folderName, self.threshold)