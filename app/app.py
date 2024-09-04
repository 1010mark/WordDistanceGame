from flask import Flask,render_template

from gensim.models import KeyedVectors
from gensim.similarities import Similarity
import numpy as np

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
    
    # UTF-8に変換（FlaskはデフォルトでUTF-8を使用するため特別な変換は不要）
    utf8_answer = answer  # 既にUTF-8として処理されていると仮定
    
    # 点数として、例えば文字数を返す（デモ用）
    score = len(utf8_answer)
    
    # プレーンテキストで返す
    return f'{score}点', 200, {'Content-Type': 'text/plain; charset=utf-8'}

def load_model(model_path):
    """
    Load a pre-trained Word2Vec model from the specified path.
    """
    model = KeyedVectors.load_word2vec_format(model_path, binary=True)
    return model

def calculate_similarity(model, word1, word2):
    """
    Calculate the cosine similarity between two words using the Word2Vec model.
    """
    if word1 in model and word2 in model:
        vector1 = model[word1]
        vector2 = model[word2]
        similarity = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
        return similarity
    else:
        raise ValueError(f"One or both of the words '{word1}' and '{word2}' are not in the vocabulary.")

def get_score(similarity):
    """
    Convert the similarity score to a point score.
    Similarity closer to 1 means a smaller score.
    """
    # Normalize similarity to a score between 0 and 10000
    score = 10000-similarity * 10000
    return score

def main():
    model_path = 'path/to/word2vec_model.bin'  # 訓練済みモデルのパスを指定
    model = load_model(model_path)

    sent_word = 'sent_word_example'  # 送られてきた単語
    target_word = 'target_word_example'  # お題の単語

    try:
        similarity = calculate_similarity(model, sent_word, target_word)
        score = get_score(similarity)
        print(f"Similarity between '{sent_word}' and '{target_word}': {similarity:.2f}")
        print(f"Score: {score:.2f}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    app.run(debug=True)