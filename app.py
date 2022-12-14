import streamlit as st
from bul_image_maker import bul_image_maker


def main():

    st.title("ぼやかしの入った白黒画像メーカー")

    height = st.slider(
        label="タテのサイズ",
        min_value=200,
        max_value=1000,
        value=500,
    )

    width = st.slider(
        label="ヨコのサイズ",
        min_value=200,
        max_value=1000,
        value=500,
    )

    times = st.slider(
        label="試行回数",
        min_value=5,
        max_value=100,
        value=30,
    )

    status_area = st.empty()

    if st.button("処理の実行"):
        x = bul_image_maker(height, width, times, status_area)
        st.image(x)


if __name__ == "__main__":

    main()
