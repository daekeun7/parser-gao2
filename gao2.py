import streamlit as st
from PIL import Image # 위에서 선언 후 사용해야한다.

st.title("Word Cloud of Keywords from GAO Reports since 2022")

tabs = st.tabs(["GAO_EN", "GAO_한글"])

with tabs[0]:
  # main()
  img = Image.open('images/en/Agriculture and Food.png')
  
  # 경로에 있는 이미지 파일을 통해 변수 저장
  
  st.image(img)
  # streamlit를 통해 이미지를 보여준다.

with tabs[1]:
  # main()
  img = Image.open('images/en/Budget and Spending.png')
  
  # 경로에 있는 이미지 파일을 통해 변수 저장
  
  st.image(img)
  # streamlit를 통해 이미지를 보여준다.
