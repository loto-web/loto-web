import streamlit as st

# ==========================================
# 毎週ここを更新するだけでサイトが変わります！
# ==========================================
DRAW_DATE = "2026年5月1日 (金)"       # 次回の抽選日
FREE_NUMBERS = [5, 12, 18, 24, 31]  # 今週の無料予想（1口分）
NOTE_URL = "https://note.com/your_account/your_article" # あなたのnote記事のURL

# ==========================================
# ページ設定とカスタムデザイン
# ==========================================
st.set_page_config(page_title="LOTO AI解析エンジン", page_icon="🎯", layout="centered")

# LOTOのボール風デザインと、プレミアム枠のCSS
st.markdown("""
<style>
.loto-ball {
    display: inline-block;
    width: 55px;
    height: 55px;
    border-radius: 50%;
    background-color: #FF5722; /* ボールの色 */
    color: white;
    text-align: center;
    line-height: 55px;
    font-size: 24px;
    font-weight: bold;
    margin: 8px;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
}
.premium-box {
    background-color: #f8f9fa;
    padding: 25px;
    border-radius: 10px;
    border-left: 6px solid #E91E63;
    margin-top: 40px;
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
完全ランダムな期待値（1.324個）に対し、厳格な検証テストで**平均1.44個の優位性（エッジ）**を記録。
過去20年分の全データをLightGBMで解析し、「平均への回帰」と「出現インターバル」から次回の当たり数字を予測するAIエンジンです。
""")

st.divider()

# --- 無料予想エリア ---
st.markdown(f"<h2 class='center-text'>🎁 今週の無料AI予想</h2>", unsafe_allow_html=True)
st.markdown(f"<p class='center-text'>次回抽選日: {DRAW_DATE}</p>", unsafe_allow_html=True)

# ボールのHTMLを生成して中央揃えで表示
balls_html = "".join([f'<div class="loto-ball">{num}</div>' for num in FREE_NUMBERS])
st.markdown(f'<div class="center-text">{balls_html}</div>', unsafe_allow_html=True)

st.caption("※無料公開枠は、AIが算出した推奨パターンのうちの1つです。")

# --- note誘導エリア（プレミアム枠） ---
st.markdown('<div class="premium-box">', unsafe_allow_html=True)
st.markdown("### 🔥 さらに確率を高めたい方へ")
st.markdown("""
AIは毎回の抽選に対し、**最も期待値の高いスコア上位5パターン**を算出しています。
1口だけの購入より、AIが推奨する5パターンを網羅することで、エッジ（優位性）を最大限に活かすことができます。

本気で当選を狙う方は、今週の【完全版】推奨ナンバーを以下から取得してください。
""")

# 大きなリンクボタン（noteへ誘導）
st.link_button("👉 AI予想【完全版】上位5パターンを見る (noteへ) ¥299", NOTE_URL, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# フッター
# ==========================================
st.divider()
st.caption("免責事項：本AIは過去データの統計的優位性に基づく予測を提供するものであり、当選を確約するものではありません。宝くじの購入は自己責任でお願いいたします。")