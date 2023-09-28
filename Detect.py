from KGramHash import KGramHash

class Detect:
    def __init__(self, docs, k, W, operationHash):
        # 初始化Detect对象，传入文档列表docs、k值和W值
        self.docs = [(title, str) for title, str in docs]  # 将文档列表重新组织为(title, document)元组列表
        self.k = k  # k值用于KGram哈希
        self.W = W  # W值用于匹配
        self.operationHash = operationHash
        self.index = {}  # 存储哈希值和文档对应关系的索引
        self.hashes_output = {}
        self.extract_output = {}
        self.init_index()  # 调用初始化索引的方法

    def init_index(self):
        # 初始化索引，建立哈希值和文档对应关系
        for title, document in self.docs:
            obj = KGramHash(self.k, document, self.operationHash)  # 创建KGramHash对象
            H, hashes = obj.extract(self.W)  # 提取文档的哈希值
            self.hashes_output[title] = hashes
            self.extract_output[title] = H
            for u, v in H:
                if v not in self.index:
                    self.index[v] = [(title, u)]  # 如果哈希值不存在于索引中，创建一个新的条目
                else:
                    self.index[v].append((title, u))  # 如果哈希值已存在，将文档信息添加到对应的列表中

    def match(self):
        # 执行文档匹配，找到匹配的文档对
        matches = {}  # 存储匹配结果的字典
        H = []  # 存储所有文档的哈希值
        for title, document in self.docs:
            selected = self.extract_output[title]
            matches[title] = []  # 初始化匹配结果列表
            for u, v in selected:
                H.append((title, u, v))  # 将文档的哈希值添加到H中

        for title, u, v in H:
            for value in self.index[v]:  # 查找索引中与哈希值v匹配的文档
                if value[0] != title and (value[0], value[1], v) not in matches[title]:
                    matches[title].append((value[0], value[1], v))  # 将匹配的文档信息添加到匹配结果中

        return matches  # 返回匹配结果字典

    def get_pairwise(self):
        # 获取匹配的文档对
        matches = self.match()  # 执行匹配
        pairwise = {}  # 存储文档对和匹配信息的字典
        for d1 in matches:
            for d2, u, v in matches[d1]:
                key = (d1, d2) if d1 < d2 else (d2, d1)  # 确保文档对的顺序一致
                if key not in pairwise:
                    pairwise[key] = [(d2, u, v)]  # 创建新的文档对条目
                else:
                    pairwise[key].append((d2, u, v))  # 将匹配信息添加到文档对的列表中

        for key, value in pairwise.items():
            size1 = len(self.hashes_output[key[0]])
            size2 = len(self.hashes_output[key[1]])
            similarity = len(value) / max(size1, size2)
            print(key, ": ", '{:.2%}'.format(similarity))  # 打印文档对和匹配信息


