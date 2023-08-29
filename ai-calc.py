import streamlit as st

st.title("Assessment Index Calculator")

if 'adv' not in st.session_state:
    st.session_state['adv'] = 0
if 'mast' not in st.session_state:
    st.session_state['mast'] = 0
if 'basic' not in st.session_state:
    st.session_state['basic'] = 0
if 'appbas' not in st.session_state:
    st.session_state['appbas'] = 0
if 'unsat' not in st.session_state:
    st.session_state['unsat'] = 0
   
col1, col2, col3, col4, col5 = st.columns(5)
with col1: 
    num_adv = st.number_input("Advanced", key='adv', step=1)
with col2:
    num_mast = st.number_input("Mastery", key='mast', step=1)
with col3:
    num_basic = st.number_input("Basic", key='basic', step=1)
with col4:
    num_appbas = st.number_input("Approaching Basic", key='appbas', step=1)
with col5:
    num_unsat = st.number_input("Unsatisfactory", key='unsat', step=1)
    
total_num = num_adv + num_mast + num_basic + num_appbas + num_unsat
if total_num != 0:    
    ass_index = st.text_area("Assessment Index", value=round((((num_adv*150)+(num_mast*100)+(num_basic))/total_num), 1))
else:
    st.write("Assessment Index incoming ...")
