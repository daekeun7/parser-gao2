import streamlit as st
from PIL import Image # 위에서 선언 후 사용해야한다.

st.title("GAO reports Word Cloud since 2022")

tabs = st.tabs(["GAO_EN", "GAO_한글"])

with tabs[0]:
  # 경로에 있는 이미지 파일을 통해 변수 저장
  img1 = Image.open('images/en/Agriculture and Food.png')
  img2 = Image.open('images/en/Auditing and Financial Management.png')
  img3 = Image.open('images/en/Agriculture and Food.png')
  img4 = Image.open('images/en/Agriculture and Food.png')
  img5 = Image.open('images/en/Agriculture and Food.png')
  img6 = Image.open('images/en/Agriculture and Food.png')
  img7 = Image.open('images/en/Agriculture and Food.png')
  img8 = Image.open('images/en/Agriculture and Food.png')
  img9 = Image.open('images/en/Agriculture and Food.png')
  img10 = Image.open('images/en/Agriculture and Food.png')
  img11 = Image.open('images/en/Agriculture and Food.png')
  img12 = Image.open('images/en/Agriculture and Food.png')
  img13 = Image.open('images/en/Agriculture and Food.png')
  img14 = Image.open('images/en/Agriculture and Food.png')
  img15 = Image.open('images/en/Agriculture and Food.png')
  img16 = Image.open('images/en/Agriculture and Food.png')
  img17 = Image.open('images/en/Agriculture and Food.png')
  img18 = Image.open('images/en/Agriculture and Food.png')
  img19 = Image.open('images/en/Agriculture and Food.png')
  img20 = Image.open('images/en/Agriculture and Food.png')
  img21 = Image.open('images/en/Agriculture and Food.png')
  img22 = Image.open('images/en/Agriculture and Food.png')
  img23 = Image.open('images/en/Agriculture and Food.png')
  img24 = Image.open('images/en/Agriculture and Food.png')
  img25 = Image.open('images/en/Agriculture and Food.png')
  img26 = Image.open('images/en/Agriculture and Food.png')
  img27 = Image.open('images/en/Agriculture and Food.png')
  img28 = Image.open('images/en/Agriculture and Food.png')
  img29 = Image.open('images/en/Agriculture and Food.png')
  img30 = Image.open('images/en/Agriculture and Food.png')
  img31 = Image.open('images/en/Agriculture and Food.png')
  img32 = Image.open('images/en/Agriculture and Food.png')
  
    
  # streamlit를 통해 이미지를 보여준다.
  st.image(img1)
  st.divider()
  st.image(img2)
  st.divider()

with tabs[1]:
  # main()
  img = Image.open('images/en/Budget and Spending.png')
  
  # 경로에 있는 이미지 파일을 통해 변수 저장
  
  st.image(img)
  # streamlit를 통해 이미지를 보여준다.
