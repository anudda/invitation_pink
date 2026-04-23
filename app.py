import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="지연이의 돌잔치에 초대합니다", 
    page_icon="🎂", 
    layout="centered"
)

# 2. 스타일 및 레이아웃 설정
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Gaegu:wght@300;400&display=swap');

.stApp { background-color: #FFF5F5 !important; }
.block-container { padding-top: 1rem !important; padding-bottom: 2rem !important; }
footer, header, #MainMenu, .stAppDeployButton, #viewerBadge {visibility: hidden; display: none !important;}

.main-title {
    font-family: 'Gaegu', cursive !important;
    color: #FF8FAB !important;
    font-size: 2.8rem !important;
    text-align: center;
    line-height: 1.2;
}

.sub-quote {
    font-family: 'Gowun Batang', serif !important;
    color: #B2A496 !important;
    text-align: center;
    font-size: 0.9rem !important;
    margin-bottom: 25px;
}

/* 메인 이미지 박스 */
.img-container {
    padding: 0px !important;
    border-radius: 100px 100px 20px 20px;
    box-shadow: 0 10px 25px rgba(255, 143, 171, 0.15);
    margin-bottom: 15px;
    overflow: hidden;
    display: flex;
    justify-content: center;
}
div[data-testid="stImage"] > img { border-radius: 100px 100px 20px 20px; }

/* 섬네일 영역: 모바일에서도 무조건 가로 1행 유지 */
.thumb-row {
    display: flex !important;
    flex-wrap: nowrap !important;
    justify-content: center !important;
    gap: 10px !important;
    margin-bottom: 20px !important;
    width: 100% !important;
}

/* 개별 섬네일 이미지 버튼 스타일 */
.thumb-btn {
    flex: 0 0 20% !important; /* 4장일 때 약 20%씩 차지 */
    aspect-ratio: 1/1 !important;
    border-radius: 10px !important;
    cursor: pointer !important;
    border: 2px solid transparent;
    transition: 0.2s;
    object-fit: cover !important;
}

.info-card {
    background-color: rgba(255, 255, 255, 0.7) !important;
    padding: 25px 15px;
    border-radius: 30px;
    text-align: center;
    margin-bottom: 25px;
    border: 1px solid rgba(255, 143, 171, 0.1);
}

.petal { position: fixed; top: -5%; z-index: 0; animation: petal-fall 12s infinite linear; color: #FFC2D1; font-size: 20px; pointer-events: none; }
@keyframes petal-fall { 0% { transform: translateY(-5%) rotate(0deg); opacity: 0; } 10% { opacity: 0.8; } 100% { transform: translateY(100vh) rotate(360deg); opacity: 0; } }
</style>
<div class="petal" style="left:15%; animation-delay:0s;">🌸</div>
<div class="petal" style="left:80%; animation-delay:4s;">💕</div>
""", unsafe_allow_html=True)

# 3. 본문 타이틀
st.markdown('<h1 class="main-title">지연이의<br>첫 생일 🎂</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-quote">지연이의 첫 돌잔치에 초대합니다.</p>', unsafe_allow_html=True)

# 4. 사진 갤러리 로직
photos = ["baby.jpg", "baby1.jpg", "baby2.jpg", "baby3.jpg"]

if 'photo_idx' not in st.session_state:
    st.session_state.photo_idx = 0

# 메인 이미지 출력
st.markdown('<div class="img-container">', unsafe_allow_html=True)
st.image(photos[st.session_state.photo_idx], use_column_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# 5. [핵심] 섬네일 버튼 (st.columns 대신 콤팩트한 radio 활용)
# Streamlit에서 모바일 한 줄을 유지하는 가장 깔끔한 방법은 radio를 이미지처럼 속이는 것입니다.
st.markdown("<p style='text-align: center; color: #FF8FAB; font-size: 0.7rem; margin-bottom: 10px;'>사진을 선택해 보세요 👇</p>", unsafe_allow_html=True)

# 라디오 버튼을 활용해 클릭 이벤트와 정렬을 동시에 해결
selected_photo = st.radio(
    "gallery",
    range(len(photos)),
    horizontal=True,
    label_visibility="collapsed",
    format_func=lambda x: f"사진 {x+1}"
)

# 라디오 버튼 선택 시 세션 업데이트 및 반영
if selected_photo != st.session_state.photo_idx:
    st.session_state.photo_idx = selected_photo
    st.rerun()

# 6. 정보 섹션
st.markdown("""
<div class="info-card">
    <p style="color: #FF8FAB; font-size: 0.7rem; font-weight: 700; letter-spacing: 2px; margin-bottom: 8px;">DATE</p>
    <p style="font-family: 'Gowun Batang'; font-size: 1.1rem; color: #5D5D5D; margin-bottom: 18px;">2026년 10월 24일 (토) 오후 1시</p>
    <p style="color: #FF8FAB; font-size: 0.7rem; font-weight: 700; letter-spacing: 2px; margin-bottom: 8px;">LOCATION</p>
    <p style="font-family: 'Gowun Batang'; font-size: 1.1rem; color: #5D5D5D; margin-bottom: 4px;"><b>행복 가든 스테이</b></p>
    <p style="font-family: 'Gowun Batang'; font-size: 0.8rem; color: #999;">서울특별시 강남구 행복로 123</p>
</div>
""", unsafe_allow_html=True)

# 7. 지도 버튼
button_html = '<div style="display: flex; justify-content: center; gap: 8px; width: 100%;"><a href="https://map.kakao.com" target="_blank" style="flex: 1; text-decoration: none; background-color: white; color: #FF8FAB; border: 1.5px solid #FF8FAB; border-radius: 50px; padding: 12px 0; font-family: \'Gowun Batang\', serif; font-weight: 700; font-size: 0.8rem; text-align: center; white-space: nowrap; display: inline-block;">카카오맵 확인</a><a href="https://map.naver.com" target="_blank" style="flex: 1; text-decoration: none; background-color: white; color: #FF8FAB; border: 1.5px solid #FF8FAB; border-radius: 50px; padding: 12px 0; font-family: \'Gowun Batang\', serif; font-weight: 700; font-size: 0.8rem; text-align: center; white-space: nowrap; display: inline-block;">네이버 지도 확인</a></div>'
st.markdown(button_html, unsafe_allow_html=True)

st.markdown("<br><p style='text-align: center; color: #FF8FAB; font-family: \"Gaegu\"; font-size: 1.1rem;'>지연이의 첫 생일을 축하해 주셔서 감사합니다.</p>", unsafe_allow_html=True)
