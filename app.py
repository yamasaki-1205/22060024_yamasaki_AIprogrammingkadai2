import streamlit as st
from logic import get_cat_images_by_breed
from data_handler import save_search_result, read_search_history

st.set_page_config(page_title="猫画像検索アプリ", page_icon="🐱")

st.title("🐾 猫の種類で画像検索アプリ")

# 入力ボックス
breed_input = st.text_input("猫の種類名を英語で入力してください（例: Siberian, Munchkin）")

# 検索ボタン
if st.button("画像を検索"):
    if breed_input:
        with st.spinner("画像を取得中…"):
            urls, error = get_cat_images_by_breed(breed_input.strip())
        if error:
            st.error(error)
        else:
            st.success(f"{len(urls)}枚の画像が見つかりました！")
            save_search_result(breed_input.strip(), urls)  # 検索履歴をCSVに保存
            for url in urls:
                st.image(url, width=300)
    else:
        st.warning("猫の猫種を入力してください。")

# 検索履歴表示
st.markdown("---")
st.subheader("📜 検索履歴")

history = read_search_history()

# 実際に履歴があるかチェックして表示
if len(history) > 0:
    for row in history[-5:][::-1]:  # 直近5件だけ表示（逆順）
        breed, img_url = row
        st.markdown(f"🔸 {breed}")
        st.image(img_url, width=300)
else:
    st.write("まだ履歴がありません。")
