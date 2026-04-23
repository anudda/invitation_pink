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

/* 기본 여백 최적화 */
.block-container { padding-top: 1rem !important; padding-bottom: 0px !important; }
footer, header, #MainMenu {visibility: hidden; display: none !important;}

.main-title { font-family: 'Gaegu', cursive !important; color: #FF8FAB !important; font-size: 2.8rem !important; text-align: center; line-height: 1.2; margin-bottom: 0; }
.sub-quote { font-family: 'Gowun Batang', serif !important; color: #B2A496 !important; text-align: center; font-size: 0.9rem !important; margin-bottom: 10px; }

/* 앨범 컴포넌트 하단 여백 밀착 */
iframe { margin-bottom: -40px !important; }

.petal { position: fixed; top: -5%; z-index: 0; animation: petal-fall 12s infinite linear; color: #FFC2D1; font-size: 20px; pointer-events: none; }
@keyframes petal-fall { 0% { transform: translateY(-5%) rotate(0deg); opacity: 0; } 10% { opacity: 0.8; } 100% { transform: translateY(100vh) rotate(360deg); opacity: 0; } }
</style>
<div class="petal" style="left:15%; animation-delay:0s;">🌸</div>
<div class="petal" style="left:80%; animation-delay:4s;">💕</div>
""", unsafe_allow_html=True)

# 3. 타이틀
st.markdown('<h1 class="main-title">지연이의<br>첫 생일 🎂</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-quote">지연이의 첫 돌잔치에 초대합니다.</p>', unsafe_allow_html=True)

# 4. 앨범 데이터 및 변환
photos = ["baby.jpg", "baby1.jpg", "baby2.jpg", "baby3.jpg"]
encoded_photos = [get_base64_image(p) for p in photos]

# 5. 반응형 앨범 HTML
thumb_items_html = "".join([
    f'<div onclick="changeImg(\'{img}\', {i})" class="thumb-item" id="thumb-{i}" style="flex: 1; aspect-ratio: 1/1; cursor: pointer; border-radius: 8px; overflow: hidden; border: 2px solid transparent; background: #fff;">'
    f'<img src="{img}" style="width: 100%; height: 100%; object-fit: cover;"></div>' 
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
        min-height: 300px;
        max-height: 500px;
        border-radius: 60px 60px 20px 20px;
        box-shadow: 0 8px 15px rgba(255, 143, 171, 0.1);
        overflow: hidden;
        background: #fff;
        display: flex; align-items: center; justify-content: center;
    }}
    #main-img {{ 
        width: 100%; height: auto; max-height: 100%; 
        object-fit: contain; /* 사진이 절대 잘리지 않음 */
        transition: opacity 0.2s ease; 
    }}
    .thumb-list {{ display: flex; justify-content: center; gap: 6px; width: 100%; padding: 0 10px; box-sizing: border-box; }}
    .active {{ border-color: #FF8FAB !important; transform: scale(1.02); }}
    #counter {{ color: #FF8FAB; font-size: 0.85rem; margin: 2px 0; font-weight: bold; }}
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
    for(let i=0; i<thumbs.length; i++) {{
        thumbs[i].classList.remove('active');
    }}
    document.getElementById('thumb-' + idx).classList.add('active');
}}
window.onload = () => changeImg('{encoded_photos[0]}', 0);
</script>
"""

# 컴포넌트 높이를 520px로 조절 (PC/모바일 공용 최적화)
components.html(album_html, height=520)

# 6. 정보 섹션
st.markdown("""
<div style="background-color: rgba(255, 255, 255, 0.8); padding: 20px 15px; border-radius: 30px; text-align: center; border: 1px solid rgba(255, 143, 171, 0.1); box-shadow: 0 5px 15px rgba(255, 143, 171, 0.05);">
    <p style="color: #FF8FAB; font-size: 0.7rem; font-weight: 700; letter-spacing: 2px; margin-bottom: 5px; font-family: 'Gowun Batang';">DATE</p>
    <p style="font-family: 'Gowun Batang'; font-size: 1.1rem; color: #5D5D5D; margin-bottom: 15px;">2026년 10월 24일 (토) 오후 1시</p>
    <p style="color: #FF8FAB; font-size: 0.7rem; font-weight: 700; letter-spacing: 2px; margin-bottom: 5px; font-family: 'Gowun Batang';">LOCATION</p>
    <p style="font-family: 'Gowun Batang'; font-size: 1.1rem; color: #5D5D5D; margin-bottom: 4px;"><b>행복 가든 스테이</b></p>
    <p style="font-family: 'Gowun Batang'; font-size: 0.8rem; color: #999;">서울특별시 강남구 행복로 123</p>
</div>
""", unsafe_allow_html=True)

# 7. 지도 버튼 및 마무리
st.markdown("""
<div style="display: flex; justify-content: center; gap: 10px; width: 100%; margin-top: 15px;">
    <a href="https://map.kakao.com" target="_blank" style="flex: 1; text-decoration: none; background: white; color: #FF8FAB; border: 1.5px solid #FF8FAB; border-radius: 50px; padding: 10px 0; font-family: 'Gowun Batang'; font-weight: 700; font-size: 0.8rem; text-align: center;">카카오맵</a>
    <a href="https://map.naver.com" target="_blank" style="flex: 1; text-decoration: none; background: white; color: #FF8FAB; border: 1.5px solid #FF8FAB; border-radius: 50px; padding: 10px 0; font-family: 'Gowun Batang'; font-weight: 700; font-size: 0.8rem; text-align: center;">네이버지도</a>
</div>
<p style='text-align: center; color: #FF8FAB; font-family: "Gaegu"; font-size: 1.1rem; margin-top: 25px;'>지연이의 첫 생일을 축하해 주셔서 감사합니다.</p>
""", unsafe_allow_html=True)
