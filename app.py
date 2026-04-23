import streamlit as st

st.set_page_config(page_title="아기 돌잔치 초대장", layout="centered")

# 전문적인 스타일링 (Pretendard 폰트와 뮤트톤 활용)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@200;400;700&family=Noto+Sans+KR:wght@100;400&display=swap');

    /* 배경색: 고급스러운 샌드 베이지 */
    .stApp { background-color: #F9F7F2 !important; }
    
    footer, header, #MainMenu, .stAppDeployButton, #viewerBadge {visibility: hidden; display: none !important;}

    /* 타이틀: 고급스러운 세리프체 */
    .main-title {
        font-family: 'Noto Serif KR', serif !important;
        color: #5D5D5D !important;
        font-size: 2.2rem !important;
        text-align: center;
        letter-spacing: 5px;
        margin-top: 60px;
        font-weight: 200;
    }

    .sub-title {
        font-family: 'Noto Sans KR', sans-serif !important;
        color: #A68E74 !important;
        text-align: center;
        font-size: 0.9rem !important;
        letter-spacing: 3px;
        margin-bottom: 40px;
    }

    /* 이미지 프레임 스타일 */
    .img-frame {
        border: 1px solid #E0DED7;
        padding: 15px;
        background-color: white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        margin-bottom: 50px;
    }

    /* 정보 섹션: 정돈된 느낌 */
    .info-section {
        text-align: center;
        font-family: 'Noto Sans KR', sans-serif !important;
        color: #5D5D5D !important;
        line-height: 2.2;
    }

    .info-label { color: #A68E74 !important; font-size: 0.8rem; letter-spacing: 2px; }
    .info-value { font-size: 1.1rem; font-weight: 400; margin-bottom: 20px; }

    /* 버튼 스타일: 깔끔한 라인 버튼 */
    div.stLinkButton a {
        background-color: transparent !important;
        color: #5D5D5D !important;
        border: 1px solid #D1CFC7 !important;
        border-radius: 0px !important;
        font-size: 0.8rem !important;
        transition: all 0.3s;
    }
    div.stLinkButton a:hover {
        background-color: #5D5D5D !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# 상단 텍스트
st.markdown('<p class="main-title">INVITATION</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">아기의 첫 번째 생일</p>', unsafe_allow_html=True)

# 이미지 출력 (프레임 효과 적용)
st.markdown('<div class="img-frame">', unsafe_allow_html=True)
st.image("baby.jpg", use_column_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# 본문 정보
st.markdown("""
    <div class="info-section">
        <p class="info-label">DATE</p>
        <p class="info-value">2026년 10월 24일 오후 1시</p>
        <p class="info-label">LOCATION</p>
        <p class="info-value">더 플라자 호텔 지스텀하우스</p>
        <p style="font-size: 0.8rem; color: #888;">서울특별시 중구 태평로2가 23</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# 지도 버튼
col1, col2 = st.columns(2)
with col1:
    st.link_button("NAVER MAP", "https://map.naver.com")
with col2:
    st.link_button("KAKAO MAP", "https://map.kakao.com")

# 하단 멘트
st.markdown("""
    <p style="text-align: center; color: #A68E74; font-size: 0.8rem; margin-top: 80px; letter-spacing: 1px;">
        마음을 담아 초대합니다.
    </p>
""", unsafe_allow_html=True)
