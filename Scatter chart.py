# 산점도 실습

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

x = [random. uniform(0, 100) for _ in range(1000)]
y = [random. uniform(0, 100) for _ in range(1000)]


plt.scatter(x, y)


print(x, "\n", y)
plt.clf()
plt.scatter(x, y, label='Random Data Points', color='green', marker="s", s=30, alpha=0.5)
#marker='원하는 모양으로' *별모양 o원모양
plt.title('Scatter plot Example')
plt.xlabel("x-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.savefig("./scatter.png")
plt.show()


#발표시 어떤 데이터를 사용하였고 왜 사용했고 어떠한 유의미한 결과가 있었는지, 어떤게 기대되는지
#
# plt.savefig("./results/ scatter.png")
#
# #results = 저장위치
# plt.savefig("./ scatter.png")
# 파일을 scatter라는 파일로 저장하겠다
#marker='원하는 모양으로' *별모양 o원모양
# 원형: 'o'
# 삼각형 위쪽: '^'
# 삼각형 아래쪽: 'v'
# 삼각형 왼쪽: '<'
# 삼각형 오른쪽: '>'
# 사각형: 's'
# 다이아몬드: 'D'
# 플러스 기호: '+'
# 곱하기 기호: 'x'
# 원형 안에 점: '.'
# 별: '*'
# 빈 원: 'o' (점이 비어있음)
# 빈 사각형: 's' (점이 비어있음)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

x = [random. uniform(0, 100) for _ in range(200)]
y = [2 * val + 1 + random. uniform(-10, 10) for val in x]

x_line = range(101)
y_line = [2 * val + 1 for val in x_line]

plt.clf()
plt.scatter(x, y, label='Random Data Points', color='green', marker="x", s=30, alpha=0.5)
plt.plot(x_line, y_line, label='y = 2x +1', color='red')

plt.title('Scatter plot Example')
plt.xlabel("x-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.savefig("./scatter.png")
plt.show()