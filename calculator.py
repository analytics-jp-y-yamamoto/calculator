import streamlit as st
import pandas as pd

st.markdown("""
<style>
div.row-widget.stButton > button:first-child  {
  background-color: #494949;
  color: #ffffff;
  height: 164px;
}

div.row-widget.stButton > button:hover  {
  background-color: #494949;
  color: #ffffff;
}

div.block-container{
  background-color: #0C0C0C;
  color: #00ffff;
  height: 1200px;
}

 p{
 font-size:60px;
 }
</style>
""", unsafe_allow_html = True)


if 'number' not in st.session_state:
  st.session_state["number"] = 0
  st.session_state["comma_count"] = 0
  st.session_state["cal_count"] = 0
  st.session_state["equal_count"] = 1
  st.session_state["answer"] = 0
  st.session_state["formula"] = "0"
  st.session_state["deci"] = 0
  st.session_state["comma"] = 0
  st.session_state["deci_count"] = -1
  st.session_state["equal"] = 0

if st.session_state["equal_count"] == 2:
    st.session_state["formula"] = "0"
    st.session_state["equal_count"] = 1

def main():
    x = len(st.session_state["formula"])
    a, output = st.columns([20-0.9*x,0.9*x+2])
    but_ac, but_cle, but_div = st.columns([2.04,1,1])
    but7, but8, but9, but_mlp = st.columns([1,1,1,1])
    but4, but5, but6, but_minus = st.columns([1,1,1,1])
    but3, but2, but1, but_pls = st.columns([1,1,1,1])
    but0, but_com, but_eql = st.columns([2.04,1,1])

    with but_ac:
        if st.button('AC', use_container_width=360):
            st.session_state["comma_count"] = 0
            st.session_state["answer"] = 0
            st.session_state["cal_count"] = 0
            st.session_state["number"] = 0
            st.session_state["formula"] = "0"
            st.session_state["deci"] = 0
            st.session_state["deci_count"] = -1
            st.session_state["equal_count"] = 1
    with but_cle:
        if st.button('C', use_container_width=164):
                st.session_state["number"] = 0
                st.session_state["formula"] = st.session_state["formula"][:-1]
    with but_div:
        if st.button('÷', use_container_width=164):
            if st.session_state["cal_count"] == 0:
                st.session_state["answer"] = st.session_state["number"]
                st.session_state["cal_count"] += 1
            else:
                st.session_state["answer"] /= st.session_state["number"]
            cal("÷", 3)

    with but7:
        if st.button('7', use_container_width=164):
            deci_cal(7)
    with but8:
        if st.button('8',use_container_width=164):
            deci_cal(8)
    with but9:
        if st.button('9',use_container_width=164):
            deci_cal(9)
    with but_mlp:
        if st.button('×', use_container_width=164):
            if st.session_state["cal_count"] == 0:
                st.session_state["answer"] = st.session_state["number"]
                st.session_state["cal_count"] += 1
            else:
                st.session_state["answer"] *= st.session_state["number"]
            cal("×", 2)


    with but4:
        if st.button('4', use_container_width=164):
            deci_cal(4)
    with but5:
        if st.button('5', use_container_width=164):
            deci_cal(5)
    with but6:
        if st.button('6', use_container_width=164):
            deci_cal(6)
    with but_minus:
        if st.button('−', use_container_width=164):
            if st.session_state["cal_count"] == 0:
                st.session_state["answer"] = st.session_state["number"]
                st.session_state["cal_count"] += 1
            else:
                st.session_state["answer"] -= st.session_state["number"]
                st.session_state["answer"] = round(st.session_state["answer"], (-1)*st.session_state["deci_count"])
            cal("-", 1)


    with but3:
        if st.button('1', use_container_width=164):
            deci_cal(1)
    with but2:
        if st.button('2', use_container_width=164):
            deci_cal(2)
    with but1:
        if st.button('3', use_container_width=164):
            deci_cal(3)
    with but_pls:
        if st.button('\+', use_container_width=164):
            if st.session_state["cal_count"] == 0:
                st.session_state["answer"] = st.session_state["number"]
                st.session_state["cal_count"] += 1
            else:
                st.session_state["answer"] += st.session_state["number"]
            cal("+", 0)

    with but0:
        if st.button('0', use_container_width=360):
            deci_cal(0)

    with but_com:
        if st.button('.', use_container_width=164):
            st.session_state["deci"] = 1
            if st.session_state["comma_count"]== 0:
                st.session_state["formula"] += "0"
            st.session_state["comma_count"] += 1
            if st.session_state["comma"] == 0:
                st.session_state["formula"] += "."
                st.session_state["comma"] += 1
    with but_eql:
        if st.button('=', use_container_width=164, key ='='):
            if st.session_state["equal"] == 0:
                st.session_state["answer"] += st.session_state["number"]
                st.session_state["formula"] = st.session_state["answer"]

            if st.session_state["equal"] == 1:
                st.session_state["answer"] -= st.session_state["number"]
                st.session_state["formula"] = st.session_state["answer"]

            if st.session_state["equal"] == 2:
                st.session_state["answer"] *= st.session_state["number"]
                st.session_state["formula"] = st.session_state["answer"]

            if st.session_state["equal"] == 3:
                st.session_state["answer"] /= st.session_state["number"]
                st.session_state["formula"] = st.session_state["answer"]

            st.session_state["comma_count"] = 0
            st.session_state["cal_count"] = 0
            st.session_state["number"] = 0
            st.session_state["deci"] = 0
            st.session_state["deci_count"] = -1
            st.session_state["equal_count"] = 2

    with output:
        st.write('<span style="font-size:60px;background-color:#000000;color:#ffffff;text-align:right">'+ str(st.session_state["formula"]) + '</span>',
                  unsafe_allow_html=True)

def deci_cal(x):
    if st.session_state["equal_count"] == 1:
        st.session_state["formula"] = ""
        st.session_state["equal_count"] = 0
    if st.session_state["deci"] == 1:
        st.session_state["formula"] += str(x)
        st.session_state["number"] += x*10**(st.session_state["deci_count"])
        st.session_state["number"] = round(st.session_state["number"], (-1)*st.session_state["deci_count"])
        st.session_state["deci_count"] -= 1

    else:
        st.session_state["comma_count"] += 1
        st.session_state["number"] *= 10
        st.session_state["number"] += x
        st.session_state["formula"] += str(x)

def cal(x, y):
    st.session_state["formula"] += str(x)
    st.session_state["number"] = 0
    st.session_state["deci"] = 0
    st.session_state["deci_count"] = -1
    st.session_state["comma"] = 0
    st.session_state["equal"] = y

with st.container():
    main()
