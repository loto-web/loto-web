import streamlit as st

# ==========================================
# 毎週ここを更新：AI解析データ（数字: 期待値%）
# 順序は気にせず入力して大丈夫です（自動でソートされます）
# ==========================================
# LOTO7 (5/1 金曜分)
LOTO7_DATE = "2026年5月1日 (金)"
LOTO7_DATA = {
    4: 30.3, 6: 43.2, 19: 31.7, 22: 25.7, 26: 30.6, 33: 29.0, 36: 26.3
}

# LOTO6 (4/30 木曜分)
LOTO6_DATE = "2026年4月30日 (木)"
LOTO6_DATA = {
    20: 23.4, 22: 22.1, 24: 22.4, 25: 20.0, 41: 22.5, 43: 19.7
}

# ミニロト (4/28 火曜分)
MINILOTO_DATE = "2026年4月28日 (火)"
MINILOTO_DATA = {
    7: 22.5, 12: 38.7, 17: 29.9, 23: 28.2, 26: 48.1
}

# あなたのnote記事のURLをここに貼り付けてください
NOTE_URL = "https://note.com/loto_yosoku/n/n4f8a28409abd"

# ==========================================
# ページ設定とデザイン（CSS）
# ==========================================
st.set_page_config(page_title="LOTO AI解析ポータル", page_icon="🎯", layout="centered")

st.markdown("""
<style>
.ball-container {
    display: inline-block;
    margin: 8px;
    text-align: center;
}
.loto-ball {
    width: 45px;
    height: 45px;
    border-radius: 50%;
    color: white;
    text-align: center;
    line-height: 45px;
    font-size: 18px;
    font-weight: bold;
    margin: 0 auto;
    box-shadow: 1px 1px 4px rgba(0,0,0,0.3);
}
.prob-text {
    font-size: 13px;
    font-weight: 600;
    color: #444;
    margin-top: 5px;
}
.ball-loto7 { background-color: #E91E63; } /* LOTO7: ピンク */
.ball-loto6 { background-color: #00BCD4; } /* LOTO6: 水色 */
.ball-miniloto { background-color: #FF9800; } /* ミニロト: オレンジ */

.loto-section {
    padding: 25px 20px;
    border-radius: 15px;
    background-color: #ffffff;
    border: 1px solid #ddd;
    margin-bottom: 25px;
    text-align: center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}
.loto-title {
    font-size: 20px;
    font-weight: bold;
    color: #333;
    margin-bottom: 15px;
    margin-top: 0;
}
.premium-box {
    background-color: #fff9db;
    padding: 25px;
    border-radius: 12px;
    border: 2px solid #fab005;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# ボール描画用の共通関数
# ==========================================
def render_balls(data_dict, ball_class):
    # データを確率（値）で降順（高い順）にソート
    sorted_data = sorted(data_dict.items(), key=lambda x: x[1], reverse=True)
    
    html = '<div style="display: flex; justify-content: center; flex-wrap: wrap;">'
    for num, prob in sorted_data:
        html += f'<div class="ball-container"><div class="loto-ball {ball_class}">{num}</div><div class="prob-text">{prob}%</div></div>'
    html += '</div>'
    return html

# ==========================================
# メインコンテンツ
# ==========================================
st.title("🎯 LOTO AI解析ポータル")
st.subheader("統計的エッジで「確率の重力」を可視化する")

st.markdown("""
過去20年分のデータを機械学習（LightGBM）で解析。
「平均への回帰」と「出現インターバル」から、AIが今週最も期待値の高まっている数字とパーセンテージを算出しました。
（左から確率が高い順に並べています）
""")

st.divider()

st.markdown("### 🎁 今週の無料AI予想（期待値上位1口分）")
st.caption("※各LOTOの出現期待値ランキングにおけるトップ数字を組み合わせた「本命」パターンです。")

# ==========================================
# HTMLを完全に1行に繋げて出力（謎の黄色い□を物理的に防止）
# ==========================================

# LOTO 7 セクション
html_loto7 = f'<div class="loto-section"><div class="loto-title">🔴 LOTO 7 ({LOTO7_DATE})</div>{render_balls(LOTO7_DATA, "ball-loto7")}</div>'
st.markdown(html_loto7, unsafe_allow_html=True)

# LOTO 6 セクション
html_loto6 = f'<div class="loto-section"><div class="loto-title">🔵 LOTO 6 ({LOTO6_DATE})</div>{render_balls(LOTO6_DATA, "ball-loto6")}</div>'
st.markdown(html_loto6, unsafe_allow_html=True)

# ミニロト セクション
html_miniloto = f'<div class="loto-section"><div class="loto-title">🟠 ミニロト ({MINILOTO_DATE})</div>{render_balls(MINILOTO_DATA, "ball-miniloto")}</div>'
st.markdown(html_miniloto, unsafe_allow_html=True)

# ==========================================
# 有料エリア誘導（プレミアム枠）
# ==========================================
# ここも1行で記述して安全対策
html_premium = f'<div class="premium-box"><h3>🔥 【全LOTO対応】AI解析データ・完全版</h3><p>有料記事（note）では、AIが算出した最新の解析フルデータをすべて公開しています。</p><p>1. <strong>出現期待値ランキング（各LOTO 上位20個）</strong><br> - 無料枠でお見せしたパーセンテージの「残り13個分」の全貌を公開。<br>2. <strong>AI推奨・最強5パターン</strong><br> - 上位20個の数字を最適に組み合わせた、期待値最大化の5パターン（本命・対抗・中穴・分散・大穴）を網羅。</p><p>自力で迷う時間を、AIの確かなデータに変えてみませんか？<br><strong>現在、3種セット特別価格【100円】で公開中です。</strong></p></div>'
st.markdown(html_premium, unsafe_allow_html=True)

st.link_button("👉 AI解析データ・完全版（note）はこちら", NOTE_URL, use_container_width=True)

st.divider()
st.caption("免責事項：本解析は統計学的な予測であり、当選を保証するものではありません。購入に関する最終決定は自己責任でお願いいたします。")
