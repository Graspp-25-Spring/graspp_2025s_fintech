# [1단계] 필요한 라이브러리 불러오기
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# [2단계] 현재 파일 기준 프로젝트 루트 경로 설정
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# [3단계] 데이터 경로 설정
file_path = os.path.join(project_root, 'data', 'processed', 'gfi_digital_transaction_pivot_table.csv')

# [4단계] 데이터 불러오기
df = pd.read_csv(file_path)  # 절대 경로 사용!

# [5단계] 데이터 확인하기
print(df.head())  # 데이터 첫 5줄 미리보기

# [6단계] 시각화에 사용할 컬럼명 설정 (너 데이터에 맞게 수정해야 해!)
x = 'year'  # X축에 쓸 컬럼명
y = 'indicator'  # Y축에 쓸 컬럼명
hue = 'country'

# [7단계] 그래프 그리기
plt.figure(figsize=(10, 6))
sns.regplot(data=df, x=x, y=y, scatter_kws={"color": "blue"}, line_kws={"color": "red"})

plt.title('Relationship between Digital Presence and Financial Inclusion', fontsize=16)
plt.xlabel('Digital Presence', fontsize=14)
plt.ylabel('Financial Inclusion', fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.show()