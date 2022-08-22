# -*- coding: utf-8 -*-
import os
os.chdir("C:/Users/Silver/Desktop/코딩/Wishlist") #작업공간 주소 입력
import pandas as pd
import folium
import json
with open('./skorea-municipalities-2018-geo.json',mode='rt',encoding='utf-8') as f:
    geo = json.loads(f.read())
    f.close() #행정구역 데이터 불러오기

# Df = pd.read_excel("./Wishlist.xlsx",header=None) #데이터 pandas로 읽어오기
Df = pd.read_csv("./Wishlist.csv",header=None) #데이터 pandas로 읽어오기
Df = Df.rename(columns=Df.iloc[0])
Df = Df.drop(Df.index[0])

lat = Df['위도'];
lon = Df['경도'];
name = Df['장소'];
arch = Df['달성'];
lat = lat.astype(float); #숫자로 타입 변경
lon = lon.astype(float);

style1 = {'fillColor': '#FFFFFF', 
          'lineColor': '#91d7ff', 
          'weight': 1, 
          'opacity': 0.65} #스타일 지정

m = folium.Map(location=[37.566345, 126.977893], zoom_start=10); #센터 위치 지정
folium.GeoJson(geo, name='sk_municipalities', style_function=lambda x:style1).add_to(m) #행정구역 지정하기, 스타일 지정

for i in range(1,len(lon)):
    if arch[i]==0:
        text = name[i] #위시리스트를 마커 형태로 지도에 추가
        iframe = folium.IFrame(text,width=150,height=50) #팝업창 크기 설정
        popup = folium.Popup(iframe, max_width=200) #팝업창 설정
        folium.Marker(
            location=[lat[i],lon[i]],
            popup=popup,
            icon=folium.Icon(color='red',icon='star')).add_to(m) #마커 설정 및 팝업창 배정
    else:
        text = name[i]
        iframe = folium.IFrame(text,width=150,height=50)
        popup = folium.Popup(iframe, max_width=200)
        folium.Marker(
            location=[lat[i],lon[i]],
            popup=popup,
            icon=folium.Icon(color='green',icon='star')).add_to(m)   
    del text, popup

m.save("./Wishlist.html"); #html 저장


