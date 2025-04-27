import streamlit as st
import pass_gen as pg

st.set_page_config(page_title="PASSWORD GENERATOR", layout = "centered")
st.header("Password generator")
st.write("\n\n\n")
size = st.text_input("Describe the length")
level = st.selectbox("hardness level", ['easy','medium', 'hard'])

if size:
    st.subheader("Your Password: ")
    pwd = pg.gen_pass(int(size), level)
    st.success(f"{pwd}")
    
