from flask import Flask, request, jsonify
from MainProcedure import MainProcedure

app = Flask(__name__)

# 定义WebService接口，使用POST方法接收源代码数据
@app.route('/similarity', methods=['POST'])
def calculate_similarity():
    try:
        # 从HTTP请求中获取源代码数据
        data = request.get_json()
        folderName = data['folderName']
        threshold = data['threshold']

        o = MainProcedure(folderName)
        result = o.start(int(threshold))

        response_data = {'result': result}
        return jsonify(response_data), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

app.run(host='127.0.0.1', port=8080)
