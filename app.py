import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="아기의 첫 번째 생일 초대장", 
    page_icon="🌸",
    layout="centered"
)

# 2. 스타일 설정 (전문적인 디테일 추가)
st.markdown("""
    <style>
    /* 감성적인 폰트 조합 */
    @import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Gaegu:wght@300;400&display=swap');

    /* 배경: 아주 부드러운 밀크티 핑크 */
    .stApp { background-color: #FFF5F5 !important; }
    
    /* 하단 불필요 요소 제거 */
    footer, header, #MainMenu, .stAppDeployButton, #viewerBadge {visibility: hidden; display: none !important;}

    /* 메인 타이틀: 가독성 있는 손글씨체와 자간 조절 */
    .main-title {
        font-family: 'Gaegu', cursive !important;
        color: #FF8FAB !important;
        font-size: 4.2rem !important;
        text-align: center;
        line-height: 1.1;
        margin-top: 40px;
        letter-spacing: -1px;
    }

    .sub-quote {
        font-family: 'Gowun Batang', serif !important;
        color: #B2A496 !important;
        text-align: center;
        font-size: 0.95rem !important;
        margin-top: 20px;
        margin-bottom: 40px;
        line-height: 1.6;
    }

    /* 이미지 스타일: 둥근 모서리와 은은한 글로우 효과 */
    .img-container {
        padding: 10px;
        background: white;
        border-radius: 100px 100px 20px 20px; /* 상단만 더 둥글게 해서 세련미 추가 */
        box-shadow: 0 15px 35px rgba(255, 143, 171, 0.15);
        margin-bottom: 40px;
    }

    /* 정보 박스: 투명도 있는 화이트 박스 */
    .info-card {
        background-color: rgba(255, 255, 255, 0.7) !important;
        backdrop-filter: blur(5px);
        padding: 35px 20px;
        border-radius: 30px;
        text-align: center;
        margin-bottom: 25px;
        border: 1px solid rgba(255, 143, 171, 0.2);
    }

    .info-label {
        font-family: 'Gowun Batang', serif !important;
        color: #FF8FAB !important;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 2px;
        margin-bottom: 10px;
    }

    .info-text {
        font-family: 'Gowun Batang', serif !important;
        color: #5D5D5D !important;
        font-size: 1.2rem;
        margin-bottom: 5px;
    }

    /* 버튼 스타일: 둥글고 부드러운 파스텔 톤 */
    div.stLinkButton a {
        background-color: white !important;
        color: #FF8FAB !important;
        border: 1.5px solid #FF8FAB !important;
        border-radius: 50px !important;
        padding: 10px 20px !important;
        font-family: 'Gowun Batang', serif !important;
        font-weight: 700 !important;
        font-size: 0.9rem !important;
        transition: all 0.3s;
    }
    div.stLinkButton a:hover {
        background-color: #FF8FAB !important;
        color: white !important;
        transform: translateY(-2px);
    }

    /* 배경 애니메이션: 천천히 내려오는 꽃잎 */
    @keyframes petal-fall {
        0% { transform: translateY(-10%) rotate(0deg); opacity: 0; }
        10% { opacity: 1; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
    }
    .petal {
        position: fixed; top: -5%; z-index: 0; animation: petal-fall 12s infinite linear;
        color: #FFC2D1; font-size: 20px; user-select: none;
    }
    </style>
    
    <div class="petal" style="left:10%; animation-delay:0s;">🌸</div>
    <div class="petal" style="left:30%; animation-delay:2s;">💕</div>
    <div class="petal" style="left:60%; animation-delay:6s;">🌸</div>
    <div class="petal" style="left:85%; animation-delay:4s;">✨</div>
""", unsafe_allow_html=True)

# 3. 본문 구성
st.markdown('<h1 class="main-title">아기의<br>첫 번째 생일</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-quote">소중한 우리 아기의 첫 걸음을<br>사랑하는 분들과 함께 축하하고 싶습니다.</p>', unsafe_allow_html=True)

# 이미지 프레임 (이미지는 baby.jpg)
st.markdown('<div class="img-container">', unsafe_allow_html=True)
st.image("baby.jpg", use_column_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# 정보 섹션
st.markdown("""
    <div class="info-card">
        <p class="info-label">DATE</p>
        <p class="info-text">2026년 10월 24일 토요일</p>
        <p class="info-text">오후 1시</p>
        <br>
        <p class="info-label">LOCATION</p>
        <p class="info-text"><b>행복 가든 스테이</b></p>
        <p style="font-size: 0.85rem; color: #888;">서울특별시 강남구 행복로 123</p>
    </div>
""", unsafe_allow_html=True)

# 지도 버튼
col1, col2 = st.columns(2)
with col1:
    st.link_button("카카오맵 확인", "https://map.kakao.com")
with col2:
    st.link_button("네이버 지도 확인", "https://map.naver.com")

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #FF8FAB; font-family: \'Gaegu\'; font-size: 1.1rem;">축하해 주시는 마음 잊지 않겠습니다.</p>', unsafe_allow_html=True)
