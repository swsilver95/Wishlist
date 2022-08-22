# -*- coding: utf-8 -*-
import os
import pandas as pd
import folium
import json
import webbrowser

# ------------------------------------------------
# 작업공간 절대경로 입력
# ------------------------------------------------
os.chdir("C:/Users/Silver/Desktop/코딩/Wishlist")

# ------------------------------------------------
# 행정구역 데이터 불러오기
# ------------------------------------------------
with open('./skorea-municipalities-2018-geo.json',mode='rt',encoding='utf-8') as f:
    geo = json.loads(f.read())
    f.close()
    
# ------------------------------------------------
# 데이터 pandas로 읽어오기
# ------------------------------------------------
Df = pd.read_csv("./Wishlist.csv",header=None)
Df = Df.rename(columns=Df.iloc[0])
Df = Df.drop(Df.index[0])

# ------------------------------------------------
# 데이터프레임으로부터 컬럼 값 불러와서 저장하기
# ------------------------------------------------
lat = Df['위도']
lon = Df['경도']
name = Df['장소']
arch = Df['달성']
lat = lat.astype(float)
lon = lon.astype(float)

# ------------------------------------------------
# 지도 스타일 지정
# ------------------------------------------------
style1 = {
    'fillColor': '#FFFFFF', 
    'lineColor': '#91d7ff', 
    'weight': 1, 
    'opacity': 0.65     
}


# ------------------------------------------------
# 지도 상세설정
# ------------------------------------------------
# 1. 지도 센터 위치 지정
m = folium.Map(location=[37.566345, 126.977893], zoom_start=10)

# 2. 지도 행정구역 지정 및 스타일 적용
folium.GeoJson(geo, name='sk_municipalities', style_function=lambda x:style1).add_to(m)

# ------------------------------------------------
# 마커 세팅 및 설정
# ------------------------------------------------
for i in range(1,len(lon)):
    # A. 아직 위시플레이스 달성을 못 했을 때
    if arch[i]==0:
        # 1. 위시리스트의 이름을 지정
        text = name[i]
        
        # 2. 리스트 클릭시 팝업창의 크기 지정
        iframe = folium.IFrame(text,width=150,height=50)
        
        # 3. 리스트 클릭시 팝업창 설정
        popup = folium.Popup(iframe, max_width=200)
        
        # 4. 마커 등록
        folium.Marker(
            location=[lat[i],lon[i]],
            popup=popup,
            icon=folium.Icon(color='red',icon='star')).add_to(m)
    # B. 위시플레이스 달성했을 때
    else:
        text = name[i]
        iframe = folium.IFrame(text,width=150,height=50)
        popup = folium.Popup(iframe, max_width=200)
        folium.Marker(
            location=[lat[i],lon[i]],
            popup=popup,
            icon=folium.Icon(color='green',icon='star')).add_to(m)   
    del text, popup

# ------------------------------------------------
# html 파일 저장 및 html 자동 오픈
# ------------------------------------------------
m.save("./Wishlist.html")
ap = os.path.abspath("./Wishlist.html")
webbrowser.open(ap)
