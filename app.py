import streamlit as st
import base64

# 1. 페이지 설정
st.set_page_config(page_title="지연이의 돌잔치에 초대합니다", page_icon="🎂", layout="centered")

# [함수] 이미지 변환 도구
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(open(image_path, "rb").read()).decode()
    except: return ""

# 2. 스타일 설정 (여백 및 모바일 1행 강제)
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Gaegu:wght@300;400&display=swap');

.stApp {{ background-color: #FFF5F5 !important; }}
.block-container {{ padding-top: 1.5rem !important; padding-bottom: 0px !important; }}

/* 요소 간 간격 최소화 */
div[data-testid="stVerticalBlock"] {{ gap: 0.5rem !important; }}

footer, header, #MainMenu {{visibility: hidden; display: none !important;}}

.main-title {{ font-family: 'Gaegu', cursive !important; color: #FF8FAB !important; font-size: 2.8rem !important; text-align: center; line-height: 1.2; margin-bottom: 0; }}
.sub-quote {{ font-family: 'Gowun Batang', serif !important; color: #B2A496 !important; text-align: center; font-size: 0.9rem !important; margin-bottom: 10px; }}

/* [핵심] 모바일에서도 컬럼이 아래로 떨어지지 않게 강제 */
div[data-testid="stHorizontalBlock"] {{
    display: flex !important;
    flex-direction: row !important;
    flex-wrap: nowrap !important;
    align-items: flex-end !important;
    justify-content: center !important;
    gap: 8px !important;
}}
div[data-testid="column"] {{
    flex: 1 1 0% !important;
    min-width: 0 !important;
}}

/* 버튼 내부 P1 등 글자 숨기기 */
.stButton button {{
    border: none !important;
    padding: 0px !important;
    background: transparent !important;
    color: transparent !important;
}}
.stButton button p {{ display: none !important; }}

.petal {{ position: fixed; top: -5%; z-index: 0; animation: petal-fall 12s infinite linear; color: #FFC2D1; font-size: 20px; pointer-events: none; }}
@keyframes petal-fall {{ 0% {{ transform: translateY(-5%) rotate(0deg); opacity: 0; }} 10% {{ opacity: 0.8; }} 100% {{ transform: translateY(100vh) rotate(360deg); opacity: 0; }} }}
</style>
<div class="petal" style="left:15%; animation-delay:0s;">🌸</div>
<div class="petal" style="left:80%; animation-delay:4s;">💕</div>
""", unsafe_allow_html=True)

# 3. 타이틀
st.markdown('<h1 class="main-title">지연이의<br>첫 생일 🎂</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-quote">지연이의 첫 돌잔치에 초대합니다.</p>', unsafe_allow_html=True)

# 4. 사진 데이터 및 세션 관리
photos = ["baby.jpg", "baby1.jpg", "baby2.jpg", "baby3.jpg"]
if 'photo_idx' not in st.session_state:
    st.session_state.photo_idx = 0

# 5. 메인 이미지 (프레임 없이 직각으로)
st.image(photos[st.session_state.photo_idx], use_container_width=True)

# 6. 썸네일 (모바일 1행 강제 버전)
cols = st.columns(len(photos))
for i in range(len(photos)):
    with cols[i]:
        # 이미지 비율을 유지하면서 클릭 가능하게 만듦
        if st.button(" ", key=f"btn_{i}", use_container_width=True):
            st.session_state.photo_idx = i
            st.rerun()
        st.image(photos[i], use_container_width=True)

# 카운터 표시
st.markdown(f"<p style='text-align: center; color: #FF8FAB; font-size: 0.8rem; font-weight: bold; margin-top: -10px;'>{st.session_state.photo_idx + 1} / {len(photos)}</p>", unsafe_allow_html=True)

# 7. 정보 섹션 (여백 없이 쫀득하게 붙음)
st.markdown("""
<div style="background-color: rgba(255, 255, 255, 0.8); padding: 25px 15px; border-radius: 35px; text-align: center; border: 1px solid rgba(255, 143, 171, 0.12); box-shadow: 0 10px 20px rgba(255, 143, 171, 0.05); margin-top: 10px;">
    <p style="color: #FF8FAB; font-size: 0.7rem; font-weight: 700; letter-spacing: 2px; margin-bottom: 5px; font-family: 'Gowun Batang';">DATE</p>
    <p style="font-family: 'Gowun Batang'; font-size: 1.15rem; color: #4A4A4A; margin-bottom: 18px;">2026년 10월 24일 (토) 오후 1시</p>
    <p style="color: #FF8FAB; font-size: 0.7rem; font-weight: 700; letter-spacing: 2px; margin-bottom: 5px; font-family: 'Gowun Batang';">LOCATION</p>
    <p style="font-family: 'Gowun Batang'; font-size: 1.1rem; color: #4A4A4A; margin-bottom: 4px;"><b>행복 가든 스테이</b></p>
    <p style="font-family: 'Gowun Batang'; font-size: 0.8rem; color: #888;">서울특별시 강남구 행복로 123</p>
</div>
""", unsafe_allow_html=True)

# 8. 지도 버튼
st.markdown("""
<div style="display: flex; justify-content: center; gap: 10px; width: 100%; margin-top: 15px;">
    <a href="https://map.kakao.com" target="_blank" style="flex: 1; text-decoration: none; background: white; color: #FF8FAB; border: 1.5px solid #FF8FAB; border-radius: 50px; padding: 12px 0; font-family: 'Gowun Batang'; font-weight: 700; font-size: 0.85rem; text-align: center;">카카오맵 확인</a>
    <a href="https://map.naver.com" target="_blank" style="flex: 1; text-decoration: none; background: white; color: #FF8FAB; border: 1.5px solid #FF8FAB; border-radius: 50px; padding: 12px 0; font-family: 'Gowun Batang'; font-weight: 700; font-size: 0.85rem; text-align: center;">네이버 지도 확인</a>
</div>
<p style='text-align: center; color: #FF8FAB; font-family: "Gaegu"; font-size: 1.1rem; margin-top: 30px;'>지연이의 첫 생일을 축하해 주셔서 감사합니다.</p>
""", unsafe_allow_html=True)
