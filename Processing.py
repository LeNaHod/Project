import pandas as pd
import csv

#판다스를 이용하여 파일불러오기
Bicycle_rental ='A:\TeamProject1\project_1\Team1\Seoul_Bicycle_rental_history_22_06.csv'
Rental_Office = 'A:\TeamProject1\project_1\Team1\Seoul_rental_office.csv'

#'ms949' 또는 'cp949' 또는 'ansi'/메모장에서 uft-8로 인코딩시 정상 사용가능.
Br = pd.read_csv(Bicycle_rental,encoding = "utf-8")
Ro = pd.read_csv(Rental_Office, encoding = "ms949") 

#... 으로 생략되어있는거 해제.
#pd.set_option('display.max_rows',None)
#pd.set_option('display.max_columns', None)

#원본데이터에서 필요한 컬럼만 추출
#Br_F,Ro_F는 센터자료는 제외. file1.to_csv('파일이름',index=False):인덱스없이 csv파일로 저장/파일명.style.hide_index():인덱스 숨기기

Br_F=Br[['대여일시','대여소번호','반납일시','반납대여소번호']]#.set_index('대여소번호',inplace=False)
Ro_F=Ro[['대여소번호','보관소(대여소)명','상세주소']] #dropna(axis=0)결측제거 0:행, 1:열

#아래부분부터는 병합하여 csv생성부분

Rentalinfo_Merage=pd.merge(Br_F,Ro_F,how='left', on='대여소번호')

Rentalinfo_sort=Rentalinfo_Merage[['대여일시','대여소번호','보관소(대여소)명','상세주소','반납일시','반납대여소번호']]

Rentalinfo_rename=Rentalinfo_sort.rename(columns={'대여소번호':'출발대여소번호','보관소(대여소)명':'출발대여소명','상세주소':'출발상세주소','반납대여소번호':'대여소번호'})

Returninfo_Merge=pd.merge(Rentalinfo_rename,Ro_F,how='left',on='대여소번호')

Returninfo_rename=Returninfo_Merge.rename(columns={'대여소번호':'반납대여소번호','보관소(대여소)명':'반납대여소명','상세주소':'반납상세주소'})

#test3.info() #컬럼별 NaN값 갯수 확인
#test4=test3[test3['출발대여소명'].isnull()]#결측값조회 Row:7617

#결측제거. 제거전: Row 1414312/ 제거후: Row 1406695
Total_Info=Returninfo_rename.dropna(subset=['출발대여소명','반납대여소명'],axis=0)

#대여소 마스터정보에없는데이터 삭제후 csv파일 생성
#Total_Info.to_csv('Rental_Info_06.csv', index=False,encoding='utf-8')


print(Br_F) #5855 / 1414312
#print(Total_Info) #전:3972483  후:3927404
#print(Total_Info.info())

