import http.server
import socketserver
import json
from urllib.parse import parse_qs
from MainProcedure import MainProcedure

# 创建一个HTTP请求处理程序
class SimilarityCheckerHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        # 解析HTTP POST请求的内容
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        post_params = parse_qs(post_data.decode('utf-8'))

        
        if 'folderName' in post_params and 'threshold' in post_params:
            folderName = post_params['folderName'][0]
            threshold = post_params['threshold'][0]

            o = MainProcedure(folderName)
            result = o.start(int(threshold))

            # 构建响应JSON数据
            response_data = {'result': result}

            # 发送HTTP响应
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
        else:
            # 如果请求参数不完整，返回错误响应
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'Bad Request: Missing folderName or threshold')

# 创建一个HTTP服务器
port = 8080  # 指定端口
httpd = socketserver.TCPServer(('', port), SimilarityCheckerHandler)

print(f'Starting HTTP server on port {port}...')
httpd.serve_forever()
