from MainProcedure import MainProcedure
import socket
import pickle
import subprocess

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
        python_program_path = "server.py"
        cmd = f"start cmd /k python {python_program_path}"
        self.process = subprocess.Popen(cmd, shell=True)

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

        try:
            self.process.wait()

        except KeyboardInterrupt:
            # 用户按下 Ctrl+C，捕获 KeyboardInterrupt 异常
            print("服务器关闭")
