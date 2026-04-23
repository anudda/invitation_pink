import streamlit as st

# 1. 페이지 설정 (탭 제목 수정 완료! ✨)
st.set_page_config(
    page_title="지연이의 돌잔치에 초대합니다", 
    page_icon="🎂", 
    layout="centered"
)

# 2. CSS 스타일 최적화
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

/* 이미지 영역: 흰 선 차단 및 둥근 프레임 */
.img-container {
    padding: 0px !important;
    background-color: transparent !important; 
    border-radius: 100px 100px 20px 20px;
    box-shadow: 0 10px 25px rgba(255, 143, 171, 0.15);
    margin-bottom: 15px;
    overflow: hidden;
    display: flex;
    justify-content: center;
}

div[data-testid="stImage"] > img {
    border-radius: 100px 100px 20px 20px;
}

/* 사진 목록(라디오 버튼) 커스텀 */
div[data-testid="stRadio"] div[role="radiogroup"] {
    justify-content: center;
    gap: 10px;
}
div[data-testid="stRadio"] label {
    background-color: white !important;
    border: 1px solid #FF8FAB !important;
    color: #FF8FAB !important;
    border-radius: 50px !important;
    padding: 3px 12px !important;
    font-size: 0.8rem !important;
    font-family: 'Gowun Batang' !important;
}

.info-card {
    background-color: rgba(255, 255, 255, 0.7) !important;
    padding: 25px 15px;
    border-radius: 30px;
    text-align: center;
    margin-top: 25px;
    margin-bottom: 25px;
    border: 1px solid rgba(255, 143, 171, 0.1);
}

.petal { position: fixed; top: -5%; z-index: 0; animation: petal-fall 12s infinite linear; color: #FFC2D1; font-size: 20px; pointer-events: none; }
@keyframes petal-fall { 0% { transform: translateY(-5%) rotate(0deg); opacity: 0; } 10% { opacity: 0.8; } 100% { transform: translateY(100vh) rotate(360deg); opacity: 0; } }
</style>
<div class="petal" style="left:15%; animation-delay:0s;">🌸</div>
<div class="petal" style="left:80%; animation-delay:4s;">💕</div>
""", unsafe_allow_html=True)

# 3. 본문 구성 (지연)
st.markdown('<h1 class="main-title">지연이의<br>첫 번째 생일 🎂</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-quote">세상에서 가장 소중한 지연이의<br>첫 돌잔치에 초대합니다.</p>', unsafe_allow_html=True)

# 4. 사진 구성 (대표사진: baby.jpg / 나머지: 1.jpg, 2.jpg...)
photos = ["baby.jpg", "1.jpg", "2.jpg", "3.jpg"] 

# 슬라이더 선택 (숫자 대신 '갤러리'로 깔끔하게)
selected_photo_idx = st.radio("갤러리", range(len(photos)), horizontal=True, label_visibility="collapsed")

# 사진 출력 영역
st.markdown('<div class="img-container">', unsafe_allow_html=True)
st.image(photos[selected_photo_idx], use_column_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# 사진 번호 표시
st.markdown(f"<p style='text-align: center; color: #FF8FAB; font-size: 0.8rem; margin-top: -10px;'>{selected_photo_idx + 1} / {len(photos)}</p>", unsafe_allow_html=True)

# 5. 정보 섹션
st.markdown("""
<div class="info-card">
    <p style="color: #FF8FAB; font-size: 0.7rem; font-weight: 700; letter-spacing: 2px; margin-bottom: 8px;">DATE</p>
    <p style="font-family: 'Gowun Batang'; font-size: 1.1rem; color: #5D5D5D; margin-bottom: 18px;">2026년 10월 24일 (토) 오후 1시</p>
    <p style="color: #FF8FAB; font-size: 0.7rem; font-weight: 700; letter-spacing: 2px; margin-bottom: 8px;">LOCATION</p>
    <p style="font-family: 'Gowun Batang'; font-size: 1.1rem; color: #5D5D5D; margin-bottom: 4px;"><b>행복 가든 스테이</b></p>
    <p style="font-family: 'Gowun Batang'; font-size: 0.8rem; color: #999;">서울특별시 강남구 행복로 123</p>
</div>
""", unsafe_allow_html=True)

# 6. 지도 버튼
button_html = '<div style="display: flex; justify-content: center; gap: 10px; padding: 0 5px; margin-top: 10px; width: 100%;"><a href="https://map.kakao.com" target="_blank" style="flex: 1; text-decoration: none; background-color: white; color: #FF8FAB; border: 1.5px solid #FF8FAB; border-radius: 50px; padding: 12px 0; font-family: \'Gowun Batang\', serif; font-weight: 700; font-size: 0.8rem; text-align: center; white-space: nowrap; display: inline-block;">카카오맵 확인</a><a href="https://map.naver.com" target="_blank" style="flex: 1; text-decoration: none; background-color: white; color: #FF8FAB; border: 1.5px solid #FF8FAB; border-radius: 50px; padding: 12px 0; font-family: \'Gowun Batang\', serif; font-weight: 700; font-size: 0.8rem; text-align: center; white-space: nowrap; display: inline-block;">네이버 지도 확인</a></div>'
st.markdown(button_html, unsafe_allow_html=True)

st.markdown("<br><p style='text-align: center; color: #FF8FAB; font-family: \"Gaegu\"; font-size: 1.1rem;'>지연이의 첫 생일을 축하해 주셔서 감사합니다.</p>", unsafe_allow_html=True)
