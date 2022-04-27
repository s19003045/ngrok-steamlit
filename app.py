import streamlit as st
import numpy as np
import pandas as pd


def main():
    # header

    sidebar = st.sidebar
    with sidebar:
        st.write('sidebar')

    st.header('ngrok + streamlit')
    container = st.container()


    with container:
        st.subheader("加減乘除")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            input_a = st.number_input("變數1")

        with col2:
            input_b = st.radio("方式",("+","-","*","/"))

        with col3:
            input_c = st.number_input("變數2")

        with col4:
            st.write('結果')
            res = 0
            if input_b == "+":
                res = st.write(input_a + input_c)
            elif input_b == "-":
                res = st.write(input_a - input_c)
            elif input_b == "*":
                res = st.write(input_a * input_c)
            elif input_b == "/":
                res = st.text(input_a / input_c)

    def fibonacci_of(n):
        if n in {0, 1}:  # Base case
            return n
        return fibonacci_of(n - 1) + fibonacci_of(n - 2)

    container2 = st.container()
    with container2:
        st.subheader('fibonacci')
        st.write("第 n 個數字的大小 = (第 n-2 個) + (第 n-1 個數字)")
        col1, col2 = st.columns(2)
        with col1:
            input_2_a = st.number_input("數列長度", min_value=0, step=1)
        with col2:
            result_list = [fibonacci_of(n) for n in range(input_2_a)]
            st.write("陣列：")
            st.write("{}".format(str(result_list)))


    container3 = st.container()
    with container3:
        st.subheader('串接字串')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            input_3_a = st.text_input("字串 1")
        with col2:
            input_3_b = st.text_input("字串 2")
        with col3:
            input_3_c = st.text_input("字串 3")
        with col4:
            input_3_result = input_3_a + input_3_b + input_3_c
            st.write("字串結果")
            st.write(f"{input_3_result}")

    container4 = st.container()
    with container4:
        st.subheader("Color picker")
        color = st.color_picker('Pick A Color', '#00f900')
        st.write('The current color is', color)


    container5 = st.container()
    with container5:
        st.subheader("Line chart")
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c'])

        st.line_chart(chart_data)


if __name__ == "__main__":
    main()