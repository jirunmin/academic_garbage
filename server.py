# import socket
# # 建立一个服务端
# server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# host = socket.gethostname() # 获取本地主机名
# server.bind((host,9090)) #绑定要监听的端口
# server.listen(5) #开始监听 表示可以使用五个链接排队

# while True:# conn就是客户端链接过来而在服务端为期生成的一个链接实例
#     conn,addr = server.accept() #等待链接,多个链接的时候就会出现问题,其实返回了两个值
#     print(conn,addr)
#     while True:
#         data = conn.recv(1024)  #接收数据
#         print('recive:',data.decode()) #打印接收到的数据
#         conn.send(data.upper()) #然后再发送数据
#     conn.close()

import socket

# 创建一个socket：
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接：
s.connect(('www.sina.com.cn', 80))
# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

# 关闭连接:
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)