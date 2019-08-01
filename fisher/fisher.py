from flask import Flask, make_response

app = Flask(__name__)
# 加载配置文件config.py
app.config.from_object('config')

@app.route('/hello/')  # 通过装饰器注册路由
def hello():
    # status code 200, 404, 301
    # content-type http headers
    # content-type: text/html
    # Response
    # 基于类的视图（即插视图）
    headers = {
        'content-type': 'text/plain',
        'location': 'https://www.baidu.com'
    }
    # response = make_response('<html></html>', 301)
    # response.headers = headers
    # return response
    return '<html></html>', 301, headers

# 另一种路由注册方法
# app.add_url_rule('/hello', view_func=hello)

if __name__ == '__main__':
    # 打开调试模式，代码修改保存后，服务会自动重启
    app.run(host='0.0.0.0', port=5001, debug=app.config['DEBUG'])



