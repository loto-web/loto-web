import streamlit as st

# ==========================================
# 毎週ここを更新するだけでOK！
# ==========================================
LOTO7_DATE = "2026年5月1日 (金)"
LOTO7_NUMS = [3, 12, 17, 24, 28, 31, 35]

LOTO6_DATE = "2026年4月30日 (木)"
LOTO6_NUMS = [5, 14, 22, 29, 36, 41]

MINILOTO_DATE = "2026年4月28日 (火)"
MINILOTO_NUMS = [2, 9, 15, 23, 30]

# あなたのnote記事のURL（忘れずに！）
NOTE_URL = "https://note.com/your_account/your_article"

# ==========================================
# ページ設定とデザイン
# ==========================================
st.set_page_config(page_title="LOTO AI解析ポータル", page_icon="🎯", layout="centered")

st.markdown("""
<style>
.loto-ball {
    display: inline-block;
    width: 45px;
    height: 45px;
    border-radius: 50%;
    color: white;
    text-align: center;
    line-height: 45px;
    font-size: 18px;
    font-weight: bold;
    margin: 4px;
    box-shadow: 1px 1px 3px rgba(0,0,0,0.2);
}
.ball-loto7 { background-color: #E91E63; }
.ball-loto6 { background-color: #00BCD4; }
.ball-miniloto { background-color: #FF9800; }

.loto-section {
    padding: 20px;
    border-radius: 15px;
    background-color: #ffffff;
    border: 1px solid #eee;
    margin-bottom: 20px;
    text-align: center;
}
.premium-box {
    background-color: #fff9db;
    padding: 25px;
    border-radius: 10px;
    border: 2px solid #fab005;
    margin-top: 30px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# メインコンテンツ
# ==========================================
st.title("🎯 LOTO AI解析ポータル")
st.subheader("統計的エッジで運をハックする")

st.markdown("""
過去20年分のデータをLightGBMで解析し、各数字の**「出現期待値（パーセンテージ）」**を算出。
今週、確率の重力がかかっている数字を公開します。
""")

st.divider()

st.markdown("### 🎁 今週の無料AI予想（各1口）")

# --- LOTO 7 セクション ---
st.markdown('<div class="loto-section">', unsafe_allow_html=True)
st.markdown(f"#### 🔴 LOTO 7 ({LOTO7_DATE})")
balls_html = "".join([f'<div class="loto-ball ball-loto7">{num}</div>' for num in LOTO7_NUMS])
st.markdown(f'<div>{balls_html}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- LOTO 6 セクション ---
st.markdown('<div class="loto-section">', unsafe_allow_html=True)
st.markdown(f"#### 🔵 LOTO 6 ({LOTO6_DATE})")
balls_html = "".join([f'<div class="loto-ball ball-loto6">{num}</div>' for num in LOTO6_NUMS])
st.markdown(f'<div>{balls_html}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- ミニロト セクション ---
st.markdown('<div class="loto-section">', unsafe_allow_html=True)
st.markdown(f"#### 🟠 ミニロト ({MINILOTO_DATE})")
balls_html = "".join([f'<div class="loto-ball ball-miniloto">{num}</div>' for num in MINILOTO_NUMS])
st.markdown(f'<div>{balls_html}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.caption("※無料枠はAI推奨パターンのうちの1つです。")

# ==========================================
# 有料エリア誘導
# ==========================================
st.markdown('<div class="premium-box">', unsafe_allow_html=True)
st.markdown("### 🔥 【完全版】AI解析データを手に入れる")
st.markdown(f"""
有料記事では、AIが算出した最新の解析結果をすべて公開しています。

1. **出現期待値ランキング（上位20個）**
   - LOTO7 / LOTO6 / ミニロトそれぞれの「今週出やすい数字」を、AIの解析パーセンテージと共にリストアップ。
2. **AI推奨・最強5パターン**
   - 上位20個の数字を最適に組み合わせた、期待値最大化5パターンを全種類網羅。

自力で迷うより、**AIが導き出した上位20個の数字**を軸に戦略を立ててみませんか？
今なら3種セット特別価格で公開中です。
""")

st.link_button("👉 【期間限定100円】AI解析・完全版データを見る", NOTE_URL, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

st.divider()
st.caption("免責事項：本解析は当選を保証するものではありません。購入は自己責任でお願いいたします。")
