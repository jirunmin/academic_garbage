import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))

data_to_send = {'folderName': "Code", 'threshold': "50"}
# 序列化数据并发送给服务器
data_to_send_serialized = pickle.dumps(data_to_send)
s.send(data_to_send_serialized)

# 接收服务器的响应
response_data_serialized = s.recv(1024)

# 反序列化响应数据
response_data = pickle.loads(response_data_serialized)

# 处理相似度检测结果
result = response_data['result']
print(result)

#s.send(b'exit')
s.close()
# # 接收欢迎消息:
# print(s.recv(1024).decode('utf-8'))
# for data in [b'Michael', b'Tracy', b'Sarah']:
#     # 发送数据:
#     s.send(data)
#     print(s.recv(1024).decode('utf-8'))
# s.send(b'exit')
# s.close()