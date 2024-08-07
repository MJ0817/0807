# Heatmap - 2차원 데이터를 시각화할 때 사용하며, 데이터의 밀도와 패턴을 파악하는데 사용

import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10, 10)

plt.clf()
heatmap = plt.imshow(data, cmap="YlGnBu", aspect='auto')
#cmap은 "컬러 맵" 또는 색상 맵을 지정하는 매개변수
#YlGnBu"는 'Yellow-Green-Blue'의 약자
#aspect는 그래프의 가로세로 비율을 조정하는 매개변수
# aspect='auto' 는 이미지의 가로세로 비율을 자동으로 조정하여 데이터가 화면에 맞게 잘려지지 않고 최적화
plt.colorbar(heatmap)
plt.title("Heatmap Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.savefig("./heatmap.png")
plt.show()