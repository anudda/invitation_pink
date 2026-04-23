import streamlit as st
import streamlit.components.v1 as components
import base64

# 1. 페이지 설정
st.set_page_config(page_title="지연이의 돌잔치에 초대합니다", page_icon="🎂", layout="centered")

# [함수] 이미지 변환
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return "data:image/jpeg;base64," + base64.b64encode(img_file.read()).decode()
    except: return ""

# 2. 메인 스타일 설정
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Gaegu:wght@300;400&display=swap');
.stApp { background-color: #FFF5F5 !important; }
.block-container { padding-top: 1rem !important; }
footer, header, #MainMenu {visibility: hidden; display: none !important;}

.main-title { font-family: 'Gaegu', cursive !important; color: #FF8FAB !important; font-size: 2.8rem !important; text-align: center; line-height: 1.2; margin-bottom: 0; }
.sub-quote { font-family: 'Gowun Batang', serif !important; color: #B2A496 !important; text-align: center; font-size: 0.9rem !important; margin-bottom: 20px; }

.petal { position: fixed; top: -5%; z-index: 0; animation: petal-fall 12s infinite linear; color: #FFC2D1; font-size: 20px; pointer-events: none; }
@keyframes petal-fall { 0% { transform: translateY(-5%) rotate(0deg); opacity: 0; } 10% { opacity: 0.8; } 100% { transform: translateY(100vh) rotate(360deg); opacity: 0; } }
</style>
<div class="petal" style="left:15%; animation-delay:0s;">🌸</div>
<div class="petal" style="left:80%; animation-delay:4s;">💕</div>
""", unsafe_allow_html=True)

# 3. 타이틀
st.markdown('<h1 class="main-title">지연이의<br>첫 생일 🎂</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-quote">지연이의 첫 돌잔치에 초대합니다.</p>', unsafe_allow_html=True)

# 4. 앨범 데이터 준비
photos = ["baby.jpg", "baby1.jpg", "baby2.jpg", "baby3.jpg"]
encoded_photos = [get_base64_image(p) for p in photos]

# 5. [수정] 앨범 컴포넌트 (폰트 및 스타일 강제 동기화)
thumb_items_html = "".join([
    f'<div onclick="changeImg(\'{img}\', {i})" class="thumb-item" id="thumb-{i}" style="flex: 1; aspect-ratio: 1/1; cursor: pointer; border-radius: 10px; overflow: hidden; border: 2px solid transparent; background: #eee;">'
    f'<img src="{img}" style="width: 100%; height: 100%; object-fit: cover;"></div>' 
    for i, img in enumerate(encoded_photos)
])

album_html = f"""
<style>
    /* 앨범 내부에도 폰트 적용 */
    @import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&display=swap');
    body {{ margin: 0; padding: 0; font-family: 'Gowun Batang', serif; }}
    .thumb-item {{ transition: 0.2s; }}
    .active {{ border-color: #FF8FAB !important; box-shadow: 0 0 10px rgba(255, 143, 171, 0.3); }}
</style>

<div id="album-container" style="display: flex; flex-direction: column; align-items: center; gap: 15px; width: 100%;">
    <div style="width: 100%; max-width: 400px; aspect-ratio: 4/5; overflow: hidden; border-radius: 80px 80px 20px 20px; box-shadow: 0 10px 25px rgba(255, 143, 171, 0.15); background: #fff;">
        <img id="main-img" src="{encoded_photos[0]}" style="width: 100%; height: 100%; object-fit: cover; transition: opacity 0.3s;">
    </div>
    <div style="display: flex; justify-content: center; gap: 8px; width: 100%; max-width: 400px; padding: 0 5px;">
        {thumb_items_html}
    </div>
    <p id="counter" style="color: #FF8FAB; font-size: 0.8rem; margin: 0; font-weight: bold;">1 / {len(photos)}</p>
</div>

<script>
function changeImg(src, idx) {{
    const mainImg = document.getElementById('main-img');
    const counter = document.getElementById('counter');
    mainImg.style.opacity = 0.5;
    setTimeout(() => {{
        mainImg.src = src;
        mainImg.style.opacity = 1;
        counter.innerText = (idx + 1) + " / {len(photos)}";
    }}, 150);
    
    const thumbs = document.getElementsByClassName('thumb-item');
    for(let i=0; i<thumbs.length; i++) {{
        thumbs[i].classList.remove('active');
    }}
    document.getElementById('thumb-' + idx).classList.add('active');
}}
// 초기화
window.onload = () => changeImg('{encoded_photos[0]}', 0);
</script>
"""

components.html(album_html, height=550)

# 6. 정보 섹션 & 지도 버튼 (디자인 동일)
st.markdown("""
<div style="background-color: rgba(255, 255, 255, 0.7); padding: 25px 15px; border-radius: 30px; text-align: center; border: 1px solid rgba(255, 143, 171, 0.1); margin: 10px 0;">
    <p style="color: #FF8FAB; font-size: 0.7rem; font-weight: 700; letter-spacing: 2px; margin-bottom: 8px; font-family: 'Gowun Batang';">DATE</p>
    <p style="font-family: 'Gowun Batang'; font-size: 1.1rem; color: #5D5D5D; margin-bottom: 18px;">2026년 10월 24일 (토) 오후 1시</p>
    <p style="color: #FF8FAB; font-size: 0.7rem; font-weight: 700; letter-spacing: 2px; margin-bottom: 8px; font-family: 'Gowun Batang';">LOCATION</p>
    <p style="font-family: 'Gowun Batang'; font-size: 1.1rem; color: #5D5D5D; margin-bottom: 4px;"><b>행복 가든 스테이</b></p>
    <p style="font-family: 'Gowun Batang'; font-size: 0.8rem; color: #999;">서울특별시 강남구 행복로 123</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div style="display: flex; justify-content: center; gap: 10px; width: 100%;"><a href="https://map.kakao.com" target="_blank" style="flex: 1; text-decoration: none; background-color: white; color: #FF8FAB; border: 1.5px solid #FF8FAB; border-radius: 50px; padding: 12px 0; font-family: \'Gowun Batang\', serif; font-weight: 700; font-size: 0.8rem; text-align: center;">카카오맵 확인</a><a href="https://map.naver.com" target="_blank" style="flex: 1; text-decoration: none; background-color: white; color: #FF8FAB; border: 1.5px solid #FF8FAB; border-radius: 50px; padding: 12px 0; font-family: \'Gowun Batang\', serif; font-weight: 700; font-size: 0.8rem; text-align: center;">네이버 지도 확인</a></div>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align: center; color: #FF8FAB; font-family: \"Gaegu\"; font-size: 1.1rem;'>지연이의 첫 생일을 축하해 주셔서 감사합니다.</p>", unsafe_allow_html=True)
