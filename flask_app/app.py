from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # 日本百名山のデータ
    mountains = [
        {"name": "富士山", "elevation": "3776m", "location": "山梨県・静岡県", "active": "はい", "difficulty": "中級"},
        {"name": "北岳", "elevation": "3193m", "location": "山梨県", "active": "いいえ", "difficulty": "中級"},
        {"name": "奥穂高岳", "elevation": "3190m", "location": "長野県・岐阜県", "active": "いいえ", "difficulty": "上級"},
        {"name": "槍ヶ岳", "elevation": "3180m", "location": "長野県", "active": "いいえ", "difficulty": "上級"},
        {"name": "白馬岳", "elevation": "2932m", "location": "長野県・富山県", "active": "いいえ", "difficulty": "中級"},
        {"name": "甲斐駒ヶ岳", "elevation": "2967m", "location": "山梨県・長野県", "active": "いいえ", "difficulty": "中級"},
        {"name": "立山", "elevation": "3015m", "location": "富山県", "active": "いいえ", "difficulty": "中級"},
        {"name": "赤岳", "elevation": "2899m", "location": "長野県・山梨県", "active": "いいえ", "difficulty": "中級"},
        {"name": "薬師岳", "elevation": "2926m", "location": "富山県", "active": "いいえ", "difficulty": "中級"},
        {"name": "蓼科山", "elevation": "2531m", "location": "長野県", "active": "いいえ", "difficulty": "初級"},
        # ここに続けて百名山すべてを追加rrr
        {"name": "恵那山", "elevation": "2191m", "location": "岐阜県・長野県", "active": "いいえ", "difficulty": "初級"},
        {"name": "荒川岳", "elevation": "3141m", "location": "静岡県", "active": "いいえ", "difficulty": "上級"},
        {"name": "笠ヶ岳", "elevation": "2898m", "location": "岐阜県", "active": "いいえ", "difficulty": "上級"},
        {"name": "西穂高岳", "elevation": "2909m", "location": "岐阜県・長野県", "active": "いいえ", "difficulty": "上級"},
        {"name": "御嶽山", "elevation": "3067m", "location": "長野県・岐阜県", "active": "はい", "difficulty": "中級"},
        {"name": "美ヶ原", "elevation": "2034m", "location": "長野県", "active": "いいえ", "difficulty": "初級"},
        {"name": "白山", "elevation": "2702m", "location": "石川県・岐阜県", "active": "いいえ", "difficulty": "中級"},
        {"name": "乗鞍岳", "elevation": "3026m", "location": "長野県・岐阜県", "active": "はい", "difficulty": "中級"},
        {"name": "焼岳", "elevation": "2455m", "location": "長野県・岐阜県", "active": "はい", "difficulty": "中級"},
        {"name": "木曽駒ヶ岳", "elevation": "2956m", "location": "長野県", "active": "いいえ", "difficulty": "中級"},
        # 残りの山を順次追加…
        # 完成時にすべて100山を記載
    ]
    return render_template("index.html", mountains=mountains)

if __name__ == "__main__":
    app.run(debug=True)
