# 워드클라우드 설치 오류
# https://visualstudio.microsoft.com/downloads/ 에서 community > build tools 를 설치합니다.

# 그래도 오류가 나면 모듈을 다운받아 cmd창에서 직접 설치해요
# https://www.lfd.uci.edu/~gohlke/pythonlibs/ 에 접속합니다.
# 여기서 일반 wordcloud를 찾아 링크타고 들어가요
# wordcloud-1.6.0-cpXX-cpXXm-winXXXX.whl 파일을 받는데, 이때, 본인의 Python 버전 & 비트수 확인해서 맞는 것으로 하세요.
# 우리는 python 버전이  3.8 이므로
# wordcloud‑1.6.0‑cp38‑cp38‑win32.whl 파일을 받으면 됩니다.
# cmd에서, 다운받은 경로로 이동 후 pip install wordcloud‑1.6.0‑cp38‑cp38‑win32.whl 하면 설치됩니다.

import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud

f = open("i_have_a_dream.txt", "r", encoding="utf-8")
text = f.read()
f.close()
# print(text)

cloud = WordCloud().generate(text)
plt.imshow(cloud, interpolation="bilinear")
plt.axis('off')
plt.savefig("out.jpg")              #워드클라우드를 파일로 저장해요!
plt.close()
print("차트를 생성했습니다.")
# plt.show()