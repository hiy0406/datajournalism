import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import seaborn as sb
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import altair as alt

font_fname = './NanumGothic.ttf'
font_name = fm.FontProperties(fname=font_fname).get_name()
matplotlib.rc('font', family=font_name)

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
st.write("  이 참사는 모두에게 큰 트라우마를 남겼습니다. 아수라장 같던 곳을 겨우 살아난 생존자들에게, 한순간에 사랑하는 사람들을 잃은 유가족과 친구, 동료들에게, 그리고 그 상황을 지켜봤던 우리들에게요. 한 달이 더 지난 지금, 여전히 우리는 그날을 또렷하게 기억하고 있습니다." )

st.markdown("### 이태원 참사가 미치는 영향에 대한 심각성 인식")
option = st.selectbox(' ',
                     ('한국 사회 전체에 미치는 영향이 심각하다.', 
                     '나의 또래 집단에 미치는 영향이 심각하다.', 
                     '나에게 미치는 영향이 심각하다.'))	
if option=='한국 사회 전체에 미치는 영향이 심각하다.':
    img=Image.open("./poll1.png")
    st.image(img)
elif option=='나의 또래 집단에 미치는 영향이 심각하다.':
    img=Image.open("./poll2.png")
    st.image(img)
elif option=='나에게 미치는 영향이 심각하다.':
    img=Image.open("./poll3.png")
    st.image(img)

st.markdown("---")

#이태원 검색량
st.markdown("## 이태원, 생각만 해도 무서워요")
st.write("사고 이후 유가족과 현장에 있었던 사람들 외, 사고 소식을 접한 국민 전체의 트라우마 문제가 대두되었습니다. 일상적 장소인 서울 한복판에서 일반 시민들, 특히 20대 청년들이 대규모로 사망했다는 사실 자체가 주는 불안감과 공포, SNS를 통해 퍼진 참사 현장의 무분별한 확산으로 인해 정신적 고통을 소호하는 사람들이 증가했기 떄문이죠. 정부를 포함한 여러 센터에서는 피해자들을 위한 심리 상담을 제공하여 이를 해결하려고 노력했습니다.")
st.write("심리치료를 받아야 할 정도로 심각한 트라우마가 생긴 사람들 외에도, 사람들의 일상에는 조금씩 변화가 시작되었습니다. 놀이공원, 공연장 등 사람들이 많이 모이는 장소는 물론, 익숙했던 출퇴근길이 언제든 사고가 날 수 있는 ‘위험한 공간’으로 여겨지기 시작했습니다.  지하철이나 버스 등의 일상적인 공간도 불편해지게 된 것이죠. ")
st.write("아래 데이터는 네이버 검색엔진을 통해 분석한 ‘이태원' 관련 검색수입니다. 저기 확 떨어진 지점 보이시나요? 이태원 참사가 발생했던 직후 네이버 검색량은 현저하게 감소하고 있는 것을 확인할 수 있었습니다.")

searchdata=pd.read_csv("./2017searching.csv")
from datetime import datetime
searchdata.date = searchdata.date.apply(lambda d: datetime.strptime(d, "%Y-%m-%d"))
searchdata.index = searchdata.date
searchdata = searchdata.drop(["date"], axis=1)
searchdata.head()
st.line_chart(searchdata)

st.write(" 실제로 서울시가 제공하는 데이터에 따르면, 이태원 1동 유동인구가 참사 이전(10월 넷째주) 대비 11월 2주까지 30.5% 감소했으며, 매출 또한 61.7% 감소했다고 합니다. 사람들의 트라우마가 이태원으로 향하는 즐거운 발걸음들을 끊은 것이지요.")
          

