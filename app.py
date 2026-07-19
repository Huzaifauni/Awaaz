import streamlit as st

st.set_page_config(page_title="Awaaz", page_icon="🔊")

st.title("🔊 Awaaz")
st.subheader("AI Accessibility Tool")

st.write("Welcome to Awaaz!")

text = st.text_area("Enter English text:")

if st.button("Translate"):
    st.success("Translation will appear here!")