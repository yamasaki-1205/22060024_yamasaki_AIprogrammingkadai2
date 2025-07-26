import requests

def get_cat_images_by_breed(breed_name):
    """
    猫種（breed_name）で画像を取得
    breed_nameは小文字推奨
    """
    # まず猫種一覧を取得してIDを探す
    breeds_url = "https://api.thecatapi.com/v1/breeds"
    response = requests.get(breeds_url)
    if response.status_code != 200:
        return None, "APIへの接続に失敗しました。"
    breeds = response.json()
    
    # 入力のbreed_nameに一致する猫種のidを探す
    breed_id = None
    for breed in breeds:
        if breed_name.lower() in breed["name"].lower():
            breed_id = breed["id"]
            break
    
    if not breed_id:
        return None, f"「{breed_name}」に該当する猫種が見つかりません。"
    
    # 猫種IDで画像検索
    images_url = f"https://api.thecatapi.com/v1/images/search?breed_ids={breed_id}&limit=5"
    img_response = requests.get(images_url)
    if img_response.status_code != 200:
        return None, "画像の取得に失敗しました。"
    images = img_response.json()
    if not images:
        return None, "画像が見つかりませんでした。"
    
    # 画像URLだけ抽出してリスト化
    img_urls = [img["url"] for img in images]
    return img_urls, None
