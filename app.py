import streamlit as st

st.set_page_config(page_title="아기 돌잔치 초대장", page_icon="🌸", layout="centered")

# CSS 수정 (상단 여백 제거 및 버튼 정렬 보정)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Gaegu:wght@300;400&display=swap');

    .stApp { background-color: #FFF5F5 !important; }
    
    /* 상단 여백 최소화 */
    .block-container { padding-top: 2rem !important; padding-bottom: 2rem !important; }
    footer, header, #MainMenu, .stAppDeployButton, #viewerBadge {visibility: hidden; display: none !important;}

    .main-title {
        font-family: 'Gaegu', cursive !important;
        color: #FF8FAB !important;
        font-size: 4rem !important;
        text-align: center;
        line-height: 1.1;
        margin-bottom: 0px; /* 타이틀 하단 여백 제거 */
    }

    .sub-quote {
        font-family: 'Gowun Batang', serif !important;
        color: #B2A496 !important;
        text-align: center;
        font-size: 0.9rem !important;
        margin-top: 10px;
        margin-bottom: 30px;
    }

    /* 이미지 컨테이너: 상단 여백 없이 꽉 차게 */
    .img-container {
        padding: 5px; /* 내부 여백 축소 */
        background: white;
        border-radius: 100px 100px 20px 20px;
        box-shadow: 0 10px 25px rgba(255, 143, 171, 0.1);
        margin-bottom: 40px;
        line-height: 0; /* 이미지 하단 미세 여백 제거 */
    }

    .info-card {
        background-color: rgba(255, 255, 255, 0.7) !important;
        padding: 30px 20px;
        border-radius: 30px;
        text-align: center;
        margin-bottom: 30px;
        border: 1px solid rgba(255, 143, 171, 0.1);
    }

    /* 버튼 정렬 보정: 두 버튼이 동일한 너비로 좌우 대칭 */
    div[data-testid="column"] {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    div.stLinkButton {
        width: 100% !important;
        display: flex;
        justify-content: center;
    }

    div.stLinkButton a {
        width: 90% !important; /* 버튼 너비를 90%로 고정해 균형 유지 */
        background-color: white !important;
        color: #FF8FAB !important;
        border: 1.5px solid #FF8FAB !important;
        border-radius: 50px !important;
        font-family: 'Gowun Batang', serif !important;
        font-weight: 700 !important;
        text-align: center;
        font-size: 0.85rem !important;
    }

    /* 배경 애니메이션 */
    @keyframes petal-fall {
        0% { transform: translateY(-5%) rotate(0deg); opacity: 0; }
        10% { opacity: 0.8; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
    }
    .petal { position: fixed; top: -5%; z-index: 0; animation: petal-fall 12s infinite linear; color: #FFC2D1; font-size: 20px; }
    </style>
    
    <div class="petal" style="left:15%; animation-delay:0s;">🌸</div>
    <div class="petal" style="left:80%; animation-delay:4s;">💕</div>
""", unsafe_allow_html=True)

# 3. 본문 구성
st.markdown('<h1 class="main-title">아기의<br>첫 번째 생일</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-quote">소중한 우리 아기의 첫 걸음을<br>함께 축하해 주세요.</p>', unsafe_allow_html=True)

# 이미지 영역 (상단 여백 제거된 컨테이너)
st.markdown('<div class="img-container">', unsafe_allow_html=True)
st.image("baby.jpg", use_column_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# 정보 섹션
st.markdown("""
    <div class="info-card">
        <p style="color: #FF8FAB; font-size: 0.75rem; font-weight: 700; letter-spacing: 2px; margin-bottom: 10px;">DATE</p>
        <p style="font-family: 'Gowun Batang'; font-size: 1.15rem; color: #5D5D5D; margin-bottom: 20px;">2026년 10월 24일 (토) 오후 1시</p>
        <p style="color: #FF8FAB; font-size: 0.75rem; font-weight: 700; letter-spacing: 2px; margin-bottom: 10px;">LOCATION</p>
        <p style="font-family: 'Gowun Batang'; font-size: 1.15rem; color: #5D5D5D; margin-bottom: 5px;"><b>행복 가든 스테이</b></p>
        <p style="font-family: 'Gowun Batang'; font-size: 0.85rem; color: #999;">서울특별시 강남구 행복로 123</p>
    </div>
""", unsafe_allow_html=True)

# 4. 지도 버튼 (비율 1:1 대칭 정렬)
col1, col2 = st.columns(2)
with col1:
    st.link_button("카카오맵 확인
