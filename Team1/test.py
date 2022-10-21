import pandas as pd
import csv
import requests as rqs
from bs4 import BeautifulSoup
from project_1 import DownCast

#개발목표1: 시간대별 가장 많이 반납된곳을 분석하여 어느용도로 사용하는지 파악
#개발목표2: 시간대별 많이 이용하는 성별과 연령대 분석. <<보류. 비교할 두 데이터 파일간에 데이터 갯수의차이가있음.제공의문제

# Key='5573566347736b7337356356636b66'
# url='http://openapi.seoul.go.kr:8088/'+Key+'/json/tbCycleRentData/100/480/2022-01-01/1'
#
# res=rqs.get(url)
# abc=pd.read_csv(url,encoding='utf-8',sep=',')
# print(abc)

#판다스이용
Bicycle_rental ='A:\TeamProject1\project_1\Team1\Seoul_Bicycle_rental_history_22_01.csv'
Rental_Office = 'A:\TeamProject1\project_1\Team1\Seoul_rental_office.csv'
Bicycle_rental_T='A:\TeamProject1\project_1\Team1\Seoul_Bicycle_rental_history_T_22_01.csv'

Br = pd.read_csv(Bicycle_rental,encoding = "ms949") #'ms949' 또는 'cp949' 또는 'ansi'
Ro = pd.read_csv(Rental_Office, encoding = "ms949")
Brt = pd.read_csv(Bicycle_rental_T, encoding='ms949')

r=Ro[['대여소번호','보관소(대여소)명','상세주소']].dropna(axis=0)



print(Br[['대여일시','대여 대여소명']])
