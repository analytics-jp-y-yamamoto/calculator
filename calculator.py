import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div id="accordion">
      <div class="card">
        <div class="card-header" id="headingOne">
          <h5 class="mb-0">
            <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            Collapsible Group Item #1
            </button>
          </h5>
        </div>
        <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #1 content
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-header" id="headingTwo">
          <h5 class="mb-0">
            <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            Collapsible Group Item #2
            </button>
          </h5>
        </div>
        <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #2 content
          </div>
        </div>
      </div>
    </div>
    """,
    height=600,
)

name = "main"

if 'number' not in st.session_state:
  st.session_state["number"] = 0
  st.session_state["count"] = 0
  st.session_state["answer"] = 0
  st.session_state["formula"] = ""
  st.session_state["deci"] = 0
  st.session_state["deci_count"] = -1
  st.session_state["equal"] = 0

def main():
    c = st.container()
    output , a = st.columns([100,1])
    formula, a = st.columns([10000,1])
    answer, a = st.columns([1000000,1])
    but1, but2, but3, but4 = st.columns([1,1,1,1],gap= "small")

    with but1:
        if st.button('7'):
            deci_cal(7)

        if st.button('4'):
            deci_cal(4)

        if st.button('1'):
            deci_cal(1)

        if st.button('0'):
            st.session_state["number"] *= 10

    with but2:
        if st.button('8'):
            deci_cal(8)

        if st.button('5'):
            deci_cal(5)

        if st.button('2'):
            deci_cal(2)

        if st.button('C'):
                st.session_state["number"] = 0

    with but3:
        if st.button('9'):
            deci_cal(9)

        if st.button('6'):
            deci_cal(6)

        if st.button('3'):
            deci_cal(3)

        if st.button('AC'):
            st.session_state["count"] = 0
            st.session_state["answer"] = 0
            st.session_state["number"] = 0
            st.session_state["formula"] = ""
            st.session_state["deci"] = 0
            st.session_state["deci_count"] = -1

    with but4:
        if st.button('÷'):
            if st.session_state["count"] == 0:
                n_count(3)
            else:
                st.session_state["answer"] /= st.session_state["number"]
                cal("÷", 3)

        if st.button('×'):
            if st.session_state["count"] == 0:
                n_count(2)
            else:
                st.session_state["answer"] *= st.session_state["number"]
                cal("×", 2)

        if st.button('−'):
            if st.session_state["count"] == 0:
                n_count(1)
            else:
                st.session_state["answer"] -= st.session_state["number"]
                st.session_state["answer"] = round(st.session_state["answer"], (-1)*st.session_state["deci_count"])
                cal("-", 1)

        if st.button('\+'):
            if st.session_state["count"] == 0:
                n_count(0)
            else:
                st.session_state["answer"] += st.session_state["number"]
                cal("+", 0)

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

        if st.button('.'):
            st.session_state["deci"] = 1

    with output:
        st.write('<span style="font-size:30px;background-color:#000000;color:#ffffff">入力:'+ str(st.session_state["number"]) + '</span>',
                  unsafe_allow_html=True)

    with formula:
        st.write('<span style="font-size:20px">式:' + st.session_state["formula"]+ '</span>',
                  unsafe_allow_html=True)

    with answer:
        st.write('<span style="font-size:20px">答え:' + str(st.session_state["answer"]) + '</span>',
                  unsafe_allow_html=True)


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

if name == 'main':
  main()
