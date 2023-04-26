import streamlit as st
import pandas as pd

with open('calculater.css') as f:
        st.markdown(f'<style>{f.read()}</style',unsafe_allow_html = True)

if 'number' not in st.session_state:
  st.session_state["number"] = 0
  st.session_state["count"] = 0
  st.session_state["answer"] = 0
  st.session_state["formula"] = ""
  st.session_state["deci"] = 0
  st.session_state["deci_count"] = -1
  st.session_state["equal"] = 0

output , a = st.columns([100,1])
formula, a = st.columns([10000,1])
answer, a = st.columns([1000000,1])
but7, but8, but9, but_divide = st.columns(4)
but4, but5, but6, but_multi = st.columns(4)
but1, but2, but3, but_minus = st.columns(4)
but0, but_clear, but_all_clear, but_plus = st.columns(4)
a, a, but_deci, but_equal = st.columns(4)

def deci_cal(x):
    if st.session_state["deci"] == 1:
        st.session_state["number"] += x*10**(st.session_state["deci_count"])
        st.session_state["number"] = round(st.session_state["number"], (-1)*st.session_state["deci_count"])
        st.session_state["deci_count"] -= 1

    else:
        st.session_state["number"] *= 10
        st.session_state["number"] += x

def n_count(x):
    st.session_state["answer"] = st.session_state["number"]
    st.session_state["number"] = 0
    st.session_state["count"] += 1
    st.session_state["formula"] += str(st.session_state["answer"]) + "="
    st.session_state["deci"] = 0
    st.session_state["deci_count"] = -1
    st.session_state["equal"] = x

def cal(x, y):
    st.session_state["formula"] = str(st.session_state["formula"])[:-1]
    st.session_state["formula"] += x + str(st.session_state["number"]) + "="
    st.session_state["number"] = 0
    st.session_state["count"] += 1
    st.session_state["deci"] = 0
    st.session_state["deci_count"] = -1
    st.session_state["equal"] = y

with but0:
    if st.button('0'):
        st.session_state["number"] *= 10

with but1:
    if st.button('1'):
        deci_cal(1)

with but2:
    if st.button('2'):
        deci_cal(2)

with but3:
    if st.button('3'):
        deci_cal(3)

with but4:
    if st.button('4'):
        deci_cal(4)

with but5:
    if st.button('5'):
        deci_cal(5)

with but6:
    if st.button('6'):
        deci_cal(6)

with but7:
    if st.button('7'):
        deci_cal(7)

with but8:
    if st.button('8'):
        deci_cal(8)

with but9:
    if st.button('9'):
        deci_cal(9)

with but_plus:
    if st.button('\+'):
        if st.session_state["count"] == 0:
            n_count(0)
        else:
            st.session_state["answer"] += st.session_state["number"]
            cal("+", 0)

with but_minus:
    if st.button('−'):
        if st.session_state["count"] == 0:
            n_count(1)
        else:
            st.session_state["answer"] -= st.session_state["number"]
            st.session_state["answer"] = round(st.session_state["answer"], (-1)*st.session_state["deci_count"])
            cal("-", 1)

with but_multi:
    if st.button('×'):
        if st.session_state["count"] == 0:
            n_count(2)
        else:
            st.session_state["answer"] *= st.session_state["number"]
            cal("×", 2)

with but_divide:
     if st.button('÷'):
         if st.session_state["count"] == 0:
             n_count(3)
         else:
             st.session_state["answer"] /= st.session_state["number"]
             cal("÷", 3)

with but_equal:
    if st.button('='):
        if st.session_state["equal"] == 0:
            st.session_state["answer"] += st.session_state["number"]
            cal("+", 0)

        if st.session_state["equal"] == 1:
            st.session_state["answer"] -= st.session_state["number"]
            cal("-", 1)

        if st.session_state["equal"] == 2:
            st.session_state["answer"] *= st.session_state["number"]
            cal("×", 2)

        if st.session_state["equal"] == 3:
            st.session_state["answer"] /= st.session_state["number"]
            cal("÷", 3)


with but_all_clear:
    if st.button('AC'):
        st.session_state["count"] = 0
        st.session_state["answer"] = 0
        st.session_state["number"] = 0
        st.session_state["formula"] = ""
        st.session_state["deci"] = 0
        st.session_state["deci_count"] = -1

with but_clear:
    if st.button('C'):
        st.session_state["number"] = 0

with but_deci:
    if st.button('.'):
        st.session_state["deci"] = 1

with output:
    st.write('<span style="font-size:30px">入力:'+ str(st.session_state["number"]) + '</span>',
              unsafe_allow_html=True)

with formula:
    st.write('<span style="font-size:20px">式:' + st.session_state["formula"]+ '</span>',
              unsafe_allow_html=True)

with answer:
    st.write('<span style="font-size:20px">答え:' + str(st.session_state["answer"]) + '</span>',
              unsafe_allow_html=True)
