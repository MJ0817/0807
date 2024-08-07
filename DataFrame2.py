#Data를 활용한 연습문제
#먼저 디렉토리 폴더안에 새폴더 생성 후 분석하고자 하는 데이터 넣기
#생성할 파이썬 프로젝트는 새로 생성한 폴더 밖의 폴더에 생성
#피마 인디언의 당뇨 데이터 셋


import pandas as pd
col_names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv',
                   names=col_names)

# print(data['preg']) 객체의 임신 횟수값만 출력
# print(data.head(5)) 상위 5명만
# print(data. describe()) 데이터셋 요약해주는 함수

import pandas as pd
import matplotlib.pyplot as plt

col_names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv',
                   names=col_names)
plt.clf()
plt.hist(data['preg'])
plt.show()
plt.savefig("/.age.")


import pandas as pd
import matplotlib.pyplot as plt

col_names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv',
                   names=col_names)
data.describe().to_csv('./results/describe.csv') #results라는 폴더 생성후 .csv파일생성