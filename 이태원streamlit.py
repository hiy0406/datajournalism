import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import seaborn as sb
import matplotlib.pyplot as plt
import altair as alt
plt.rcParams['font.family'] = 'NanumGothic'

path = "./"

@st.cache
def load_data(filename):
    data = pd.read_csv(filename)
    return data


# Webpage Title
st.title("이태원 참사, 남겨진 상인들")

st.subheader("데이터저널리즘 8조 김미주, 이예은, 임채림, 허인영")

st.write("모두의 마음에 상처로 남은 10월의 이태원. 사람들의 발길이 끊긴 그곳에는 오늘도 가게 문을 여는 상인들이 있습니다.")
st.markdown("***")

#이태원 참사 개요
st.markdown(
"""
## 이태원 참사, 그 날의 기록

테스트~~

***     
""")

#참사 전후 이태원에 대한 인식 변화
st.markdown("## 사고 전후 이태원에 대한 인식 변화")

st.markdown("### 참사 이후 현재까지의 워드클라우드")
img=Image.open(path+"after10.png")
st.image(img, caption='2022-10-30 ~ 2022-12-8')

st.markdown("### 상권 지원 이후 현재까지의 워드클라우드")
img=Image.open(path+"after_support.png")
st.image(img, caption='2022-11-24~ 2022-12-8')

st.markdown("### 참사 이전 한 달간의 워드클라우드")
img=Image.open(path+"2022_10.png")
st.image(img, caption='2022-10-1 ~ 2022-10-28')

st.markdown("### 참사 이전, 코로나 기간 동안의 워드클라우드")
img=Image.open(path+"after_corona.png")
st.image(img, caption='2020-01-20 ~ 2022-10-28')

st.markdown("### 코로나 이전 기간의 워드클라우드")
img=Image.open(path+"before_corona.png")
st.image(img, caption='2019-08-19 ~ 2020-01-19')

st.markdown("---")

#이태원 상인 지원에 대한 인식
st.markdown("## 이태원 상인 지원에 대한 대중들의 반응")
youtube_comments = load_data(path+"youtube_result2.csv")
count=youtube_comments['new'].value_counts()
labels = [0,1,'none']
data = []
for label in labels:
    data.append(count[label])
labels=['Negative','긍정','판단 불가']

colors = sb.color_palette('pastel')
fig1 = plt.figure(figsize=(16,8))
plt.pie(data, labels=labels, colors=colors, autopct='%.0f%%')
st.pyplot(fig1)

st.markdown("---")

#이태원 상권 변화
DataFrame = load_data(path+'2017searching.csv')

st.markdown("## 이태원 상권 붕괴 현황")
st.markdown("### 이태원 맛집 검색량 추이")
# df2 = pd.read_csv(path+'2017searching.csv')
# st.dataframe( df2.head() )
# st.bar_chart(df2[ ['search'] ] )
# chart = alt.Chart(df2).mark_circle().encode( x = 'search', y='date', color = 'species' )
# st.altair_chart(chart, use_container_width=True)

st.markdown("### 이태원 1동의 유동인구 및 매출 변화")
img=Image.open(path+"pop1.png")
st.image(img)
img=Image.open(path+"sales1.png")
st.image(img)

st.markdown("### 이태원 2동의 유동인구 및 매출 변화")
img=Image.open(path+"pop2.png")
st.image(img)
img=Image.open(path+"sales2.png")
st.image(img)

st.markdown("---")

#사회에 미친 영향
st.markdown("## 무너진 이태원 상권, 그 영향은?")
st.markdown("---")
