import streamlit as st
import streamlit.components.v1 as components
import base64

# 1. 페이지 설정
st.set_page_config(page_title="🎂지연이의 돌잔치에 초대합니다", page_icon="🎂", layout="centered")

# --- [여백 조절용 수치] 필요시 조절하세요! ---
TOP_GAP = 20      # 타이틀과 사진 사이 간격
BOTTOM_GAP = 20   # 사진과 아래 카드 사이 간격
ALBUM_HEIGHT = 450 # 앨범 영역 전체 높이
# ----------------------------------------------

# [함수] 이미지 텍스트 변환
def get_b64(path):
    try: return "data:image/jpeg;base64," + base64.b64encode(open(path, "rb").read()).decode()
    except: return ""

# 2. 통합 스타일 및 꽃잎 애니메이션
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Gaegu:wght@300;400&display=swap');

.stApp {{ background-color: #FFF5F5 !important; font-family: 'Gowun Batang', serif; }}
.block-container {{ padding: 2rem 1rem 3rem !important; }}
div[data-testid="stVerticalBlock"] {{ gap: 0rem !important; }}
footer, header, #MainMenu {{ display: none !important; }}

iframe {{ 
    border: none; 
    margin-top: 0px !important; 
    margin-bottom: {BOTTOM_GAP}px !important; 
    display: block; 
}}

.petal {{ 
    position: fixed; 
    top: -10%; 
    z-index: 0; 
    animation: fall linear infinite; 
    color: #FFC2D1; 
    pointer-events: none; 
}}

@keyframes fall {{
    0% {{ transform: translateY(-10%) rotate(0deg); opacity: 0; }}
    10% {{ opacity: 0.8; }}
    100% {{ transform: translateY(110vh) rotate(720deg); opacity: 0; }}
}}
</style>

<div class="petal" style="left:10%; animation-duration:10s; font-size:20px;">🌸</div>
<div class="petal" style="left:25%; animation-duration:12s; animation-delay:2s; font-size:16px;">💕</div>
<div class="petal" style="left:40%; animation-duration:9s; animation-delay:1s; font-size:22px;">🌸</div>
<div class="petal" style="left:60%; animation-duration:13s; animation-delay:4s; font-size:15px;">💕</div>
<div class="petal" style="left:75%; animation-duration:11s; animation-delay:3s; font-size:18px;">🌸</div>
<div class="petal" style="left:90%; animation-duration:8s; animation-delay:0s; font-size:20px;">💕</div>
""", unsafe_allow_html=True)

# 3. 타이틀 섹션 (서브 문구 폰트를 'Gaegu'로 변경하여 귀여움 업그레이드!)
st.markdown(f"""
<div style="text-align: center; position: relative; z-index: 10;">
    <h1 style="font-family: 'Gaegu', cursive; color: #FF8FAB; font-size: 2.8rem; margin: 0; line-height: 1.2;">Jiyeon's<br>1st Birthday</h1>
    <p style="font-family: 'Gaegu', cursive; color: #A89080; font-size: 1.25rem; margin-top: 15px; margin-bottom: {TOP_GAP}px; font-weight: bold; line-height: 1.6;">
        향긋한 봄 내음이 가득한 4월<br>
        지연이의 첫 돌잔치에 여러분을 초대합니다
    </p>
</div>
""", unsafe_allow_html=True)

# 4. 사진 데이터 준비
photos = ["baby.jpg", "baby1.jpg", "baby2.jpg", "baby3.jpg"]
b64_photos = [get_b64(p) for p in photos]

# 5. 앨범 컴포넌트 (배경색 통일 버전)
thumbs = "".join([f'<img class="t" src="{p}" onclick="s(this, \'{p}\', {i})">' for i, p in enumerate(b64_photos)])

album_html = """
<style>
    /* 전체 배경을 사이트 배경색(#FFF5F5)과 통일 */
    body { margin: 0; background: #FFF5F5; font-family: sans-serif; text-align: center; overflow: hidden; }
    
    .main { 
        width: 100%; 
        max-width: 450px; 
        height: 400px;
        object-fit: contain;
        /* 사진 뒤에 깔리는 배경색도 동일하게 설정 */
        background: #FFF5F5;
        margin: 0 auto; 
        display: block; 
        border-radius: 12px;
    }
    .row { display: flex; align-items: center; justify-content: center; gap: 6px; max-width: 450px; margin: 15px auto 5px; padding: 0 10px; box-sizing: border-box; }
    .t { width: 60px; height: 60px; border-radius: 6px; cursor: pointer; border: 2px solid transparent; transition: 0.2s; object-fit: cover; display: block; }
    .active { border-color: #FF8FAB !important; }
    .cnt { color: #FF8FAB; font-size: 13px; font-weight: bold; margin: 5px 0 0; }
</style>
<img id="m" class="main" src='""" + b64_photos[0] + """'>
<div class="row">""" + thumbs + """</div>
<p id="c" class="cnt">1 / """ + str(len(photos)) + """</p>
<script>
    function s(el, src, i) {
        document.getElementById('m').src = src;
        document.getElementById('c').innerText = (i+1) + " / """ + str(len(photos)) + """";
        document.querySelectorAll('.t').forEach(t => t.classList.remove('active'));
        el.classList.add('active');
    }
</script>
"""
components.html(album_html, height=520)

# 6. 정보 카드 및 버튼
st.markdown("""
<div style="position: relative; z-index: 10;">
    <div style="background: rgba(255,255,255,0.85); padding: 25px; border-radius: 30px; text-align: center; border: 1px solid rgba(255,143,171,0.2); box-shadow: 0 8px 15px rgba(255,143,171,0.05); margin-bottom: 15px;">
        <p style="color: #FF8FAB; font-size: 0.7rem; font-weight: bold; letter-spacing: 2px; margin: 0 0 5px;">DATE</p>
        <p style="font-size: 1.15rem; color: #4A4A4A; margin: 0 0 15px;">2026년 10월 24일 (토) 오후 1시</p>
        <p style="color: #FF8FAB; font-size: 0.7rem; font-weight: bold; letter-spacing: 2px; margin: 0 0 5px;">LOCATION</p>
        <p style="font-size: 1.1rem; color: #4A4A4A; font-weight: bold; margin: 0 0 2px;">행복 가든 스테이</p>
        <p style="font-size: 0.8rem; color: #888; margin: 0;">서울특별시 강남구 행복로 123</p>
    </div>
    <div style="display: flex; gap: 10px;">
        <a href="https://map.kakao.com" target="_blank" style="flex: 1; background: white; color: #FF8FAB; border: 1.5px solid #FF8FAB; border-radius: 50px; padding: 12px 0; text-align: center; text-decoration: none; font-weight: bold; font-size: 0.85rem;">카카오맵 확인</a>
        <a href="https://map.naver.com" target="_blank" style="flex: 1; background: white; color: #FF8FAB; border: 1.5px solid #FF8FAB; border-radius: 50px; padding: 12px 0; text-align: center; text-decoration: none; font-weight: bold; font-size: 0.85rem;">네이버 지도 확인</a>
    </div>
    <p style="text-align: center; color: #FF8FAB; font-family: 'Gaegu', cursive; font-size: 1.15rem; margin-top: 30px;">지연이의 첫 생일을 축하해 주셔서 감사합니다.</p>
</div>
""", unsafe_allow_html=True)
