from MainProcedure import MainProcedure

class CallAPI:
    def call(self, folderName, threshold):
        pass

class LocalCall(CallAPI):
    def call(self, folderName, threshold):
        o = MainProcedure(folderName)
        result = o.start(threshold)
        for (key, similarity) in result:
            print(key, ": ", '{:.3%}'.format(similarity))  

