import streamlit as st
import random

# 명언 데이터
quotes = {
    "노력": [
        "노력은 배신하지 않는다.",
        "오늘의 당신은 어제의 노력의 결과다.",
        "끝까지 포기하지 않는 것이 진짜 용기다."
    ],
    "꿈": [
        "큰 꿈을 꾸어라. 작은 꿈에는 영혼이 담기지 않는다.",
        "꿈꾸는 자만이 미래를 본다.",
        "당신의 꿈이 당신의 방향이다."
    ],
    "용기": [
        "가장 어두운 밤이 지나야 새벽이 온다.",
        "두려움 속에서도 나아가는 것이 진짜 용기다.",
        "넘어져도 다시 일어나면 된다."
    ]
}

# 웹 제목
st.title("🌸 랜덤 명언 생성기 🌸")
st.write("주제를 선택하고 오늘의 명언을 받아보세요!")

# 선택 박스
theme = st.selectbox("주제를 선택하세요", list(quotes.keys()))

# 버튼
if st.button("명언 뽑기 🎲"):
    st.success(random.choice(quotes[theme]))
