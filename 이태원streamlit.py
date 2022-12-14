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
st.title("10.29(2022) 참사, 남겨진 상인들")
st.markdown("### 사람들의 발길이 끊긴 그곳에는 오늘도 가게 문을 여는 상인들이 있습니다")
st.write("  기사를 시작하기에 앞서, 10.29(2022) 참사로 사망한 분들의 명복을 빕니다." )
st.write("  2022년 10월 29일, 이태원에서 비극적인 압사 참사가 일어났습니다. 핼로윈을 이틀 남긴 10월의 토요일, 코로나 19 확산세가 어느 정도 감소하여 약 3년 만에 사회적 거리두기 없이 핼러윈 축제를 즐기기 위해 수많은 인구가 이태원으로 몰렸습니다. 즐거움으로 가득해야만 했던 거리, 하지만 오후 10시 15분 경 도시는 순식간에 비명소리와 사이렌 소리도 뒤덮혀 버렸습니다. 폭이 채 5m가 되지 않는 해밀턴호텔 옆 골목에서 대규모 압사가 시작되었기 때문이죠. 이 끔찍한 사고로 인해 158명이 사망했고, 197명이 부상을 당하는 등 300명이 넘는 사상자가 발생하였습니다." )
st.write("  서울에 거주하고 있는 2030 청년들은 이날 수많은 연락들을 받으셨을 거예요. 가족들은 물론 주변 지인들 모두 급하게 연락을 돌려 서로의 안부를 확인하고 가슴을 쓸어내렸다고 합니다. 실제로 국내 이동통신 3사에 따르면, 참사 발생한 직후부터 다음날까지 전국적으로 유의미한 트래픽 증가가 있었다고 해요.  사람들은 한 명씩 늘어나는 부상자와 사망자 수를 보며 엄청난 공포감에 휩싸였습니다. 서울 도심에서 이러한 대규모 인명피해가 발생한 것은 1995년 삼풍백화점 이후로 처음이었기 때문이었어요. 정부는 참사 이후 10월 30일부터 11월 5일 밤 24시까지를 국가애도기간으로 지정하고, 사고 발생지역인 서울시 용산구를 특별재난지역으로 선포했습니다." )
st.write("  이 참사는 모두에게 큰 트라우마를 남겼습니다. 아수라장 같던 곳을 겨우 살아난 생존자들에게, 한순간에 사랑하는 사람들을 잃은 유가족과 친구, 동료들에게, 그리고 그 상황을 지켜봤던 우리들에게요." )

data1 = [82.4,17.6]
data2 = [62.5,37.5]
data3 = [60.7,39.3]
labels=['그렇다','그렇지않다']

colors = sb.color_palette('pastel')
fig1 = plt.figure(figsize=(16,8))
plt.pie(data1, labels=labels, colors=colors, autopct='%.0f%%')
fig2 = plt.figure(figsize=(16,8))
plt.pie(data2, labels=labels, colors=colors, autopct='%.0f%%')
fig3 = plt.figure(figsize=(16,8))
plt.pie(data3, labels=labels, colors=colors, autopct='%.0f%%')

option = st.selectbox('이태원 참사가 미치는 영향에 대한 심각성 인식',
                     ('한국 사회 전체에 미치는 영향이 심각하다.', 
                     '나의 또래 집단에 미치는 영향이 심각하다.', 
                     '나에게 미치는 영향이 심각하다.'))	
if option=='한국 사회 전체에 미치는 영향이 심각하다.':
    st.pyplot(fig1)
elif option=='나의 또래 집단에 미치는 영향이 심각하다.':
    st.pyplot(fig2)
elif option=='나에게 미치는 영향이 심각하다.':
    st.pyplot(fig3)

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
fig0 = plt.figure(figsize=(16,8))
plt.pie(data, labels=labels, colors=colors, autopct='%.0f%%')
st.pyplot(fig0)

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
