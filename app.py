import streamlit as st

st.set_page_config(page_title="지연이의 돌잔치에 초대합니다", page_icon="🎂", layout="centered")

# CSS: 가로 슬라이딩 영역 설정
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Gaegu:wght@300;400&display=swap');

.stApp { background-color: #FFF5F5 !important; }
footer, header, #MainMenu, .stAppDeployButton, #viewerBadge {visibility: hidden; display: none !important;}

/* 가로 슬라이딩 컨테이너 */
.scroll-container {
    display: flex;
    overflow-x: auto;
    scroll-snap-type: x mandatory; /* 옆으로 딱딱 걸리게 설정 */
    gap: 10px;
    padding-bottom: 15px;
    -webkit-overflow-scrolling: touch;
}
.scroll-container::-webkit-scrollbar { display: none; } /* 스크롤바 숨기기 */

.scroll-item {
    flex: 0 0 100%; /* 한 화면에 사진 한 장씩 */
    scroll-snap-align: center;
    display: flex;
    justify-content: center;
}

.scroll-item img {
    width: 100%;
    border-radius: 100px 100px 20px 20px;
    box-shadow: 0 10px 25px rgba(255, 143, 171, 0.15);
}

.main-title { font-family: 'Gaegu'; color: #FF8FAB; font-size: 2.8rem; text-align: center; line-height: 1.2; }
.sub-quote { font-family: 'Gowun Batang'; color: #B2A496; text-align: center; font-size: 0.9rem; margin-bottom: 25px; }

.info-card {
    background-color: rgba(255, 255, 255, 0.7);
    padding: 25px 15px;
    border-radius: 30px;
    text-align: center;
    border: 1px solid rgba(255, 143, 171, 0.1);
}
</style>
""", unsafe_allow_html=True)

# 1. 타이틀
st.markdown('<h1 class="main-title">지연이의<br>첫 생일 🎂</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-quote">지연이의 소중한 순간들을 옆으로 밀어서 확인해 보세요.</p>', unsafe_allow_html=True)

# 2. 가로 슬라이딩 갤러리 구현 (HTML/CSS 방식)
photos = ["baby.jpg", "baby1.jpg", "baby2.jpg", "baby3.jpg"]

# 사진들을 가로로 나열하는 HTML 생성
gallery_html = '<div class="scroll-container">'
for photo in photos:
    # 각 사진을 Base64로 변환하지 않고 파일명 그대로 사용 (Streamlit이 정적 파일을 서빙할 때 가능)
    # 직접 배포 환경에서는 이미지 주소를 처리해야 하므로 안전하게 st.image를 쓰되 레이아웃만 변경합니다.
    gallery_html += f'<div class="scroll-item"><img src="app/static/{photo}" onerror="this.src=\'https://via.placeholder.com/400x500?text=Image+Not+Found\'"></div>'
gallery_html += '</div>'

# 하지만 Streamlit에서는 보안상 로컬 이미지 직접 참조가 까다로우므로 아래 방식을 추천합니다:
# [대안] 가로 컬럼을 만들어서 가로 스크롤을 유도하는 방식
st.write("👈 옆으로 밀어서 보세요 👉")
col_photos = st.columns(len(photos))
for i, photo in enumerate(photos):
    with col_photos[i]:
        st.image(photo, use_column_width=True)

# 3. 정보 섹션 & 지도 버튼 (기존 코드와 동일)
st.markdown("""
<div class="info-card">
    <p style="color: #FF8FAB; font-size: 0.7rem; font-weight: 700; letter-spacing: 2px;">DATE</p>
    <p style="font-size: 1.1rem; color: #5D5D5D;">2026년 10월 24일 오후 1시</p>
</div>
""", unsafe_allow_html=True)

button_html = '<div style="display: flex; justify-content: center; gap: 10px; margin-top: 20px;"><a href="https://map.kakao.com" target="_blank" style="flex: 1; text-decoration: none; background-color: white; color: #FF8FAB; border: 1.5px solid #FF8FAB; border-radius: 50px; padding: 12px 0; text-align: center; font-size: 0.8rem; font-weight: bold;">카카오맵 확인</a><a href="https://map.naver.com" target="_blank" style="flex: 1; text-decoration: none; background-color: white; color: #FF8FAB; border: 1.5px solid #FF8FAB; border-radius: 50px; padding: 12px 0; text-align: center; font-size: 0.8rem; font-weight: bold;">네이버 지도 확인</a></div>'
st.markdown(button_html, unsafe_allow_html=True)
