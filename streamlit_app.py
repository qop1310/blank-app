import streamlit as st

st.set_page_config(page_title="무한 적분 퀴즈", layout="centered")
st.title("📘 무한 적분 공식 퀴즈")
st.markdown("주요 적분 공식을 확인하고, 해당 문제를 풀어보세요.")
st.warning("※ 정답에는 적분 상수 **`+ C`** 를 포함하지 마세요.")

# 퀴즈 데이터
quiz_data = [
    {
        "id": 1,
        "formula_name": "거듭제곱 함수의 적분 공식",
        "formula_latex": r"\int x^n dx = \frac{1}{n+1}x^{n+1} + C \quad (n \neq -1)",
        "problem_latex": r"\int x^5 dx",
        "correct_answer": r"\frac{1}{6}x^6 + C",
        "simplified_answer": "x^6/6"
    },
    {
        "id": 2,
        "formula_name": "역수 함수의 적분 공식",
        "formula_latex": r"\int \frac{1}{x} dx = \ln|x| + C",
        "problem_latex": r"\int \frac{3}{x} dx",
        "correct_answer": r"3\ln|x| + C",
        "simplified_answer": "3ln(|x|)"
    },
    {
        "id": 3,
        "formula_name": "지수 함수의 적분 공식",
        "formula_latex": r"\int e^x dx = e^x + C",
        "problem_latex": r"\int e^{x+2} dx",
        "correct_answer": r"e^{x+2} + C",
        "simplified_answer": "e^(x+2)"
    },
    {
        "id": 4,
        "formula_name": "삼각 함수 (사인) 적분 공식",
        "formula_latex": r"\int \sin(x) dx = -\cos(x) + C",
        "problem_latex": r"\int 2\sin(x) dx",
        "correct_answer": r"-2\cos(x) + C",
        "simplified_answer": "-2cos(x)"
    },
    {
        "id": 5,
        "formula_name": "삼각 함수 (코사인) 적분 공식",
        "formula_latex": r"\int \cos(x) dx = \sin(x) + C",
        "problem_latex": r"\int (\cos(x) - 1) dx",
        "correct_answer": r"\sin(x) - x + C",
        "simplified_answer": "sin(x)-x"
    }
]

# 사용자 입력 정규화
def normalize(ans):
    return ans.lower().replace(" ", "").replace("\\", "").replace("|", "").replace("(", "").replace(")", "").replace("+c", "")

# 퀴즈 렌더링
for quiz in quiz_data:
    st.divider()
    st.subheader(f"🧠 {quiz['formula_name']}")
    st.latex(quiz['formula_latex'])

    st.markdown("**적용 문제:**")
    st.latex(quiz['problem_latex'])

    st.markdown("정답을 수식 형태가 아닌 문자열로 입력하세요. 예: `x^6/6`, `3ln(|x|)`")
    user_input = st.text_input("정답 f(x) =", key=f"input_{quiz['id']}")
    col1, col2 = st.columns(2)

    if col1.button("채점하기", key=f"check_{quiz['id']}"):
        if not user_input:
            st.warning("답을 입력해주세요.")
        else:
            user = normalize(user_input)
            correct = normalize(quiz["simplified_answer"])
            if user == correct:
                st.success("🎉 정답입니다!")
                st.latex(f"f(x) = {quiz['correct_answer']}")
            else:
                st.error("❌ 오답입니다. 공식을 다시 확인해보세요.")

    if col2.button("정답 보기", key=f"show_{quiz['id']}"):
        st.info("📌 정답은 다음과 같습니다:")
        st.latex(f"f(x) = {quiz['correct_answer']}")
