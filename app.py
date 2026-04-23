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

/* [중요] 섬네일 버튼 영역 - 모바일 한 줄 강제 정렬 */
.thumbnail-wrapper {
    display: flex !important;
    flex-direction: row !important;
    justify-content: center !important;
    gap: 8px !important;
    margin-top: 10px;
    margin-bottom: 20px;
}

/* 섬네일 개별 버튼 스타일 */
.stButton > button {
    border: 2px solid transparent !important;
    padding: 0px !important;
    background-color: transparent !important;
    border-radius: 10px !important;
    width: 100% !important;
    aspect-ratio: 1/1 !important;
}

/* 선택된 섬네일 강조 */
.stButton > button:active, .stButton > button:focus {
    border: 2px solid #FF8FAB !important;
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

# 5. 섬네일 영역 (가로 한 줄 배치 강제)
# st.columns 대신 직접적인 가로 배치를 유도하기 위해 columns 내부 패딩을 극단적으로 줄임
cols = st.columns(len(photos))
for i, photo in enumerate(photos):
    with cols[i]:
        # 이미지 버튼 (이미지 자체를 버튼 위에 올리지 않고 버튼 클릭만 인식하게 구성)
        if st.button(f"P{i+1}", key=f"btn_{i}", use_container_width=True):
            st.session_state.photo_idx = i
            st.rerun()
        # 버튼 바로 아래에 작은 이미지 배치
        st.image(photo, use_column_width=True)

st.markdown(f"<p style='text-align: center; color: #FF8FAB; font-size: 0.7rem;'>좌측부터 사진을 눌러보세요 ( {st.session_state.photo_idx + 1} / {len(photos)} )</p>", unsafe_allow_html=True)

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
