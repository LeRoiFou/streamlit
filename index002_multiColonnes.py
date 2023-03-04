import streamlit as st

col1, col2, col3 = st.columns([1,1,1])

with col1:
    st.write("test")
    st.button('1')
with col2:
    st.button('2')
with col3:
    st.button('3')
    
