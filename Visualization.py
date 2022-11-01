# 시각화 도넛차트

import collections
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



Dt='A:\TeamProject1\project_1\RentalData\Rental_Info_F.csv'
Dt01=pd.read_csv(Dt)

#어디서 가장많이빌렸는지?(아침-밤 전체) :
# 1 마곡나루역 2번출구
# 2 뚝섬유원지역 1번출구앞
# 3 여의나루역 1번출구앞
# 4 마곡나루역 5번출구 뒤편

#어디서 가장 반납을 많이했는지?( 동일 )
#1:뚝섬유원지역 1번출구앞
#2:한강공원 망원나들목
#3:마곡나루역 5번출구 뒤편
#4:여의나루역 1번출구 앞

#=주로 출퇴근용으로 많이이용

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

#---------------------------시각화 코드(공통)----------------------------------------------

plt.rcParams['figure.figsize']= [12, 8] #피규어사이즈 지정/
#폰트 설정

plt.rc('font', family='NanumGothic')
mpl.rcParams['axes.unicode_minus'] = False

#각 값설정 outRing
Group_name=['아침','점심','저녁','밤']
Gorup_value=[Morning_count,Day_count,Evening_count,Night_count] #점심은 시간이 혼자두배라서 /2


#-----------------------------대여(출발)데이터 출력---------------------------------------------

#inside ring 설정
Sub_name=[Morning_s_1D[0],Morning_s_1D[2],Morning_s_1D[4],Morning_s_1D[6],
          Day_s_1D[0],Day_s_1D[2],Day_s_1D[4],Day_s_1D[6],
          Evening_s_1D[0],Evening_s_1D[2],Evening_s_1D[4],Evening_s_1D[6],
          Night_s_1D[0],Night_s_1D[2],Night_s_1D[4],Night_s_1D[6]]

Sub_value=[Morning_s_1D[1],Morning_s_1D[3],Morning_s_1D[5],Morning_s_1D[7],
           Day_s_1D[1],Day_s_1D[3],Day_s_1D[5],Day_s_1D[7],
           Evening_s_1D[1],Evening_s_1D[3],Evening_s_1D[5],Evening_s_1D[7],
           Night_s_1D[1],Night_s_1D[3],Night_s_1D[5],Night_s_1D[7]]

#도넛형으로 만들기위한 아웃 링 레드:아침 그린:점심 블루:저녁 아이보리:밤
#다른방법으론 wedgeprops= 딕셔너리를 넣어서 다양한 디테일 변경
#width 파이 가운데 뚫기 plt.pie(값,wedgeprops=width값을넣은 변수)
#edgecolor 테두리선 색깔
#linewidth 테두리선 두께
width_num = 0.4 #값이높을수록 중앙의원이작아짐

a,b,c,d = [plt.cm.Reds,plt.cm.Greens,plt.cm.Blues,plt.cm.pink] #색 기본값을 기정하고 아래 colors에서 알파값지정같음
fig, ax = plt.subplots()
ax.axis('equal')
grouplabelprop = dict(size=15, weight='bold',color='white',va='center')
sublabelprop = dict(size=10)

#radius:원의크기,labledistance=라벨간 거리 값이 클수록 원밖으로나감 pctdistance:퍼센트의 위치
pie_outside, _ = ax.pie(Gorup_value,radius=1.2, labels=Group_name,labeldistance=0.8,colors=[a(0.7),b(0.7),c(0.7),d(0.7)],
                        textprops=grouplabelprop)

plt.setp(pie_outside,width=width_num,edgecolor='white')

#실질적으로 값이들어가는 부분
pie_insid,plt_labels,junk = \
     ax.pie(Sub_value,radius=(1.2-width_num),autopct='%1.1f%%',
            colors=[a(0.6),a(0.5),a(0.4),a(0.3),b(0.6),b(0.5),b(0.4),b(0.3),c(0.6),c(0.5),c(0.4),c(0.3),d(0.6),d(0.5),d(0.4),d(0.3)],
            pctdistance=0.8,textprops=sublabelprop)

plt.setp(pie_insid, width=width_num, edgecolor='white')

