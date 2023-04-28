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
  height: 1080px;
  padding: 40px 20px 20px 20px;
}

 p{
 font-size:60px;
 text-align:right;
 }
</style>
""", unsafe_allow_html = True)


if 'number' not in st.session_state:
  st.session_state["number"] = 0 #入力された数字保存用
  st.session_state["comma_count"] = 0 #表示用の式の小数点の前に0を挿入する用
  st.session_state["cal_count"] = 0 #演算回数カウント用
  st.session_state["equal_count"] = 1 #=が押された後の表示判定用
  st.session_state["answer"] = 0 #演算結果数字保存用
  st.session_state["formula"] = "0" #表示される色保存用
  st.session_state["deci"] = 0 #小数点ボタンの押下判定用
  st.session_state["comma"] = 0 #式に小数点代入用
  st.session_state["deci_count"] = -1 #小数点の桁数判定用
  st.session_state["equal"] = 0 #=押下時の残りの演算判定用
  st.session_state["deci_total_count"] = 0 #掛け算時の浮動小数点処理用
  st.session_state["cal_flag"] = 0

if st.session_state["equal_count"] == 2:
    st.session_state["formula"] = ""
    st.session_state["equal_count"] = 1

def deci_cal(x): #押下された数字入力用 x:int型
    st.session_state["cal_flag"] = 0
    if st.session_state["equal_count"] == 1:
        st.session_state["formula"] = ""
        st.session_state["equal_count"] = 0

    if st.session_state["deci"] == 1: #小数点が押されている場合は小数に変換し代入
        st.session_state["formula"] += str(x)
        st.session_state["number"] += x*10**(st.session_state["deci_count"])
        st.session_state["number"] = round(st.session_state["number"], (-1)*st.session_state["deci_count"])
        st.session_state["deci_count"] -= 1

    else: #小数点が押されていない場合は元の数字を10倍して足す
        st.session_state["comma_count"] += 1
        st.session_state["number"] *= 10
        st.session_state["number"] += x
        st.session_state["formula"] += str(x)

def on_ac_button_clicked(): #ACボタンが押されたら変数リセット
    st.session_state["cal_flag"] = 0
    st.session_state["comma_count"] = 0
    st.session_state["answer"] = 0
    st.session_state["cal_count"] = 0
    st.session_state["number"] = 0
    st.session_state["formula"] = "0"
    st.session_state["deci"] = 0
    st.session_state["deci_count"] = -1
    st.session_state["equal_count"] = 1
    st.session_state["comma"] = 0
    st.session_state["deci_total_count"] = 0

def on_equal_button_clicked(): #=ボタンが押された場合の処理
    if st.session_state["equal"] == 0:
        st.session_state["answer"] += st.session_state["number"]
        st.session_state["formula"] = st.session_state["answer"]

    if st.session_state["equal"] == 1:
        st.session_state["answer"] -= st.session_state["number"]
        st.session_state["answer"] = round(st.session_state["answer"], (-1)*st.session_state["deci_count"])
        st.session_state["formula"] = st.session_state["answer"]

    if st.session_state["equal"] == 2:
        st.session_state["deci_total_count"] *= (-1)*(st.session_state["deci_count"])
        st.session_state["answer"] *= st.session_state["number"]
        st.session_state["formula"] = round(st.session_state["answer"], (-1)*st.session_state["deci_total_count"])

    if st.session_state["equal"] == 3:
        st.session_state["answer"] /= st.session_state["number"]
        st.session_state["formula"] = st.session_state["answer"]

    st.session_state["comma_count"] = 0
    st.session_state["cal_count"] = 0
    st.session_state["number"] = 0
    st.session_state["deci"] = 0
    st.session_state["deci_count"] = -1
    st.session_state["equal_count"] = 2
    st.session_state["comma"] = 0
    st.session_state["deci_total_count"] = 0

def on_com_button_clicked():
    st.session_state["deci"] = 1
    if st.session_state["comma_count"]== 0:
        st.session_state["formula"] += "0"
    st.session_state["comma_count"] += 1
    if st.session_state["comma"] == 0:
        st.session_state["formula"] += "."
        st.session_state["comma"] += 1

def on_cle_button_clicked():
    st.session_state["cal_flag"] = 0
    st.session_state["number"] = int(st.session_state["number"]/10)
    st.session_state["formula"] = st.session_state["formula"][:-1]

def cal(x, y): #演算処理&答え表示処理 x:str型(+,-,×,÷), y:int型 y=0:和,y=1:差,y=2:積,y=3:商の判定
    st.session_state["cal_flag"] += 1
    if st.session_state["cal_flag"] == 1:
        if y == 0:
            if st.session_state["cal_count"] == 0:
                st.session_state["answer"] = st.session_state["number"]
                st.session_state["cal_count"] += 1
            else:
                st.session_state["answer"] += st.session_state["number"]

        if y == 1:
            if st.session_state["cal_count"] == 0:
                st.session_state["answer"] = st.session_state["number"]
                st.session_state["cal_count"] += 1
            else:
                st.session_state["answer"] -= st.session_state["number"]
                st.session_state["answer"] = round(st.session_state["answer"], (-1)*st.session_state["deci_count"])

        if y == 2:
            if st.session_state["cal_count"] == 0:
                st.session_state["answer"] = st.session_state["number"]
                st.session_state["cal_count"] += 1
                st.session_state["deci_total_count"] += st.session_state["deci_count"]
            else:
                st.session_state["deci_total_count"] *= (-1)*(st.session_state["deci_count"])
                st.session_state["answer"] *= st.session_state["number"]

        if y == 3:
            if st.session_state["cal_count"] == 0:
                st.session_state["answer"] = st.session_state["number"]
                st.session_state["cal_count"] += 1
            else:
                st.session_state["answer"] /= st.session_state["number"]

        st.session_state["formula"] += str(x)
        st.session_state["number"] = 0
        st.session_state["deci"] = 0
        st.session_state["deci_count"] = -1
        st.session_state["comma"] = 0
        st.session_state["equal"] = y



with st.container():
    a, output = st.columns([1,100])
    but_ac, but_cle, but_div = st.columns([2.04,1,1])
    but7, but8, but9, but_mlp = st.columns([1,1,1,1])
    but4, but5, but6, but_minus = st.columns([1,1,1,1])
    but3, but2, but1, but_pls = st.columns([1,1,1,1])
    but0, but_com, but_eql = st.columns([2.04,1,1])

    with but_ac:
        if st.button('AC', use_container_width=360):
            on_ac_button_clicked()
    with but_cle:
        if st.button('C', use_container_width=164):
            on_cle_button_clicked()
    with but_div:
        if st.button('÷', use_container_width=164):
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
            cal("+", 0)

    with but0:
        if st.button('0', use_container_width=360):
            deci_cal(0)

    with but_com:
        if st.button('.', use_container_width=164):
            on_com_button_clicked()
    with but_eql:
        if st.button('=', use_container_width=164):
            on_equal_button_clicked()

    with output:
        st.write('<span style="font-size:60px;background-color:#000000;color:#ffffff;text-align:right;">'+ str(st.session_state["formula"]) + '</span>',
                  unsafe_allow_html=True)
