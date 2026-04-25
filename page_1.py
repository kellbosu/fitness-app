import streamlit as st

st.title("ENTER MAXES HERE")
st.write("ENTER MAXES HERE")
col1, col2, col3 = st.columns(3)
col2.button("New Program", width="stretch")

st.markdown("""
<style>
    .stButton>button {
        background-color: #FABC02;
        color: DarkOrchid;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.button("Styled Button")