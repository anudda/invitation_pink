import streamlit as st
import streamlit.components.v1 as components

# 1. 페이지 설정
st.set_page_config(page_title="지연이의 돌잔치에 초대합니다", page_icon="🎂", layout="centered")

# 2. 기본 스타일 (배경 및 꽃잎)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Gaegu:wght@300;400&display=swap');
.stApp { background-color: #FFF5F5 !important; }
.block-container { padding-top: 1rem !important; }
footer, header, #MainMenu {visibility: hidden; display: none !important;}

.main-title { font-family: 'Gaegu', cursive; color: #FF8FAB; font-size: 2.8rem; text-align: center; line-height: 1.2; margin-bottom: 0; }
.sub-quote { font-family: 'Gowun Batang', serif; color: #B2A496; text-align: center; font-size: 0.9rem; margin-bottom: 20px; }

/* 꽃잎 애니메이션 */
.petal { position: fixed; top: -5%; z-index: 0; animation: petal-fall 12s infinite linear; color: #FFC2D1; font-size: 20px; pointer-events: none; }
@keyframes petal-fall { 0% { transform: translateY(-5%) rotate(0deg); opacity: 0; } 10% { opacity: 0.8; } 100% { transform: translateY(100vh) rotate(360deg); opacity: 0; } }
</style>
<div class="petal" style="left:15%; animation-delay:0s;">🌸</div>
<div class="petal" style="left:80%; animation-delay:4s;">💕</div>
""", unsafe_allow_html=True)

# 3. 타이틀
st.markdown('<h1 class="main-title">지연이의<br>첫 생일 🎂</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-quote">지연이의 첫 돌잔치에 초대합니다.</p>', unsafe_allow_html=True)

# 4. [핵심] 인스타그램 피드형 앨범 컴포넌트
# 사진 리스트 (반드시 정적 파일 경로 확인)
photos = ["baby.jpg", "baby1.jpg", "baby2.jpg", "baby3.jpg"]

# 사진 전환을 위한 HTML/JS 코드
# 이 부분은 Streamlit 내부가 아니라 별도의 독립된 HTML 박스로 작동합니다.
album_html = f"""
<div id="album-container" style="display: flex; flex-direction: column; align-items: center; gap: 15px; width: 100%; font-family: sans-serif;">
    <div style="width: 100%; max-width: 400px; aspect-ratio: 4/5; overflow: hidden; border-radius: 80px 80px 20px 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); background: #eee;">
        <img id="main-img" src="./app/static/{photos[0]}" style="width: 100%; height: 100%; object-fit: cover; transition: 0.3s;">
    </div>

    <div style="display: flex; justify-content: center; gap: 8px; width: 100%; max-width: 400px;">
        {"".join([f'<div onclick="changeImg(\'./app/static/{p}\', {i})" style="flex: 1; aspect-ratio: 1/1; cursor: pointer; border-radius: 10px; overflow: hidden; border: 2px solid transparent;" class="thumb-item"><img src="./app/static/{p}" style="width: 100%; height: 100%; object-fit: cover;"></div>' for i, p in enumerate(photos)])}
    </div>
</div>

<script>
function changeImg(src, idx) {{
    document.getElementById('main-img').src = src;
    const thumbs = document.getElementsByClassName('thumb-item');
    for(let i=0; i<thumbs.length; i++) {{
        thumbs[i].style.borderColor = (i === idx) ? '#FF8FAB' : 'transparent';
    }}
}}
// 초기화
changeImg('./app/static/{photos[0]}', 0);
</script>
"""

# HTML 컴포넌트 실행 (높이는 사진 크기에 맞춰 넉넉히 600px)
components.html(album_html, height=600)

# 5. 정보 섹션 (기존 디자인 유지)
st.markdown("""
<div style="background-color: rgba(255, 255, 255, 0.7); padding: 25px 15px; border-radius: 30px; text-align: center; border: 1px solid rgba(255, 143, 171, 0.1); margin: 20px 0;">
    <p style="color: #FF8FAB; font-size: 0.7rem; font-weight: 700; letter-spacing: 2px; margin-bottom: 8px;">DATE</p>
    <p style="font-family: 'Gowun Batang'; font-size: 1.1rem; color: #5D5D5D; margin-bottom: 18px;">2026년 10월 24일 (토) 오후 1시</p>
    <p style="color: #FF8FAB; font-size: 0.7rem; font-weight: 700; letter-spacing: 2px; margin-bottom: 8px;">LOCATION</p>
    <p style="font-family: 'Gowun Batang'; font-size: 1.1rem; color: #5D5D5D; margin-bottom: 4px;"><b>행복 가든 스테이</b></p>
    <p style="font-family: 'Gowun Batang'; font-size: 0.8rem; color: #999;">서울특별시 강남구 행복로 123</p>
</div>
""", unsafe_allow_html=True)

# 6. 지도 버튼
st.markdown('<div style="display: flex; justify-content: center; gap: 10px; width: 100%;"><a href="https://map.kakao.com" target="_blank" style="flex: 1; text-decoration: none; background-color: white; color: #FF8FAB; border: 1.5px solid #FF8FAB; border-radius: 50px; padding: 12px 0; font-family: \'Gowun Batang\', serif; font-weight: 700; font-size: 0.8rem; text-align: center;">카카오맵 확인</a><a href="https://map.naver.com" target="_blank" style="flex: 1; text-decoration: none; background-color: white; color: #FF8FAB; border: 1.5px solid #FF8FAB; border-radius: 50px; padding: 12px 0; font-family: \'Gowun Batang\', serif; font-weight: 700; font-size: 0.8rem; text-align: center;">네이버 지도 확인</a></div>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align: center; color: #FF8FAB; font-family: \"Gaegu\"; font-size: 1.1rem;'>지연이의 첫 생일을 축하해 주셔서 감사합니다.</p>", unsafe_allow_html=True)
