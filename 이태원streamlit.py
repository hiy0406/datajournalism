import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import seaborn as sb
import matplotlib
import matplotlib.pyplot as plt

# Webpage Title
st.title("10.29(2022) 참사, 남겨진 상인들")
st.caption("사람들의 발길이 끊긴 그곳에는 오늘도 가게 문을 여는 상인들이 있습니다.")
st.markdown("---")

st.write("  기사를 시작하기에 앞서, 10.29(2022) 참사로 사망한 분들의 명복을 빕니다." )
st.write("  2022년 10월 29일, 이태원에서 비극적인 압사 참사가 일어났습니다. 핼로윈을 이틀 남긴 10월의 토요일, 코로나 19 확산세가 어느 정도 감소하여 약 3년 만에 사회적 거리두기 없이 핼러윈 축제를 즐기기 위해 수많은 인구가 이태원으로 몰렸습니다. 즐거움으로 가득해야만 했던 거리, 하지만 오후 10시 15분 경 도시는 순식간에 비명소리와 사이렌 소리도 뒤덮혀 버렸습니다. 폭이 채 5m가 되지 않는 해밀턴호텔 옆 골목에서 대규모 압사가 시작되었기 때문이죠. 이 끔찍한 사고로 인해 158명이 사망했고, 197명이 부상을 당하는 등 300명이 넘는 사상자가 발생하였습니다." )
st.write("  서울에 거주하고 있는 2030 청년들은 이날 수많은 연락들을 받으셨을 거예요. 가족들은 물론 주변 지인들 모두 급하게 연락을 돌려 서로의 안부를 확인하고 가슴을 쓸어내렸다고 합니다. 실제로 국내 이동통신 3사에 따르면, 참사 발생한 직후부터 다음날까지 전국적으로 유의미한 트래픽 증가가 있었다고 해요.  사람들은 한 명씩 늘어나는 부상자와 사망자 수를 보며 엄청난 공포감에 휩싸였습니다. 서울 도심에서 이러한 대규모 인명피해가 발생한 것은 1995년 삼풍백화점 이후로 처음이었기 때문이었어요. 정부는 참사 이후 10월 30일부터 11월 5일 밤 24시까지를 국가애도기간으로 지정하고, 사고 발생지역인 서울시 용산구를 특별재난지역으로 선포했습니다." )
st.write("  이 참사는 모두에게 큰 트라우마를 남겼습니다. 아수라장 같던 곳을 겨우 살아난 생존자들에게, 한순간에 사랑하는 사람들을 잃은 유가족과 친구, 동료들에게, 그리고 그 상황을 지켜봤던 우리들에게요. 한 달이 더 지난 지금, 여전히 우리는 그날을 또렷하게 기억하고 있습니다." )


st.header("10.29 참사가 미치는 영향에 대한 심각성 인식")
img=Image.open("./poll.png")
st.image(img, caption="*한국언론진흥재단 미디어연구센터 온라인 설문조사(2022년 11월 25일~30일, N=1000")
st.markdown("---")

#이태원 검색량
st.header('"이태원, 생각만 해도 무서워요"')
st.write("사고 이후 유가족과 현장에 있었던 사람들 외, 사고 소식을 접한 국민 전체의 트라우마 문제가 대두되었습니다. 일상적 장소인 서울 한복판에서 일반 시민들, 특히 20대 청년들이 대규모로 사망했다는 사실 자체가 주는 불안감과 공포, SNS를 통해 퍼진 참사 현장의 무분별한 확산으로 인해 정신적 고통을 소호하는 사람들이 증가했기 떄문이죠. 정부를 포함한 여러 센터에서는 피해자들을 위한 심리 상담을 제공하여 이를 해결하려고 노력했습니다.")
st.write("심리치료를 받아야 할 정도로 심각한 트라우마가 생긴 사람들 외에도, 사람들의 일상에는 조금씩 변화가 시작되었습니다. 놀이공원, 공연장 등 사람들이 많이 모이는 장소는 물론, 익숙했던 출퇴근길이 언제든 사고가 날 수 있는 ‘위험한 공간’으로 여겨지기 시작했습니다.  지하철이나 버스 등의 일상적인 공간도 불편해지게 된 것이죠. ")
st.write("아래 데이터는 네이버 검색엔진을 통해 분석한 ‘이태원' 관련 검색수입니다. 저기 확 떨어진 지점 보이시나요? 이태원 참사가 발생했던 직후 네이버 검색량은 현저하게 감소하고 있는 것을 확인할 수 있었습니다.")

