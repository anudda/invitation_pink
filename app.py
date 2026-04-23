import streamlit as st

st.set_page_config(page_title="아기 돌잔치 초대장", page_icon="🌸", layout="centered")

# CSS 최적화
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Gaegu:wght@300;400&display=swap');

.stApp { background-color: #FFF5F5 !important; }
.block-container { padding-top: 1rem !important; padding-bottom: 2rem !important; }
footer, header, #MainMenu, .stAppDeployButton, #viewerBadge {visibility: hidden; display: none !important;}

.main-title {
    font-family: 'Gaegu', cursive !important;
    color: #FF8FAB !important;
    font-size: 3.5rem !important;
    text-align: center;
    line-height: 1.1;
    margin-bottom: 5px;
}

.sub-quote {
    font-family: 'Gowun Batang', serif !important;
    color: #B2A496 !important;
    text-align: center;
    font-size: 0.9rem !important;
    margin-bottom: 25px;
}

/* 이미지 영역 보정: 배경을 투명하게 하여 흰 선 차단 */
.img-container {
    padding: 0px !important;
    background-color: transparent !important; 
    border-radius: 100px 100px 20px 20px;
    box-shadow: 0 10px 25px rgba(255, 143, 171, 0.1);
    margin-bottom: 35px;
    overflow: hidden;
    display: block;
}

div[data-testid="stImage"] > img {
    padding: 0px !important;
    margin: 0px !important;
    border-radius: 100px 100px 20px 20px;
    display: block;
}

.info-card {
    background-color: rgba(255, 255, 255, 0.7) !important;
    padding: 25px 15px;
    border-radius: 30px;
    text-align: center;
    margin-bottom: 25px;
    border: 1px solid rgba(255, 143, 171, 0.1);
}

.petal { position: fixed; top: -5%; z-index: 0; animation: petal-fall 12s infinite linear; color: #FFC2D1; font-size: 20px; }
@keyframes petal-fall { 0% { transform: translateY(-5%) rotate(0deg); opacity: 0; } 10% { opacity: 0.8; } 100% { transform: translateY(100vh) rotate(360deg); opacity: 0; } }
</style>
<div class="petal" style="left:15%; animation-delay:0s;">🌸</div>
<div class="petal" style="left:80%; animation-delay:4s;">💕</div>
""", unsafe_allow_html=True)

# 1. 상단 텍스트
st.markdown('<h1 class="main-title">아기의<br>첫 번째 생일</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-quote">소중한 우리 아기의 첫 걸음을<br>함께 축하해 주세요.</p>', unsafe_allow_html=True)

# 2. 이미지 영역 (프레임 배경 제거 완료)
st.markdown('<div class="img-container">', unsafe_allow_html=True)
st.image("baby.jpg", use_column_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# 3. 정보 섹션
st.markdown("""
<div class="info-card">
    <p style="color: #FF8FAB; font-size: 0.7rem; font-weight: 700; letter-spacing: 2px; margin-bottom: 8px;">DATE</p>
    <p style="font-family: 'Gowun Batang'; font-size: 1.1rem; color: #5D5D5D; margin-bottom: 18px;">2026년 10월 24일 (토) 오후 1시</p>
    <p style="color: #FF8FAB; font-size: 0.7rem; font-weight: 700; letter-spacing: 2px; margin-bottom: 8px;">LOCATION</p>
    <p style="font-family: 'Gowun Batang'; font-size: 1.1rem; color: #5D5D5D; margin-bottom: 4px;"><b>행복 가든 스테이</b></p>
    <p style="font-family: 'Gowun Batang'; font-size: 0.8rem; color: #999;">서울특별시 강남구 행복로 123</p>
</div>
""", unsafe_allow_html=True)

# 4. 지도 버튼 (HTML을 최소화하여 파싱 오류 방지)
button_html = """
<div style="display: flex; justify-content: center; gap: 8px; padding: 0px; width: 100%;">
    <a href="https://map.kakao.com" target="_blank" style="flex: 1; text-decoration: none; background-color: white; color: #FF8FAB; border: 1.5px solid #FF8FAB; border-radius: 50px; padding: 12px 0; font-family: 'Gowun Batang', serif; font-weight: 700; font-size: 0.8rem; text-align: center; white-space: nowrap;">카카오맵 확인</a>
    <a
