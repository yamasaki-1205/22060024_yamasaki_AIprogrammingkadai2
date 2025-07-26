import csv
import os

CSV_FILE = "history.csv"

def save_search_result(breed_name, image_urls):
    """検索結果をCSVファイルに保存"""
    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for url in image_urls:
            writer.writerow([breed_name, url])

def read_search_history():
    """CSVファイルから履歴を読み込む"""
    if not os.path.exists(CSV_FILE):
        return []
    with open(CSV_FILE, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        return list(reader)
