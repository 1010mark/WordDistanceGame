from flask import Flask,render_template,request
from fuzzywuzzy import fuzz




app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play")
def play():
    return render_template("play.html")

@app.route('/score', methods=['GET'])
def score():
    # クエリパラメータ 'answer' を取得
    answer = request.args.get('answer', '')
    target_word="summer"
    
    
    # UTF-8に変換（FlaskはデフォルトでUTF-8を使用するため特別な変換は不要）
    utf8_answer = answer  # 既にUTF-8として処理されていると仮定
    
    # 点数として、例えば文字数を返す（デモ用）
    similarity=fuzz.ratio(answer.lower(), target_word.lower())
    score = max(0, 10000- similarity*100)
    
    # プレーンテキストで返す
    return f'{score}点', 200, {'Content-Type': 'text/plain; charset=utf-8'}




if __name__ == "__main__":
    app.run(debug=True)