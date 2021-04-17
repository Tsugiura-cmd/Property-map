import folium
from streamlit_folium import folium_static
import streamlit as st
import numpy as np
import pandas as pd
from csv import reader

#------------csvファイルをリストに格納---------------
with open('list.csv', 'r',encoding="utf-8") as csv_file:
    csv_reader = reader(csv_file)
    # Passing the cav_reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)
    #print(list_of_rows)

list_array=np.array(list_of_rows[1:][:])
lon_lat=list_array[:,3:5] ##緯度経度抽出　2次元配列
#print(lon_lat)
##工事名抽出　1次元配列
name=list_array[:,1]
#print(name)




#------------csvファイルを表として表示---------------
#st.title("首都土施工物件一覧") # タイトル
def load_data(nrows):
    data = pd.read_csv("list.csv", nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

# Load 10,000 rows of data into the dataframe.
data = load_data(10000)

#st.write(data)

# ------------------------マッピング作成------------------------
# サンプル用の緯度経度データを作成する
sales_office = pd.DataFrame(
    data=lon_lat,
    index=name,
    columns=["x","y"]
)

# データを地図に渡す関数を作成する
def AreaMarker(df,m):
    for index, r in df.iterrows(): 

        # ピンをおく
        folium.Marker(
            location=[r.x, r.y],
            popup=index,
        ).add_to(m)

       

# ------------------------画面作成------------------------

#st.title("首都土施工物件マッピング") # タイトル
m = folium.Map(location=[35.688313,139.77679], zoom_start=7) # 地図の初期設定
AreaMarker(sales_office,m) # データを地図渡す
folium_static(m) # 地図情報を表示