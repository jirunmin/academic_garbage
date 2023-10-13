import copy
class KGramHash:
    def __init__(self, k, string, operationHash):
        # 初始化KGramHash对象，指定k值和输入字符串
        self.k = k
        self.document = copy.deepcopy(string)
        self.document.insert(0, " ")
        self.operationHash = operationHash
        self.hvalue = [0]
        self.pvalue = [1]
        self.base = 2
        self.mod = 2 ** 64
        self.init_hash_value(operationHash)  # 调用初始化哈希值的方法


    def init_hash_value(self, operationHash):
        for i in range(1, len(self.document)):
            self.hvalue.append(self.hvalue[i-1]*self.base + operationHash[self.document[i]])
            self.pvalue.append(self.pvalue[i-1]*self.base)

    def get_hash_value(self, lposition, rposition):
        return self.hvalue[rposition] - self.hvalue[lposition-1] * self.pvalue[rposition-lposition+1]
    

    def get_hashes(self):
        hashes = []
        
        for i in range(self.k, len(self.document)):
            hashes.append(self.get_hash_value(i-self.k+1, i))

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

        return selected, hashes
