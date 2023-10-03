import socket
import time
import threading
import pickle
from MainProcedure import MainProcedure


# 创建基于IPv4和TCP协议的Socket：
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
s.bind(('127.0.0.1', 9999))

s.listen(5)
print('Waiting for connection...')

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data:
            break

        # 反序列化接收到的数据
        received_data = pickle.loads(data)

        # 调用相似度检测函数
        folderName = received_data['folderName']
        threshold = received_data['threshold']
        
        o = MainProcedure(folderName)
        result = o.start(int(threshold))
        # 将结果发送回客户端
        response_data = {'result': 1}
        response = pickle.dumps(response_data)
        sock.send(response)
        # sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))

    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

