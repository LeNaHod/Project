import collections
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter

Dt='A:\TeamProject1\project_1\RentalData\Rental_Info_F.csv'
Dt01=pd.read_csv(Dt)


#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)

#--------가장 많이반납한 지역 --------------
#groupby=말그대로 그룹화시킴.
#방법1.카운트로 가장많이나온 값을 매겨서 rnak로 순위정리하기
#방법2.최빈값을구하고,가장많이나온 값을 하나씩 추가해서 제외해서 다음으로 작은값을 구하는법



#---------------------------------------시간별로 데이터 필터링--------------------------
Morning=Dt01[(Dt01['대여시간'].between('06:00:00','09:29:59')) & (Dt01['반납시간'].between('06:00:00','09:59:59'))]
Day=Dt01[(Dt01['대여시간'].between('10:00:00','16:29:59')) & (Dt01['반납시간'].between('10:00:00','16:59:59'))]
Evening=Dt01[(Dt01['대여시간'].between('17:00:00','19:29:59')) & (Dt01['반납시간'].between('17:00:00','20:29:59'))]
Night=Dt01[(Dt01['대여시간'].between('20:30:00','23:29:59')) & (Dt01['반납시간'].between('20:30:00','23:59:59'))]

Morning_count=Morning['대여시간'].count() #모든 컬럼의 갯수가같으므로 하나만출력.
Day_count=Day['대여시간'].count()
Evening_count=Evening['대여시간'].count()
Night_count=Night['대여시간'].count()

# print(test1.info())#214237

#지정 컬럼에서 값별로 몇번씩 많이나왔는지.(어느데이터가 가장많이나왔는지 갯수별로확인) 최빈값은 하나만출력(.mode)

#print(test1[['출발대여소번호','출발대여소명','출발상세주소']].mode())

#Counter:찾으려는곳에서 어떤값이 얼만큼있는지
#print(Counter(Morning['출발대여소명']))

#시간별로 구한데이터에서 대여소 정보를 Counter로 최빈값구하기. most_common(출력할갯수). 단 list로반환.

#아침
Morning_start=collections.Counter(Morning['출발대여소명']).most_common(4) #출발을 어디서 가장많이했는지
Morning_s_df=pd.DataFrame(Morning_start)
Morning_s_1D=np.ravel(Morning_s_df)

Morning_return=collections.Counter(Morning['반납대여소명']).most_common(4) #반납을 어디에 가장많이했는지
Morning_r_df=pd.DataFrame(Morning_return)
Morning_r_1D=np.ravel(Morning_r_df)


# #점심
Day_start=collections.Counter(Day['출발대여소명']).most_common(4) #출발을 어디서 가장많이했는지
Day_s_df=pd.DataFrame(Day_start)
Day_s_1D=np.ravel(Day_s_df)

Day_return=collections.Counter(Day['반납대여소명']).most_common(4) #반납을 어디에 가장많이했는지
Day_r_df=pd.DataFrame(Day_return)
Day_r_1D=np.ravel(Day_r_df)

#저녁
Evening_start=collections.Counter(Evening['출발대여소명']).most_common(4) #출발을 어디서 가장많이했는지
Evening_s_df=pd.DataFrame(Evening_start)
Evening_s_1D=np.ravel(Evening_s_df)

Evening_return=collections.Counter(Evening['반납대여소명']).most_common(4) #반납을 어디에 가장많이했는지
Evening_r_df=pd.DataFrame(Evening_return)
Evening_r_1D=np.ravel(Evening_r_df)

#밤
Night_start=collections.Counter(Night['출발대여소명']).most_common(4) #출발을 어디서 가장많이했는지
Night_s_df=pd.DataFrame(Night_start)
Night_s_1D=np.ravel(Night_s_df)

Night_return=collections.Counter(Night['반납대여소명']).most_common(4) #반납을 어디에 가장많이했는지
Night_r_df=pd.DataFrame(Night_return)
Night_r_1D=np.ravel(Night_r_df)