st.subheader("'이태원' 키워드 관련 검색량 추이")
st.info("*검색어: 이태원맛집, 이태원음식점, 이태원식당, 이태원밥, 이태원카페")
@st.cache
def load_data():
  data = pd.read_csv("./2017searching.csv")
  from datetime import datetime
  data.date = data.date.apply(lambda d: datetime.strptime(d, "%Y-%m-%d"))
  data.index = data.date
  data = data.drop(["date"], axis=1)
  return data

searchdata = load_data()
st.line_chart(searchdata)

st.write(" 실제로 서울시가 제공하는 데이터에 따르면, 이태원 1동 유동인구가 참사 이전(10월 넷째주) 대비 11월 2주까지 30.5% 감소했으며, 매출 또한 61.7% 감소했다고 합니다. 사람들의 트라우마가 이태원으로 향하는 즐거운 발걸음들을 끊은 것이지요.")
st.markdown("---")

#상권매출액 공간적 변화
st.header("다시 희망을 잃어버린 이태원")
st.write("사실 이태원은 ‘희망이 보이기 시작하는’ 동네였습니다. 외국인 관광객들과 각종 이벤트를 중심으로 매출이 만들어지던 지역의 특성상 코로나19 확산으로 인해 가장 심각한 피해를 입었기 때문이었죠. 지난 2년간 이태원의 피해는 어떠했는지 잠깐 살펴볼까요? ")
st.subheader("코로나19 전후 이태원 상권의 공간적 변화")
option = st.selectbox('', ['2018-2019 유동인구 변화율',
                      '2019-2020 유동인구 변화율',
                      '2018-2019 매출액 변화율',
                      '2019-2020 매출액 변화율'])

if option=='2018-2019 유동인구 변화율':
    img=Image.open("./18-19pop.png")
    st.image(img)
elif option=='2019-2020 유동인구 변화율':
    img=Image.open("./19-20pop.png")
    st.image(img)
elif option=='2018-2019 매출액 변화율':
    img=Image.open("./18-19sale.png")
    st.image(img)
elif option=='2019-2020 매출액 변화율':
    img=Image.open("./19-20sale.png")
    st.image(img)
st.caption("권도율 and 전재식. (2022). 코로나19 전후 서울 상권 매출의 공간적 변화. 부동산학연구, 28(3), 25-44.")

