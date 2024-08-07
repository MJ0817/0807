import numpy  ### Data Preparation(데이터 전처리) - 컴퓨터가 인식할 수 있게 변환하는 과정. ###

# WHY?
# * 데이터 정제 - 결측치, 이상치 및 오류 데이터 처리를 통한 신뢰성 향상
# * 데이터 변환 - 데이터를 적절한 형식으로 변환 ex) 스케일링, 정규화, 로그화
# * 데이터 통합 - 여러 데이터를 일관된 데이터 세트로 생성 ex) 데이터베이스 통합
# * 데이터 축소 - 불필요한 데이터 삭제
# * 데이터 인코딩 - 데이터를 모델 또는 다른 기기에서 사용할 수 있는 형태로 변환(male:0, female:1)
# * 데이터 시각화 - 그래프 형태로 나타냄


               # 데이터 정규화 및 스케일링 #
# - 데이터 값의 범위를 조절하여 모든 특성이 동일한 척도로 변환
# - 일반적으로 데이터를 0과 1사이의 값으로 조정



#Pandas - 데이터 전처리 및 분석을 위한 파이썬 라이브러리

#(1) series - 1차원 데이터에 레이블이 붙은 배열 데이터 구조, Dataframe의 열은 하나의 series로 구성
# series 데이터를 구성하기 위해서는 1차원 배열 데이터가 필요
# series는 Numpy와 호환



import pandas as pd
import numpy as np

my_index = np.array([1, 2, 3]) #1, 2, 3리스트를 numpy 배열로 변환
data = ['김민준', '이관훈', '김우진']

series = pd.Series(data, index=my_index)
print(series)

data_2 = [10, 20, 30, 40, 50]
series_2 = pd.Series(data_2)
print(series_2)




import pandas as pd
data = pd.Series([10, 20, 30, 40, 50], index = ["A", "B", "C", "D", "E"])
data["B"] =60  #인덱스 "B"의 값을 60으로 변경
print(data,'\n', data["B"])

#DataFrame
# - 행과 열로 구성된 2차원 이상의 테이블 형식의 데이터 구조
# - 데이터 프레임을 통해 데이터를 구조화 및 관리 기능
# - CSV, 엑셀, 데이터베이스, 웹 스크래핑 등 다양한 데이터를 가져와 데이터 프레임으로 변환이 가능


import pandas as pd
data = {
    '이름': ['Alice', 'Bob', 'Joon'],
    '나이': [25, 30, 38],
    '성별': ['여', '여', '남']
}
df = pd.DataFrame(data, index=['A','B','C'])
print(df)
df.to_csv("./data.csv") #excel파일로 저장하는 코드