import socket
import pickle
from MainProcedure import MainProcedure

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind(('127.0.0.1', 9997))

print('Bind UDP on 9997...')
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    # 反序列化接收到的数据
    received_data = pickle.loads(data)

    # 调用相似度检测函数
    folderName = received_data['folderName']
    threshold = received_data['threshold']
    o = MainProcedure(folderName)
    result = o.start(int(threshold))
    

    # 将结果发送回客户端
    response_data = {'result': result}
    response = pickle.dumps(response_data)
    s.sendto(response, addr)

    print('Result has send to %s:%s.' % addr)