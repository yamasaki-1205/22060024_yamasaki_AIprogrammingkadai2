import streamlit as st
from logic import get_cat_images_by_breed

st.title("猫の種類で画像検索アプリ")

breed_input = st.text_input("猫の種類名を入力してください（例: bengal, siamese）")

if breed_input:
    with st.spinner("画像を取得中…"):
        urls, error = get_cat_images_by_breed(breed_input.strip())
    if error:
        st.error(error)
    else:
        st.success(f"{len(urls)}枚の画像を見つけました！")
        for url in urls:
            st.image(url, width=300)
