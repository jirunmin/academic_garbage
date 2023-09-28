class KGramHash:
    def __init__(self, k, string):
        # 初始化KGramHash对象，指定k值和输入字符串
        self.k = k
        self.document = string
        self.shingleHash = {}  # 存储shingle的哈希映射
        self.init_hash_value()  # 调用初始化哈希值的方法

    def init_hash_value(self):
        # 初始化shingle的哈希值映射
        self.shingleHash = {
            ("aLOAD", "invokespecial", "return"): 1,
            ("iLOAD", "iPUSH", "iIFCMP"): 2,
            ("iPUSH", "iIFCMP", "iLOAD"): 3,
            ("iIFCMP", "iLOAD", "iRETURN"): 4,
            ("iLOAD", "iRETURN", "iLOAD"): 5,
            ("iRETURN", "iLOAD", "iPUSH"): 6,
            ("iLOAD", "iPUSH", "iSUB"): 7,
            ("iPUSH", "iSUB", "invokestatic"): 8,
            ("iSUB", "invokestatic", "iLOAD"): 9,
            ("invokestatic", "iLOAD", "iPUSH"): 10,
            ("iSUB", "invokestatic", "iADD"): 11,
            ("invokestatic", "iADD", "iRETURN"): 12,
            ("iPUSH", "iLOAD", "iIFCMP"): 13,
            ("iLOAD", "iIFCMP", "iPUSH"): 14,
            ("iIFCMP", "iPUSH", "iLOAD"): 15,
            ("iPUSH", "iLOAD", "iADD"): 16,
            ("iLOAD", "iADD", "invokestatic"): 17,
            ("iADD", "invokestatic", "iPUSH"): 18,
            ("invokestatic", "iPUSH", "iLOAD"): 19,
            ("iADD", "invokestatic", "iADD"): 20,
            ("iADD", "iRETURN", "iLOAD"): 21,
            ("iRETURN", "iLOAD", "iRETURN"): 22,
            ("invokestatic", "iADD", "GOTO"): 23,
            ("iADD", "GOTO", "iLOAD"): 24,
            ("GOTO", "iLOAD", "iRETURN"): 25,
            ("invokespecial", "return", "iLOAD"): 0,
            ("return", "iLOAD", "iPUSH"): 0,
            ("iPUSH", "iIFCMP", "iPUSH"): 0,
        }

    def get_hashes(self):
        # 获取输入字符串中每个shingle的哈希值
        n = len(self.document)
        hashes = [self.shingleHash[tuple(self.document[i:i+self.k])] for i in range(n - self.k + 1)]
        return hashes

    def extract(self, W):
        # 提取具有最小哈希值的shingle的索引和哈希值
        hashes = self.get_hashes()
        n = len(hashes)

        selected = []
        q = [0] * n
        hh, tt = 0, -1

        for i in range(n):
            if hh <= tt and i - W + 1 > q[hh]:
                hh += 1

            while hh <= tt and hashes[q[tt]] >= hashes[i]:
                tt -= 1

            tt += 1
            q[tt] = i

            if i >= W - 1:
                if len(selected) == 0 or q[hh] != selected[-1][0]:
                    selected.append((q[hh], hashes[q[hh]]))

        return selected
