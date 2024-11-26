# 사용 방법
from PIL import Image # 위에서 선언 후 사용해야한다.


# main()
img = Image.open('data/image.jpg')

# 경로에 있는 이미지 파일을 통해 변수 저장

st.image(img)
# streamlit를 통해 이미지를 보여준다.
