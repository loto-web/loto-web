import streamlit as st

# ==========================================
# 毎週ここを更新するだけでサイトが変わります！
# ==========================================
# --- LOTO7 の設定（7個） ---
LOTO7_DATE = "2026年5月1日 (金)"
LOTO7_NUMS = [3, 12, 17, 24, 28, 31, 35]

# --- LOTO6 の設定（6個） ---
LOTO6_DATE = "2026年4月30日 (木)"
LOTO6_NUMS = [5, 14, 22, 29, 36, 41]

# --- ミニロト の設定（5個） ---
MINILOTO_DATE = "2026年4月28日 (火)"
MINILOTO_NUMS = [2, 9, 15, 23, 30]

# --- note記事のURL ---
NOTE_URL = "https://note.com/your_account/your_article"

# ==========================================
# ページ設定とカスタムデザイン
# ==========================================
st.set_page_config(page_title="LOTO AI解析エンジン", page_icon="🎯", layout="centered")

st.markdown("""
<style>
.loto-ball {
    display: inline-block;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    color: white;
    text-align: center;
    line-height: 50px;
    font-size: 20px;
    font-weight: bold;
    margin: 6px;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
}
.ball-loto7 { background-color: #E91E63; } /* ピンク系 */
.ball-loto6 { background-color: #00BCD4; } /* 水色系 */
.ball-miniloto { background-color: #FF9800; } /* オレンジ系 */

.premium-box {
    background-color: #f8f9fa;
    padding: 25px;
    border-radius: 10px;
    border-left: 6px solid #FFD700; /* ゴールド */
    margin-top: 30px;
    margin-bottom: 20px;
}
.center-text {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# メインコンテンツ
# ==========================================
st.title("🎯 LOTO AI解析エンジン")
st.subheader("データサイエンスで「運」をハックする")

st.markdown("""
過去20年分の全データをLightGBMで解析し、「平均への回帰」と「出現インターバル」から次回の当たり数字を予測。
完全ランダムな期待値を超えるエッジ（優位性）を追求するAIエンジンです。
""")

st.divider()

st.markdown(f"<h3 class='center-text'>🎁 今週の無料AI予想（1口）</h3>", unsafe_allow_html=True)

# ==========================================
# タブ切り替えエリア
# ==========================================
tab1, tab2, tab3 = st.tabs(["🔴 LOTO7", "🔵 LOTO6", "🟠 ミニロト"])

with tab1:
    st.markdown(f"<p class='center-text'>次回抽選日: {LOTO7_DATE}</p>", unsafe_allow_html=True)
    balls_html = "".join([f'<div class="loto-ball ball-loto7">{num}</div>' for num in LOTO7_NUMS])
    st.markdown(f'<div class="center-text">{balls_html}</div>', unsafe_allow_html=True)

with tab2:
    st.markdown(f"<p class='center-text'>次回抽選日: {LOTO6_DATE}</p>", unsafe_allow_html=True)
    balls_html = "".join([f'<div class="loto-ball ball-loto6">{num}</div>' for num in LOTO6_NUMS])
    st.markdown(f'<div class="center-text">{balls_html}</div>', unsafe_allow_html=True)

with tab3:
    st.markdown(f"<p class='center-text'>次回抽選日: {MINILOTO_DATE}</p>", unsafe_allow_html=True)
    balls_html = "".join([f'<div class="loto-ball ball-miniloto">{num}</div>' for num in MINILOTO_NUMS])
    st.markdown(f'<div class="center-text">{balls_html}</div>', unsafe_allow_html=True)

st.caption("※無料公開枠は、AIが算出した推奨パターンのうちの1つです。")

# ==========================================
# note誘導エリア（プレミアム枠）
# ==========================================
st.markdown('<div class="premium-box">', unsafe_allow_html=True)
st.markdown("### 🔥 【期間限定100円】全種類の最強AI予想を見る")
st.markdown("""
AIは毎回の抽選に対し、**最も期待値の高いスコア上位5パターン**を算出しています。

現在、**「LOTO7」「LOTO6」「ミニロト」全3種の完全版予想（上位5パターン×3種 ＝ 計15パターン）をセットにして、リリース記念の特別価格【100円】**で公開中です！（※実績が出次第、本来の299円に値上げ予定）

本気でエッジを効かせたい方は、値上げ前に今週の【完全版】推奨ナンバーを取得してください。
""")

# 大きなリンクボタン（noteへ誘導）
st.link_button("👉 3種セット！AI予想【完全版】を見る (noteへ) ¥100", NOTE_URL, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# フッター
# ==========================================
st.divider()
st.caption("免責事項：本AIは過去データの統計的優位性に基づく予測を提供するものであり、当選を確約するものではありません。宝くじの購入は自己責任でお願いいたします。")