st.subheader("이태원 1동 유입인구 변화")
img=Image.open("./inflow_pop.png")
st.image(img)
st.write("데이터를 통해 살펴보도록 하죠. 위쪽 데이터는 서울시에서 제공하고 있는 생활 유동 인구를 시각화한 데이터입니다. 맛집, 카페, 클럽 등의 주요 시설이 모여있으며 사고의 중심지인 해밀톤 호텔이 있는 이태원 1동을 주로 살펴보았습니다.  먼저 왼쪽 그래프를 보실까요? 코로나19 확산으로 계속해서 낮은 유입인구수를 지속하였으나, 단계적 일상 회복 방안이 실시되었던 2022년 5월을 기점으로 유입인구수가 대폭 상승하여 이전의 기세를 회복하는 듯 합니다. 그러나 오른쪽의 그래프를 통해 확인할 수 있듯, 10.29 참사를 기점으로 다시 급락하게 되었습니다. 앞에서 살펴본 네이버 검색량 그래프와도 일치하는 데이터라고 할 수 있습니다. 거칠게 몰아쳤던 코로나19 상황 속에서도 언젠가는 매출을 회복할 수 있을 것이라는 상인들의 기대가 무참히 깨지게 된 것이죠. 이태원의 특성상 핼러윈, 크리스마스 등 주요 행사가 몰려있는 10~12월의 매출로 1~3월의 매출을 매꿔왔기에 이번 참사는 그들에게 더 크게 다가왔습니다.")
st.write("이태원에서 잡화점을 운영하는 A씨는 “코로나 19 확산세가 줄어들며 손님들이 한 두 명씩 오기 시작하는 게 체감돼 희망을 봤었다”며 “우리 얘기를 하는 게 염치가 없지만 (10.29 참사로) 상권이 다시 죽은 게 염려스럽다”고 답했습니다. 겨우 희망을 찾은 이태원 상권, 다시 무너지기 시작했습니다.")
st.markdown("---")

#소상공인 지원
st.header("이태원 소상공인 지원책 살펴보기")
st.write("절망적인 상황 속에서 서울시가 나서기 시작했습니다. 서울시가 지난달 24일 발표한 ‘이태원 소상공인 긴급 지원 방안’에는 100억 원 규모의 ‘이태원 상권 회복 자금’ 공급과 70억 원 규모의 지역 상품권 사업비 지원 내용이 담겼습니다. 이태원 상권 회복자금은 이태원 1, 2동에서 매장형 업체를 운영 중인 2409개의 소상공인 및 중소기업 중 유흥업, 도박 등의 융자 지원 제한 업종에 해당되지 않는 업종을 운영 중인 업체를 대상으로 해요. 업체 당 최대 3000만 원을 연 2.0%의 저리로 공급하며, 1년 거치 4년 균등 분할 상환 조건을 건 융자 지원책입니다.")
st.write("그러나 이러한 서울시의 융자 지원책의 실효성에 대해서는 의문을 제기하는 목소리가 높아지고 있다고 해요. 참사가 있었던 골목 건너편 ‘퀴논길’에서 카페를 운영하고 있는 자영업자 A씨는 “요즘 같은 고금리 상황에서의 저리 대출은 이점이 있을 수도 있겠지만, 결국은 갚아야 할 빚”이라며 “대출은 임시 방편에 불과하다”라고 답했습니다.")
st.write("그렇다면 서울시는 왜 이태원 소상공인에 대한 직접 지원을 하지 않고 있는 걸까요? 이태원 소상공인 직접 지원에 대한 법적 근거가 확립되지 않았다는 점이 그 이유입니다. 기존 소상공인법은 지원대상과 근거가 명확하게 명시되어 있지 않고, 재난 및 코로나 19 관련 피해 지원에 대한 법적 근거는 있지만, ‘피해’의 의미가 모호해 결국 현행법으로는 이태원 소상공인에 대한 직접 지원이 어려운 상황입니다.")
st.write("지난 달 28일, 중소벤처기업부에서도 용산구를 특별 재난 지역으로 선포함에 따라 소상공인 특별 지원 방안을 확정했으나, 그 내용은 융자 규모를 업체당 7000만 원으로 확대하고 금리를 1.5%로 추가 인하하는 것으로, 이는 결국 서울시 융자 지원책의 연장선에 불과합니다. 결국 이태원 상인들이 필요로 하는 지원금, 보조금 형태의 지원은 이루어지고 있지 않습니다.")
st.write("서울시는 해당 법안의 신속한 처리를 요구하고 있지만, 법안 통과 후 직접 지원 대책이 마련되기까지 얼마의 시간이 걸릴지 알 수 없기에, 이태원 상인들은 오늘도 가게 문을 연채로 기다릴 뿐입니다.")

