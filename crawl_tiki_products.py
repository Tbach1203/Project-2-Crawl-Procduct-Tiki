import pandas as pd
import requests
import json
import time
from tqdm import tqdm
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'
}

def get_Id(df):
    return df['id'].tolist()

def clean_html(html_text):
    if html_text is None:
        return ""
    soup = BeautifulSoup(html_text, "html.parser")
    return soup.get_text(separator=" ", strip=True)

def product(data):
    return {
        "id": data.get("id"),
        "name": data.get("name"),
        "url_key": data.get("url_key"),
        "price": data.get("price"),
        "description": clean_html(data.get("description")),
        "images": data.get("images")[0].get("base_url")
    }

def info_Products(ids):
    result = []
    for id in tqdm(ids, total=len(ids)):
        response = requests.get(url='https://api.tiki.vn/product-detail/api/v1/products/{}'.format(id), headers=headers, timeout=10)
        if response.status_code == 200:
            result.append(product(response.json()))
            with open('products.json', 'w', encoding='utf-8') as file:
                json.dump(result, file, indent=4, ensure_ascii=False)
            # time.sleep(2)
        
if __name__ == "__main__":
    df = pd.read_csv('products-0-200000.csv')
    ids = get_Id(df)
    info_Products(ids)
  
    


    
    
