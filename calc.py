import streamlit as st

st.header('WELCOME TO MY CALCULATOR')
x=st.number_input('input your first number')
y=st.number_input('input your second number')

if st.button('add'):
    z=x+y
    st.write(z)
if st.button('subtract'):
    z=x-y
    st.write(z)
