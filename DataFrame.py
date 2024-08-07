import numpy
import numpy as np
import pandas as pd

my_index = ['A', 'B', 'C']
my_columns = ['이름', '나이', '성별']
my_data = numpy.array([['Alice', 'Bob', 'Joon'],
                       [25, 30 , 28],
                       ['여', '여', '남']]).transpose()

df = pd.DataFrame(my_data, index=my_index, columns=my_columns)

#print(df, df.shape) # .shape이 객체가 가지고 있는 속성 정보, 몇 행열인지 표기
#print(df[['나이', '이름']]) #원하는 key값 호출
print(df, "\n", df.loc["A"]) # 코드는 DataFrame 전체를 출력한 후 빈 줄을 넣고, 그 다음에 "A" 행의 데이터를 출력