import streamlit as st
import streamlit.components.v1 as components
import base64

# 1. 페이지 설정
st.set_page_config(page_title="지연이의 돌잔치에 초대합니다", page_icon="🎂", layout="centered")

# [함수] 이미지 텍스트 변환 (경량화)
def get_b64(path):
    try: return "data:image/jpeg;base64," + base64.b64encode(open(path, "rb").read()).decode()
    except: return ""

# 2. 통합 스타일 및 배경 애니메이션
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Gaegu:wght@300;400&display=swap');

.stApp { background-color: #FFF5F5 !important; font-family: 'Gowun Batang', serif; }
.block-container { padding: 2rem 1rem 3rem !important; }
div[data-testid="stVerticalBlock"] { gap: 0.8rem !important; } /* 위젯 기본 간격 최적화 */
footer, header, #MainMenu { display: none !important; }

/* 앨범 액자(iframe) 기본 여백 초기화 - 겹침 방지 */
iframe { border: none; margin: 0 !important; display: block; }

/* 흩날리는 꽃잎 애니메이션 */
.petal { position: fixed; top: -10%; animation: fall linear infinite; pointer-events: none; z-index: 0; }
@keyframes fall { 100% { transform: translateY(110vh) rotate(720deg); } }
</style>

<div class="petal" style="left:10%; animation-duration:10s; font-size:20px;">🌸</div>
<div class="petal" style="left:25%; animation-duration:12s; animation-delay:2s; font-size:16px;">💕</div>
<div class="petal" style="left:40%; animation-duration:9s; animation-delay:1s; font-size:22px;">🌸</div>
<div class="petal" style="left:60%; animation-duration:13s; animation-delay:4s; font-size:15px;">💕</div>
<div class="petal" style="left:75%; animation-duration:11s; animation-delay:3s; font-size:18px;">🌸</div>
<div class="petal" style="left:90%; animation-duration:8s; animation-delay:0s; font-size:20px;">💕</div>
""", unsafe_allow_html=True)

# 3. 타이틀 섹션 (파이썬 코드로 깔끔하게 분리)
st.markdown("""
<div style="text-align: center; position: relative; z-index: 10;">
    <h1 style="font-family: 'Gaegu', cursive; color: #FF8FAB; font-size: 2.8rem; margin: 0; line-height: 1.2;">지연이의<br>첫 생일 🎂</h1>
    <p style="color: #B2A496; font-size: 0.9rem; margin-top: 5px;">지연이의 첫 돌잔치에 초대합니다.</p>
</div>
""", unsafe_allow_html=True)

# 4. 사진 데이터 및 앨범 렌더링
photos = ["baby.jpg", "baby1.jpg", "baby2.jpg", "baby3.jpg"]
b64_photos = [get_b64(p) for p in photos]

# 썸네일 HTML 반복문 한 줄로 압축
thumbs = "".join([f'<img class="t" src="{p}" onclick="s(this, \'{p}\', {i})">' for i, p in enumerate(b64_photos)])

# 초경량 앨범 HTML
album_html = f"""
<style>
    body {{ margin: 0; background: transparent; font-family: sans-serif; text-align: center; }}
    /* 대표 사진: 직각 유지, 350px 고정, 잘림 없음 */
    .main {{ width: 100%; max-width: 450px; height: 350px; object-fit: contain; margin: 0 auto; display: block; }}
    /* 썸네일 줄: 원본 비율 유지, 아래로 정렬 */
    .row {{ display: flex; align-items: flex-end; justify-content: center; gap: 8px; max-width: 450px; margin: 10px auto 5px; padding: 0 10px; box-sizing: border-box; }}
    .t {{ flex: 1; width: 100%; height: auto; border-radius: 6px; cursor: pointer; border: 2px solid transparent; transition: 0.2s; }}
    .active {{ border-color: #FF8FAB !important; }}
    .cnt {{ color: #FF8FAB; font-size: 13px; font-weight: bold; margin: 0; }}
</style>

<img id="m" class="main" src="{b64_photos[0]}">
<div class="row">{thumbs}</div>
<p id="c" class="cnt">1 / {len(photos)}</p>

<script>
    function s(el, src, i) {{
        document.getElementById('m').src = src;
        document.getElementById('c').innerText = (i+1) + " / {len(photos)}";
        document.querySelectorAll('.t').forEach(t => t.classList.remove('active'));
        el.classList.add('active');
    }}
    document.querySelector('.t').classList.add('active');
</script>
"""

# 전체 높이를 480px로 여유롭게 고정하여 겹침 방지
components.html(album_html, height=480)

# 5. 정보 카드 및 버튼 
# 덩어리로 묶어 Streamlit 레이아웃의 변수 차단
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
