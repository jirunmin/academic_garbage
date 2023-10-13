from Detect import Detect
from ReadCode import ReadCode
from BertTest import BERTmodel
import os



class MainProcedure:
    def __init__(self, folderName):
        self.operationHash = {}
        self.idx = 0
        self.folderName = folderName
        self.out_folder = os.path.join(self.folderName, "out")

        if not os.path.exists(self.out_folder):
            os.mkdir(self.out_folder)

    def update(self, operation):
        if operation not in self.operationHash:
            self.operationHash[operation] = self.idx
            self.idx += 1

    def load_folder(self):
        folder_path = self.folderName
        file_extension = ".java"

        # 用于存储匹配的文件列表
        matching_files = []

        # 遍历文件夹
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(file_extension):
                    matching_files.append((os.path.splitext(file)[0], os.path.join(root, file)))

        return matching_files


    def get_documents(self, files):
        strs = []
        for title, file in files:
            o = ReadCode(file, self.out_folder)
            operations = o.extract()
            for operation in operations:
                self.update(operation)
            # print(operations)
            strs.append((title, operations))

        return strs

    def start(self, threshold):
        docs = self.get_documents(self.load_folder())

        o = Detect(docs, 3, 4, self.operationHash)
        ans = o.sift(threshold)

        # other = BERTmodel(docs)
        # otherans = other.sift(threshold)

        # for (key, similarity) in otherans:
        #     print(key, ": ", '{:.3%}'.format(similarity))  

        self.delete_file(self.out_folder)

        return ans

    def delete_file(self, folder_to_delete):
        # 遍历文件夹中的所有文件和子文件夹
        for root, dirs, files in os.walk(folder_to_delete):
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)  # 删除文件

        os.rmdir(folder_to_delete)

# o = MainProcedure("Code")
# o.start(64)