from MainProcedure import MainProcedure
import socket
import pickle
import subprocess
import time
import requests

class CallAPI:
    def call(self, folderName, threshold):
        pass

class LocalCall(CallAPI):
    def call(self, folderName, threshold):
        o = MainProcedure(folderName)
        result = o.start(threshold)
        for (key, similarity) in result:
            print(key, ": ", '{:.3%}'.format(similarity))  

class TCPCall(CallAPI):
    def __init__(self, server_host, server_port):
        python_program_path = "TCPserver.py"
        cmd = f"start cmd /k python {python_program_path}"
        self.process = subprocess.Popen(cmd, shell=True)

        time.sleep(2)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 建立连接:
        self.s.connect((server_host, server_port))

    def get_response(self, folderName, threshold):
        data_to_send = {'folderName': folderName, 'threshold': str(threshold)}
        # 序列化数据并发送给服务器
        data_to_send_serialized = pickle.dumps(data_to_send)
        self.s.send(data_to_send_serialized)

        # 接收服务器的响应
        response_data_serialized = self.s.recv(1024)

        # 反序列化响应数据
        response_data = pickle.loads(response_data_serialized)

        return response_data['result']

    def call(self, folderName, threshold):
        result = self.get_response(folderName, threshold)
        for (key, similarity) in result:
            print(key, ": ", '{:.3%}'.format(similarity))  

        self.s.close()
        self.process.terminate()


class UDPCall(CallAPI):
    def __init__(self, server_host, server_port):
        python_program_path = "UDPserver.py"
        cmd = f"start cmd /k python {python_program_path}"
        self.process = subprocess.Popen(cmd, shell=True)

        time.sleep(4)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_host = server_host
        self.server_port = server_port

    def get_response(self, folderName, threshold):
        data_to_send = {'folderName': folderName, 'threshold': str(threshold)}
        # 序列化数据并发送给服务器
        data_to_send_serialized = pickle.dumps(data_to_send)
        self.s.sendto(data_to_send_serialized, (self.server_host, self.server_port))

        # 接收服务器的响应
        response_data_serialized, server_address = self.s.recvfrom(1024)

        # 反序列化响应数据
        response_data = pickle.loads(response_data_serialized)

        return response_data['result']

    def call(self, folderName, threshold):
        result = self.get_response(folderName, threshold)
        for (key, similarity) in result:
            print(key, ": ", '{:.3%}'.format(similarity))  

        self.s.close()
        self.process.terminate()


class HTTPCall(CallAPI):
    def __init__(self, url):
        python_program_path = "HTTPserver.py"
        cmd = f"start cmd /k python {python_program_path}"
        self.process = subprocess.Popen(cmd, shell=True)

        time.sleep(2)
        self.url = url

    def call(self, folderName, threshold):
        # 构建POST请求数据
        data = {'folderName': folderName,'threshold': str(threshold)}

        # 发送POST请求
        response = requests.post(self.url, data=data)

        # 检查响应
        if response.status_code == 200:
            result = response.json()
            resultAns = result['result']
            for (key, similarity) in resultAns:
                print(key, ": ", '{:.3%}'.format(similarity))
        else:
            print(f'HTTP Error: {response.status_code}')
            print(response.text)

        self.process.terminate()


class WebServiceCall(CallAPI):
    def __init__(self, url):
        python_program_path = "WebServiceserver.py"
        cmd = f"start cmd /k python {python_program_path}"
        self.process = subprocess.Popen(cmd, shell=True)

        time.sleep(2)
        self.url = url

    def call(self, folderName, threshold):
        # 构建POST请求数据
        data = {'folderName': folderName,'threshold': str(threshold)}

        # 发送POST请求到WebService接口
        response = requests.post(self.url, json=data)

        # 处理HTTP响应
        if response.status_code == 200:
            result = response.json()
            resultAns = result['result']
            for (key, similarity) in resultAns:
                print(key, ": ", '{:.3%}'.format(similarity))
        else:
            print("HTTP请求失败")

        self.process.terminate()