import requests

# 定义接口的URL
url = 'http://localhost:8080'  # 换成实际的服务器地址和端口


# 构建POST请求数据
data = {
    'folderName': "Code",
    'threshold': "64"
}

# 发送POST请求
response = requests.post(url, data=data)

# 检查响应
if response.status_code == 200:
    result = response.json()
    resultAns = result['result']
    for (key, similarity) in resultAns:
        print(key, ": ", '{:.3%}'.format(similarity))
else:
    print(f'HTTP Error: {response.status_code}')
    print(response.text)
