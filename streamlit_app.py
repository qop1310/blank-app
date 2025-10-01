import streamlit as st

st.title("Calculus note")
st.success("Fundamental Theorem of Calculus")
st.info("빨간색 영역의 넓이는 A(x+h)-A(x)이며 h가 충분히 작을 때 f(x)h로 근사가능하다. 따라서 충분히 작은 양수 h에 대해 {A(x+h)-A(x)}/h = f(x)이므로 A'(x)=f(x)이다.")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/FTC_geometric.svg/750px-FTC_geometric.svg.png")