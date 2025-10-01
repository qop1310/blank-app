import streamlit as st

st.title("Calculus note")
st.success("Fundamental Theorem of Calculus")
st.info("빨간색 영역의 넓이는 A(x+h)-A(x)이며 h가 충분히 작을 때 f(x)h로 근사가능하다. 따라서 충분히 작은 양수 h에 대해 {A(x+h)-A(x)}/h = f(x)이므로 A'(x)=f(x)이다.")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/FTC_geometric.svg/750px-FTC_geometric.svg.png")
st.latex(r"e^{i\pi} + 1 = 0")
st.link_button("그래프 그리기", "https://www.desmos.com/calculator?lang=ko")
# st.markdown(): 마크다운 문법 지원 (굵게, 기울임, 목록 등)
st.markdown("**굵은 텍스트**, *기울임 텍스트*")
st.markdown("""- 첫 번째 항목
- 두 번째 항목
- 여러 줄을 쓸 때""")
# 수평선 (구분선) 출력
st.markdown("---")  # 또는
st.divider()        # Streamlit >= 1.22 이상에서 가능
# st.tabs(["이름1", "이름2", ...]): 탭 인터페이스 생성
tab1, tab2 = st.tabs(["탭 1", "탭 2"])  # 2개의 탭 생성

with tab1:
    st.write("탭 1에 해당하는 내용입니다.")  # 첫 번째 탭에 표시할 내용
with tab2:
    st.write("탭 2에 해당하는 내용입니다.")  # 두 번째 탭에 표시할 내용
# st.expander("제목"): 내용을 접었다 펼 수 있는 컨테이너입니다
with st.expander("ℹ️ 자세한 설명 보기"):
    st.write("여기에 상세 설명이나 보조 정보를 넣을 수 있습니다.")
# st.sidebar: 사이드바 영역에 콘텐츠를 배치합니다
st.sidebar.title("📌 사이드바 메뉴")
option = st.sidebar.selectbox("옵션을 선택하세요", ["A", "B", "C"])
st.write("선택한 옵션:", option)
# 여러 옵션 중 하나 선택
subject = st.radio("좋아하는 과목을 선택하세요", ["수학", "물리", "화학", "국어", "영어", "기타"])
st.write("선택한 과목:", subject)