plt.title('시간별 이용현황(대여)',fontsize=30,pad=30)
plt.xlabel('기간:2022-01~2022-06',loc='center')
#다중범례를 적용하기위해 각 개별 아티스트로 등록
legend1=plt.legend([Group_name[0]+' : 6:00~9:30',Group_name[1]+' : 10:00~16:30',Group_name[2]+' : 17:00~19:30', Group_name[3]+' : 20:30~21:30'],ncol=2,
                   frameon=False,bbox_to_anchor=(0.7,0.95))
art_leng1=plt.gca().add_artist(legend1)
#--------------------sub데이터 라벨 밖으로 꺼내기----------------------------
bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)

kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=1, va="center") #z order=겹치기속성

for i, p in enumerate(pie_insid):
    ang = (p.theta2 - p.theta1)/2. + p.theta1 #안쪽파이의 각
    y = 0.75*np.sin(np.deg2rad(ang)) #화살표의 끝위치의 y좌표 최적 0.7-0.8 값이커질수록 선이짧아진다.
    x = 0.75*np.cos(np.deg2rad(ang)) #화살표 끝위치의x좌표 최적0.7-0.8
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(Sub_name[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),#x,y텍스트의 위치
                horizontalalignment=horizontalalignment, **kw)
plt.show()

'''
#------------------------------------도착데이터 그래프-----------------------------------------


Sub_name=[Morning_r_1D[0],Morning_r_1D[2],Morning_r_1D[4],Morning_r_1D[6],
          Day_r_1D[0],Day_r_1D[2],Day_r_1D[4],Day_r_1D[6],
          Evening_r_1D[0],Evening_r_1D[2],Evening_r_1D[4],Evening_r_1D[6],
          Night_r_1D[0],Night_r_1D[2],Night_r_1D[4],Night_r_1D[6]]

Sub_value=[Morning_r_1D[1],Morning_r_1D[3],Morning_r_1D[5],Morning_r_1D[7],
           Day_r_1D[1],Day_r_1D[3],Day_r_1D[5],Day_r_1D[7],
           Evening_r_1D[1],Evening_r_1D[3],Evening_r_1D[5],Evening_r_1D[7],
           Night_r_1D[1],Night_r_1D[3],Night_r_1D[5],Night_r_1D[7]]

width_num = 0.4
a,b,c,d = [plt.cm.Reds,plt.cm.Greens,plt.cm.Blues,plt.cm.pink]
fig, ax = plt.subplots()
ax.axis=('equal')
grouplabelprop = dict(size=15, weight='bold',color='white',va='center')
sublabelprop = dict(size=10)

pie_outside, _ = ax.pie(Gorup_value,radius=1.2, labels=Group_name,labeldistance=0.8,colors=[a(0.7),b(0.7),c(0.7),d(0.7)],
                        textprops=grouplabelprop)

plt.setp(pie_outside,width=width_num,edgecolor='white')


pie_insid,plt_labels,junk = \
     ax.pie(Sub_value,radius=(1.2-width_num),autopct='%1.1f%%',
            colors=[a(0.6),a(0.5),a(0.4),a(0.3),b(0.6),b(0.5),b(0.4),b(0.3),c(0.6),c(0.5),c(0.4),c(0.3),d(0.6),d(0.5),d(0.4),d(0.3)],
            pctdistance=0.8,textprops=sublabelprop)

plt.setp(pie_insid, width=width_num, edgecolor='white')

plt.title('시간별 이용현황(도착)',fontsize=30,pad=30)
plt.xlabel('기간:2022-01~2022-06',loc='center')


legend1=plt.legend([Group_name[0]+' : 6:00~9:30',Group_name[1]+' : 10:00~16:30',Group_name[2]+' : 17:00~19:30', Group_name[3]+' : 20:30~21:30'],
                   ncol=2,frameon = False,bbox_to_anchor=(0.7,0.95))
art_leng1=plt.gca().add_artist(legend1)
#--------------------sub내용의 라벨들을 밖으로 꺼내오는작업 부분---------------------------------------
bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)

kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=1, va="center") #z order=겹치기속성

for i, p in enumerate(pie_insid):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = 0.75*np.sin(np.deg2rad(ang))
    x = 0.75*np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(Sub_name[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, **kw)

plt.show()

'''

