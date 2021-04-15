'''
    작성자 : 서울1반 4팀 황윤호
    내용 : 유저 추천 알고리즘
    생성일자 : 2021-04-01
    최종수정일자 : 2021-04-01
'''

'''
xgboost 기본 예제
'''
# from pandas import DataFrame


# # df = Times Series data
# df = DataFrame()
# df['t'] = [x for x in range(10)]

# # Times Series data => Supervised Learning Problem 형태로 바꾸기
# df['t-1'] = df['t'].shift(1)
# print(df)

'''
#하루의 데이터를 입력으로 다음날 하루의 값을 예측하는 코드
'''
# from pandas import DataFrame
# from pandas import concat

# days_in = 1
# days_out = 1

# df = DataFrame(x for x in range(10))
# raw = []

# for i in range(days_in, 0, -1):
#     raw.append(df.shift(i))

# for i in range(0, days_out):
#     raw.append(df.shift(-i))

# sum = concat(raw, axis = 1)

# sum.dropna(inplace = True)

# print(sum)

'''
주식 예측
'''
from pandas import DataFrame
from pandas import concat
from xgboost import XGBRegressor
from pandas_datareader import data as pdr
import numpy as np

# 30일 데이터로 다음날 하루 예측
days_in = 30
day_out = 1

# 주식
event = pdr.get_data_yahoo('055550.KS')
# print(event)

# 종가
event_close = event["Close"]

# 종가의 값만 받음
values = event_close.values

# Times Series data => Supervised Learning Problem 형태로 바꾸기
df = DataFrame(values)
# print(df)
raw = []

for i in range(days_in, 0, -1):
    raw.append(df.shift(i))
for i in range(0, day_out):
    raw.append(df.shift(-i))

sum = concat(raw, axis=1)

sum.dropna(inplace=True)

# Supervised Learning 데이터로 변형된 데이터는 train에 저장
train = sum.values
print(type(train))
print(train)
# print(np.fromstring(train))

# 모델 훈련 및 예측
trainX, trainy = train[:, :-1], train[:, -1]

# days_in, n_estimators 값에 따라 예측 값이 달라진다.
model = XGBRegressor(objective='reg:squarederror', n_estimators=80)
model.fit(trainX, trainy)

data_in = values[-days_in:]

result = model.predict(np.array([data_in]))

print(result)

print('Input: %s, Predicted: %.3f' % (data_in, result[0]))