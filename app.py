import streamlit as st
import base64

st.set_page_config(page_title="🌸 아기의 첫 번째 생일 파티에 초대합니다", page_icon="👶", layout="centered")

def get_video_base64(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except: return None

# 스타일 설정
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&family=Gamja+Flower&display=swap');
    .stApp { background-color: #fffaf0 !important; }
    footer, header, #MainMenu, .stAppDeployButton, #viewerBadge {visibility: hidden; display: none !important;}
    
    h1 { font-family: 'Nanum Pen Script', cursive !important; color: #e91e63 !important; font-size: 3.8rem !important; text-align: center; line-height: 1.1; }
    h3, p, span, b, div { font-family: 'Gamja Flower', cursive !important; color: #8d6e63 !important; }
    .info-box { background-color: #ffffff !important; padding: 25px; border-radius: 20px; box-shadow: 2px 5px 15px rgba(233, 30, 99, 0.1); text-align: center; margin-bottom: 25px; border: 1px solid #fce4ec; }
    
    div[data-testid="column"]:nth-of-type(1) div.stLinkButton a { background-color: #FEE500 !important; color: #3C1E1E !important; border: none !important; }
    div[data-testid="column"]:nth-of-type(2) div.stLinkButton a { background-color: #03C75A !important; color: white !important; border: none !important; }

    @keyframes hearts-fall { 0% { top: -10%; } 100% { top: 100%; } }
    .heart { position: fixed; top: -10%; z-index: 0; animation: hearts-fall 10s linear infinite; color: #ffb7c5; opacity: 0.6; font-size: 25px; user-select: none; }
    </style>
    <div class="heart" style="left:10%; animation-delay:0s;">❤</div>
    <div class="heart" style="left:50%; animation-delay:4s;">🌸</div>
    <div class="heart" style="left:80%; animation-delay:2s;">✨</div>
""", unsafe_allow_html=True)

st.markdown("<h1>아기의<br>첫 번째 생일 🎂</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.5rem;'>꽃보다 예쁜 아기의<br>첫 돌잔치에 초대합니다 🌸</p>", unsafe_allow_html=True)

# 1. 파일을 읽어서 데이터로 변환 (파일명 확인!)
image_data = get_image_base64("baby.jpg") 

# 2. 만약 데이터를 성공적으로 가져왔다면?
if image_data:
    # 3. HTML 태그를 사용해 화면에 그리기
    st.markdown(
        f'''
        <img src="data:image/jpeg;base64,{image_data}" 
             style="width: 100%; border-radius: 20px;">
        ''', 
        unsafe_allow_html=True
    )
    
st.markdown("""
    <div class='info-box'>
        <h3>📅 일시</h3>
        <p style='font-size: 1.4rem; font-weight: bold;'>2026년 10월 24일 (토) 오후 1시</p>
    </div>
    <div class='info-box'>
        <h3>📍 장소</h3>
        <p style='font-size: 1.1rem;'><b>행복 호텔 라일락홀</b></p>
        <p style='font-size: 0.9rem;'>서울특별시 강남구 행복로 123</p>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1: st.link_button("💛 카카오맵", "https://map.kakao.com", use_container_width=True)
with col2: st.link_button("💚 네이버 지도", "https://map.naver.com", use_container_width=True)
