import streamlit as st
import streamlit.components.v1 as components
import base64

# 1. 페이지 설정
st.set_page_config(page_title="지연이의 돌잔치에 초대합니다", page_icon="🎂", layout="centered")

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

/* 전체 여백 최소화 */
.block-container { padding-top: 1.5rem !important; padding-bottom: 0px !important; }
footer, header, #MainMenu {visibility: hidden; display: none !important;}

.main-title { font-family: 'Gaegu', cursive !important; color: #FF8FAB !important; font-size: 2.8rem !important; text-align: center; line-height: 1.2; margin-bottom: 0; }
.sub-quote { font-family: 'Gowun Batang', serif !important; color: #B2A496 !important; text-align: center; font-size: 0.9rem !important; margin-bottom: 5px; }

/* 앨범 컴포넌트 하단 여백 초밀착 */
iframe { margin-bottom: -75px !important; }

.petal { position: fixed; top: -5%; z-index: 0; animation: petal-fall 12s infinite linear; color: #FFC2D1; font-size: 20px; pointer-events: none; }
@keyframes petal-fall { 0% { transform: translateY(-5%) rotate(0deg); opacity: 0; } 10% { opacity: 0.8; } 100% { transform: translateY(100vh) rotate(360deg); opacity: 0; } }
</style>
<div class="petal" style="left:15%; animation-delay:0s;">🌸</div>
<div class="petal" style="left:80%; animation-delay:4s;">💕</div>
""", unsafe_allow_html=True)

# 3. 타이틀
st.markdown('<h1 class="main-title">지연이의<br>첫 생일 🎂</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-quote">지연이의 첫 돌잔치에 초대합니다.</p>', unsafe_allow_html=True)

# 4. 사진 데이터
photos = ["baby.jpg", "baby1.jpg", "baby2.jpg", "baby3.jpg"]
encoded_photos = [get_base64_image(p) for p in photos]

# 5. [수정] 썸네일 원본 비율 유지 앨범
# aspect-ratio를 제거하고 width를 조절하여 원본 비율대로 나오게 설정
thumb_items_html = "".join([
    f'''<div onclick="changeImg('{img}', {i})" class="thumb-item" id="thumb-{i}" style="flex: 1; cursor: pointer; border-radius: 6px; overflow: hidden; border: 2px solid transparent;">
        <img src="{img}" style="width: 100%; height: auto; display: block;">
    </div>''' 
    for i, img in enumerate(encoded_photos)
])

album_html = f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&display=swap');
    body {{ margin: 0; padding: 0; font-family: 'Gowun Batang', serif; background: transparent; overflow: hidden; }}
    #album-container {{ 
        display: flex; flex-direction: column; align-items: center; 
        gap: 8px; width: 100%; max-width: 450px; margin: 0 auto; 
    }}
    .main-img-wrapper {{
        width: 100%;
        max-height: 480px;
        border-radius: 0px; 
        overflow: hidden;
        background: transparent;
        display: flex; align-items: center; justify-content: center;
    }}
    #main-img {{ 
        width: 100%; height: auto; max-height: 480px; 
        object-fit: contain;
        transition: opacity 0.2s ease;
    }}
    /* 썸네일 리스트: 원본 비율 시 높이가 다를 수 있어 align-items: flex-end로 하단 정렬 */
    .thumb-list {{ 
        display: flex; 
        justify-content: center; 
        align-items: flex-end; 
        gap: 6px; 
        width: 100%; 
        padding: 0 15px; 
        box-sizing: border-box; 
    }}
    .active {{ border-color: #FF8FAB !important; }}
    #counter {{ color: #FF8FAB; font-size: 0.8rem; margin: 0px 0 5px 0; font-weight: bold; }}
</style>

<div id="album-container">
    <div class="main-img-wrapper"><img id="main-img" src="{encoded_photos[0]}"></div>
    <div class="thumb-list">{thumb_items_html}</div>
    <p id="counter">1 / {len(photos)}</p>
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
    }}, 100);
    const thumbs = document.getElementsByClassName('thumb-item');
    for(let i=0; i<thumbs.length; i++) {{ thumbs[i].classList.remove('active'); }}
    document.getElementById('thumb-' + idx).classList.add('active');
}}
window.onload = () => changeImg('{encoded_photos[0]}', 0);
</script>
"""

components.html(album_html, height=510)

# 6. 정보 섹션
st.markdown("""
<div style="background-color: rgba(255, 255, 255, 0.8); padding: 25px 15px; border-radius: 35px; text-align: center; border: 1px solid rgba(255, 143, 171, 0.12); box-shadow: 0 10px 20px rgba(255, 143, 171, 0.05); position: relative; z-index: 10;">
    <p style="color: #FF8FAB; font-size: 0.7rem; font-weight: 700; letter-spacing: 2px; margin-bottom: 5px; font-family: 'Gowun Batang';">DATE</p>
    <p style="font-family: 'Gowun Batang'; font-size: 1.15rem; color: #4A4A4A; margin-bottom: 18px;">2026년 10월 24일 (토) 오후 1시</p>
    <p style="color: #FF8FAB; font-size: 0.7rem; font-weight: 700; letter-spacing: 2px; margin-bottom: 5px; font-family: 'Gowun Batang';">LOCATION</p>
    <p style="font-family: 'Gowun Batang'; font-size: 1.1rem; color: #4A4A4A; margin-bottom: 4px;"><b>행복 가든 스테이</b></p>
    <p style="font-family: 'Gowun Batang'; font-size: 0.8rem; color: #888;">서울특별시 강남구 행복로 123</p>
</div>
""", unsafe_allow_html=True)

# 7. 지도 버튼
st.markdown("""
<div style="display: flex; justify-content: center; gap: 10px; width: 100%; margin-top: 15px;">
    <a href="https://map.kakao.com" target="_blank" style="flex: 1; text-decoration: none; background: white; color: #FF8FAB; border: 1.5px solid #FF8FAB; border-radius: 50px; padding: 12px 0; font-family: 'Gowun Batang'; font-weight: 700; font-size: 0.85rem; text-align: center;">카카오맵 확인</a>
    <a href="https://map.naver.com" target="_blank" style="flex: 1; text-decoration: none; background: white; color: #FF8FAB; border: 1.5px solid #FF8FAB; border-radius: 50px; padding: 12px 0; font-family: 'Gowun Batang'; font-weight: 700; font-size: 0.85rem; text-align: center;">네이버 지도 확인</a>
</div>
<p style='text-align: center; color: #FF8FAB; font-family: "Gaegu"; font-size: 1.1rem; margin-top: 30px;'>지연이의 첫 생일을 축하해 주셔서 감사합니다.</p>
""", unsafe_allow_html=True)
