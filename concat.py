import pandas as pd
import numpy as np
import collections
from collections import Counter

# 대여일시를 날짜/시로 분철하는 작업 1회만 실행

Dt='A:\TeamProject1\project_1\RentalData\Rental_Info_F.csv'


# Dt01='A:\TeamProject1\project_1\RentalData\Rental_Info_01.csv'
# Dt02='A:\TeamProject1\project_1\RentalData\Rental_Info_02.csv'
# Dt03='A:\TeamProject1\project_1\RentalData\Rental_Info_03.csv'
# Dt04='A:\TeamProject1\project_1\RentalData\Rental_Info_04.csv'
# Dt05='A:\TeamProject1\project_1\RentalData\Rental_Info_05.csv'
# Dt06='A:\TeamProject1\project_1\RentalData\Rental_Info_06.csv'
#
# DtF=pd.read_csv(Dt)
#
# Dt11=pd.read_csv(Dt01)
# Dt22=pd.read_csv(Dt02)
# Dt33=pd.read_csv(Dt03)
# Dt44=pd.read_csv(Dt04)
# Dt55=pd.read_csv(Dt05)
# Dt66=pd.read_csv(Dt06)

#날짜와 시간을 분리하여 새 컬럼에 저장.

# rental_date_split=Dtf['대여일시'].str.split(' ') # 공백을으로 날짜/시간이 분리되어있으니까 split으로 분리
# return_date_split=Dtf['반납일시'].str.split(' ')
# Dtf['대여날짜']=rental_date_split.str.get(0) #2022-01-01, 09:02:01 로나뉘어서  날짜는 0번째인덱스 시간은 1번째인덱스
# Dtf['대여시간']=rental_date_split.str.get(1)
# Dtf['반납날짜']=return_date_split.str.get(0)
# Dtf['반납시간']=return_date_split.str.get(1)
#
# Dtf=Dtf[['대여날짜','대여시간','출발대여소번호','출발대여소명','출발상세주소','반납날짜','반납시간','반납대여소번호','반납대여소명','반납상세주소']]

#object형 -> datetime으로 변경. 형변을 굳이 안해도 결과는 동일하여 일단 주석처리
# Dt01['대여날짜']=pd.to_datetime(Dt01['대여날짜']) #데이터타입을 변경할경우 기존df=pd.to_datetime | .apply(람다~)으로 덮어씌워줘야한다.
# Dt01['대여시간']=pd.to_datetime(Dt01['대여시간'])
# Dt01['반납날짜']=pd.to_datetime(Dt01['반납날짜'])
# Dt01['반납시간']=pd.to_datetime(Dt01['반납시간'])
#print(Dt01.info())

#print(DtF.info())#row 18121392
# print(Dt11.info())
# print(Dt22.info())
# print(Dt33.info())
# print(Dt44.info())
# print(Dt55.info())
# print(Dt66.info())