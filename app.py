# 3. 타이틀 섹션 (구름 배경 + 미니멀 문구)
st.markdown(f"""
<div style="text-align: center; position: relative; z-index: 10; padding: 10px 0;">
    <div style="background: rgba(255, 255, 255, 0.6); 
                display: inline-block; 
                padding: 15px 30px; 
                border-radius: 50px; 
                box-shadow: 0 4px 15px rgba(255, 143, 171, 0.1);">
        
        <h1 style="font-family: 'Gaegu', cursive; color: #FF8FAB; font-size: 2.5rem; margin: 0; line-height: 1.2;">
            지연이의 첫 돌 🎂
        </h1>
        
        <p style="font-family: 'Gaegu', cursive; color: #A89080; font-size: 1.1rem; margin-top: 5px; margin-bottom: 0; font-weight: bold;">
            꽃보다 예쁜 지연이의 첫 생일잔치 🌸
        </p>
    </div>
    
    <div style="margin-bottom: {TOP_GAP}px;"></div>
</div>
""", unsafe_allow_html=True)
