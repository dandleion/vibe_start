import streamlit as st

import streamlit as st
import random

import streamlit as st
import random
import streamlit as st
import random

# ✅ 페이지 설정 (항상 제일 위)
st.set_page_config(
    page_title="MBTI 진로 추천기 🎯",
    page_icon="🧭",
    layout="centered",
)

# ✅ 스타일 (CSS 및 배경 GIF)
st.markdown("""
    <style>
    /* 배경 애니메이션 */
    [data-testid="stAppViewContainer"] {
        background-image: url("https://i.gifer.com/7VE.gif");
        background-size: cover;
        background-position: center;
    }

    /* 전체 카드 스타일 */
    .career-box {
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        font-size: 22px;
        font-weight: bold;
        color: #333;
        transition: all 0.3s ease;
    }

    .career-box:hover {
        background-color: #fff;
        transform: scale(1.02);
    }

    .title {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        color: #ffd700;
        text-shadow: 2px 2px 10px #000;
        margin-top: 30px;
    }

    .subtitle {
        font-size: 22px;
        text-align: center;
        color: white;
        margin-bottom: 30px;
        text-shadow: 1px 1px 5px #000;
    }

    .selectbox label {
        color: white !important;
    }

    .footer {
        font-size: 14px;
        text-align: center;
        color: white;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ 타이틀
st.markdown('<div class="title">✨ MBTI로 알아보는 나의 미래 직업 ✨</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">MBTI를 선택하면 당신에게 딱 맞는 직업을 추천해줄게요! 🚀</div>', unsafe_allow_html=True)

# ✅ MBTI 리스트
mbti_list = [
    "ISTJ 🧠", "ISFJ 💖", "INFJ 🔮", "INTJ 🧬",
    "ISTP 🔧", "ISFP 🎨", "INFP 📖", "INTP 🧠",
    "ESTP ⚡", "ESFP 🎤", "ENFP 🌈", "ENTP 🚀",
    "ESTJ 👔", "ESFJ 🏡", "ENFJ 🎓", "ENTJ 👑"
]

# ✅ 직업 추천 데이터
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
    "ESFJ": ["간호사 🏥", "상담교사 🗨️", "영양사 🥗"],
    "ENFJ": ["교사 👩‍🏫", "HR 매니저 💼", "사회 운동가 ✊"],
    "ENTJ": ["CEO 💼", "정치가 🏛️", "프로젝트 매니저 📋"],
}

# ✅ 사용자 선택
selected = st.selectbox("💡 당신의 MBTI는?", mbti_list)

# MBTI 코드만 추출 (ex. "ENFP 🌈" → "ENFP")
selected_mbti = selected.split()[0]

# ✅ 버튼 클릭 시 결과 출력
if st.button("🔍 나에게 어울리는 직업 보기"):
    st.markdown("---")
    st.markdown('<div class="subtitle">🌟 당신에게 어울리는 직업 🌟</div>', unsafe_allow_html=True)
    careers = career_dict.get(selected_mbti, ["직업 정보를 찾을 수 없어요 😢"])
    random.shuffle(careers)

    for job in careers:
        st.markdown(f'<div class="career-box">{job}</div>', unsafe_allow_html=True)

# ✅ 푸터
st.markdown('<div class="footer">© 2025 MBTI Career Explorer | Made for Teens 🚀</div>', unsafe_allow_html=True)

# ✅ 페이지 설정은 항상 가장 먼저 해야 함!
st.set_page_config(
    page_title="MBTI 진로 추천기 🎯",
    page_icon="🧭",
    layout="centered",
)

# ------------------ 사용자 정의 스타일 ------------------ #
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #e0f7fa, #fce4ec);
        color: #333;
    }
    .title {
        font-size: 42px;
        font-weight: bold;
        color: #5c6bc0;
        text-align: center;
        margin-top: 30px;
    }
    .subtitle {
        font-size: 20px;
        text-align: center;
        margin-bottom: 20px;
    }
    .career-box {
        background-color: #ffffffdd;
        border-radius: 15px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 2px 4px 12px rgba(0,0,0,0.1);
        text-align: center;
        font-size: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ 타이틀 ------------------ #
st.markdown('<div class="title">🔮 MBTI로 알아보는 나의 꿈! 🔮</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">당신의 MBTI를 선택하면 어울리는 직업을 추천해드릴게요! ✨</div>', unsafe_allow_html=True)

# ------------------ MBTI 목록 ------------------ #
mbti_list = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# ------------------ MBTI별 추천 직업 ------------------ #
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
    random.shuffle(careers)  # 직업 순서 랜덤

    for job in careers:
        st.markdown(f'<div class="career-box">{job}</div>', unsafe_allow_html=True)

# ------------------ 푸터 ------------------ #
st.markdown("""
<hr style="margin-top:50px;">
<p style='text-align:center; font-size:14px;'>📱 친구와 공유해보세요! | Made for 10대의 진로 탐색</p>
""", unsafe_allow_html=True)
