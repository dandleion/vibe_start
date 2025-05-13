import streamlit as st
st.title('나의 첫 웹 서비스 만들기!!')
st.write('hello streamlit!!')
import streamlit as st
import random

# ------------------ 설정 ------------------ #
st.set_page_config(
    page_title="MBTI 진로 추천기 🎯",
    page_icon="🧭",
    layout="centered",
)

# ------------------ 스타일 ------------------ #
st.markdown("""
    <style>
    body {
        background-color: #f0f4ff;
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        color: #5b5bff;
        text-align: center;
        padding: 10px;
    }
    .subtitle {
        font-size: 24px;
        color: #333;
        text-align: center;
        margin-bottom: 20px;
    }
    .career-box {
        background-color: #ffffffaa;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 2px 4px 12px rgba(0,0,0,0.1);
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🔮 MBTI로 알아보는 나의 꿈! 🔮</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">당신의 MBTI를 선택하면 어울리는 직업을 추천해드릴게요! ✨</div>', unsafe_allow_html=True)

# ------------------ MBTI 목록 ------------------ #
mbti_list = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# ------------------ 추천 직업 ------------------ #
career_dict = {
    "ISTJ": ["공무원 🏛️", "회계사 📊", "경찰관 🚓"],
    "ISFJ": ["간호사 🏥", "사회복지사 🤝", "초등교사 🍎"],
    "INFJ": ["상담사 💬", "작가 ✍️", "심리학자 🧠"],
    "INTJ": ["데이터 과학자 📈", "연구원 🔬", "전략가 ♟️"],
    "ISTP": ["엔지니어 🔧", "파일럿 ✈️", "수의사 🐾"],
    "ISFP": ["디자이너 🎨", "플로리스트 💐", "요리사 👨‍🍳"],
    "INFP": ["시인 📜", "애니메이터 🖌️", "작가 ✍️"],
    "INTP": ["AI 개발자 🤖", "이론 물리학자 🌌", "프로그래머 💻"],
    "ESTP": ["스포츠 선수 ⚽", "모험가 🧗", "영업 전문가 🗣️"],
    "ESFP": ["연예인 🎤", "이벤트 플래너 🎪", "유튜버 📹"],
    "ENFP": ["광고기획자 📺", "강연가 🎙️", "게임 기획자 🎮"],
    "ENTP": ["기업가 🚀", "마케터 📢", "변호사 ⚖️"],
    "ESTJ": ["경영자 👔", "군인 🪖", "교장선생님 🎓"],
    "ESFJ": ["간호사 🏥", "상담교사 🗨️", "식품영양사 🥗"],
    "ENFJ": ["교사 👩‍🏫", "HR 매니저 🧑‍💼", "사회 운동가 ✊"],
    "ENTJ": ["CEO 💼", "정치가 🏛️", "프로젝트 매니저 📋"],
}

# ------------------ 사용자 입력 ------------------ #
selected_mbti = st.selectbox("💡 당신의 MBTI는?", mbti_list)

if st.button("🔍 나에게 어울리는 직업 찾기!"):
    st.markdown("---")
    st.markdown('<div class="subtitle">✨ 추천 직업 ✨</div>', unsafe_allow_html=True)
    careers = career_dict.get(selected_mbti, ["직업 정보를 찾을 수 없어요."])
    random.shuffle(careers)
    
    for job in careers:
        st.markdown(f'<div class="career-box">{job}</div>', unsafe_allow_html=True)

# ------------------ 푸터 ------------------ #
st.markdown("""
<hr style="margin-top:50px;">
<p style='text-align:center; font-size:14px;'>Made with 💖 for curious teens | MBTI x Career Finder</p>
""", unsafe_allow_html=True)
