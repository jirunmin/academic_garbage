from KGramHash import KGramHash
from Detect import Detect
from ReadCode import ReadCode
import os

operationHash = {}
idx = 0

def update(operation):
    global idx
    if operation not in operationHash:
        operationHash[operation] = idx
        idx += 1

def load_folder(folderName):
    folder_path = folderName
    file_extension = ".java"

    # 用于存储匹配的文件列表
    matching_files = []

    # 遍历文件夹
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(file_extension):
                matching_files.append((os.path.splitext(file)[0], os.path.join(root, file)))

    return matching_files


def get_documents(files):
    strs = []
    for title, file in files:
        o = ReadCode(file)
        operations = o.extract()
        for operation in operations:
            update(operation)
        strs.append((title, operations))

    return strs

o = Detect(get_documents(load_folder("Code")), 3, 4, operationHash)
o.get_pairwise()

# 定义要删除的文件夹路径
folder_to_delete = "Code\out"

# 遍历文件夹中的所有文件和子文件夹
for root, dirs, files in os.walk(folder_to_delete):
    for file in files:
        file_path = os.path.join(root, file)
        os.remove(file_path)  # 删除文件