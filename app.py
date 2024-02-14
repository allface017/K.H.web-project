#テンプレート

from flask import Flask,render_template

app = Flask(__name__) # インスタンス生成

@app.route('/') # URLを指定


@app.route('/')
def sample():
    return render_template('index.html')

@app.route('/work')
def work():
    return render_template('Workflow.html')

if __name__ == "__main__":
    app.run(debug=True) 
    # サーバー起動
    