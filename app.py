#テンプレート

from flask import Flask,render_template

app = Flask(__name__) # インスタンス生成

@app.route('/') # URLを指定

def hello_world():
    return 'Hello World!'

@app.route('/next')

def next():
    return 'next page'

@app.route('/sample')
def sample():
    return render_template('index.html')


# if __name__ == "__main__":
    # app.run(debug=True) # サーバー起動
    