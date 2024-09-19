from flask import Flask,render_template,request
from gensim.models import KeyedVectors
import numpy as np
import os



app = Flask(__name__)

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'chive-1.2-mc90', 'chive-1.2-mc90.txt')
model = KeyedVectors.load_word2vec_format(model_path, binary=False)



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
    target_word="夏"
    # UTF-8に変換（FlaskはデフォルトでUTF-8を使用するため特別な変換は不要）
    utf8_answer = answer  # 既にUTF-8として処理されていると仮定
    try:
        answer_vector = model[answer]
        target_vector = model[target_word]
       
    
    
    
    
    # 点数として、例えば文字数を返す（デモ用）
        similarity = np.dot(answer_vector, target_vector) / (np.linalg.norm(answer_vector) * np.linalg.norm(target_vector))
        score = max(0, 10000 - int(similarity * 10000))
    
    # プレーンテキストで返す
        return f'{score}点', 200, {'Content-Type': 'text/plain; charset=utf-8'}
    
    except KeyError as e:
        return '単語がモデルに存在しません', 400, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(debug=True)