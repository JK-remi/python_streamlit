import streamlit as st
import fincance_naver

# 사이드 바 화면
st.sidebar.header("Log In")
user_id = st.sidebar.text_input('ID', 'streamlit', 15)
user_pwd = st.sidebar.text_input('PWD', '1234', 20, type='password')

if user_pwd == '1234':
    st.sidebar.header('PORTFOLIO')
    opt_data = ['환율조회', '따릉이', '유성우']
    menu = st.sidebar.selectbox('SELECT MENU', opt_data, index=0)

    if menu == '환율조회':
        st.subheader(f'{menu} 데이터 분석>>>>>>  ')
        fincance_naver.exchange_main()
    elif menu == '따릉이':
        st.subheader(f'{menu} 데이터 분석>>>>>>  ')
    elif menu == '유성우':
        st.subheader(f'{menu} 데이터 분석>>>>>>  ')
    else:
        st.subheader('WELCOME ABOARD')