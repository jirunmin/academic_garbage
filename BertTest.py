from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity

class BERTmodel:
    def __init__(self, docs):
        self.docs = [(title, str) for title, str in docs]

        # 加载BERT模型和分词器
        model_name = "bert-base-uncased"  # 可根据需要选择不同的BERT模型
        self.tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
        self.model = BertModel.from_pretrained("bert-base-uncased")

    # 将词组列表转换为BERT嵌入
    def get_bert_embeddings(self, text):
        inputs = self.tokenizer(text, padding=True, truncation=True, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**inputs)
            embeddings = outputs.last_hidden_state.mean(dim=1)
        return embeddings
    

    def getSimilarity(self, list1, list2):
        # 获取两个词组列表的BERT嵌入
        embeddings1 = self.get_bert_embeddings(list1)
        embeddings2 = self.get_bert_embeddings(list2)

        similarity = cosine_similarity(embeddings1, embeddings2)

        return similarity[0][0]
    
    def sift(self, percent):
        n = len(self.docs)
        answer = []

        for i in range(n):
            for j in range(i+1, n):
                similarity = self.getSimilarity(self.docs[i][1], self.docs[j][1])
                if similarity >= percent/100:
                    answer.append(((self.docs[i][0], self.docs[j][0]), similarity))

        return answer

