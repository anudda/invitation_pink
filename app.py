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

# 2. 메인 스타일
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Gaegu:wght@300;400&display=swap');
.stApp { background-color: #FFF5F5 !important; }

/* 위젯 간 간격 정상화 (0.5rem) */
div[data-testid="stVerticalBlock"] { gap: 0.5rem !important; }
.block-container { padding-top: 2rem !important; padding-bottom: 2rem !important; }

footer, header, #MainMenu {visibility: hidden; display: none !important;}

.main-title { 
    font-family: 'Gaegu', cursive !important; 
    color: #FF8FAB !important; 
    font-size: 2.8rem !important; 
    text-align: center; 
    line-height: 1.2; 
    margin-bottom: 5px; 
}
.sub-quote { 
    font-family: 'Gowun Batang', serif !important; 
    color: #B2A496 !important; 
    text-align: center; 
    font-size: 0.9rem !important; 
    margin-bottom: 15px; 
}

/* 겹침 방지를 위해 마이너스 마진 모두 제거 */
iframe { 
    width: 100%; 
    border: none; 
    margin: 0px !important; 
}

.petal { position: fixed; top: -5%; z-index: 0; animation: petal-fall 12s infinite linear; color: #FFC2D1; font-size: 20px; pointer-events: none; }
@keyframes petal-fall { 0% { transform: translateY(-5%) rotate(0deg); opacity: 0; } 10% { opacity: 0.8; } 100% { transform: translateY(100vh) rotate(360deg); opacity: 0; } }
</style>
<div class="petal" style="left:15%; animation-delay:0s;">🌸</div>
<div class="petal" style="left:80%; animation-delay:4s;">💕</div>
""", unsafe_allow_html=True)

# 3. 타이틀 섹션
st.markdown('<h1 class="main-title">지연이의<br>첫 생일 🎂</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-quote">지연이의 첫 돌잔치에 초대합니다.</p>', unsafe_allow_html=True)

# 4. 사진 데이터 준비
photos = ["baby.jpg", "baby1.jpg", "baby2.jpg", "baby3.jpg"]
encoded_photos = [get_base64_image(p) for p in photos]

# 5. 앨범 컴포넌트 (높이 420px로 정밀 조정)
thumb_html = "".join([
    f'<div onclick="changeImg(\'{img}\', {i})" class="thumb-item" id="thumb-{i}"><img src="{img}"></div>'
    for i, img in enumerate(encoded_photos)
])

album_content = f"""
<div id="album-container">
    <div class="main-wrapper"><img id="main-img" src="{encoded_photos[0]}"></div>
    <div class="thumb-list">{thumb_html}</div>
    <p id="counter">1 / {len(photos)}</p>
</div>

<style>
    body {{ margin: 0; padding: 0; background: transparent; overflow: hidden; }}
    #album-container {{ display: flex; flex-direction: column; align-items: center; gap: 8px; width: 100%; }}
    .main-wrapper {{ 
        width: 100%; 
        height: 320px; /* 대표 사진 높이 고정으로 겹침 방지 */
        display: flex; justify-content: center; align-items: center; 
        background: transparent; 
    }}
    #main-img {{ max-width: 100%; max-height: 100%; object-fit: contain; }}
    .thumb-list {{ 
        display: flex; flex-wrap: nowrap; justify-content: center; align-items: flex-end; 
        gap: 6px; width: 100%; padding: 0 10px; box-sizing: border-box; 
    }}
    .thumb-item {{ flex: 1; cursor: pointer; border: 2px solid transparent; border-radius: 6px; overflow: hidden; }}
    .thumb-item img {{ width: 100%; height: auto; display: block; }}
    .active {{ border-color: #FF8FAB !important; }}
    #counter {{ color: #FF8FAB; font-size: 13px; font-weight: bold; margin: 2px 0; font-family: sans-serif; }}
</style>

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

# [수정] 높이를 420으로 고
