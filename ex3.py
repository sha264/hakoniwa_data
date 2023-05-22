import numpy as np
import matplotlib.pyplot as plt

trial_num = 10
ep_trial_num = 8

# ファイル名のリスト
#files = [f"result_data{i}.csv" for i in range(1, trial_num + 1)]
ep_files = [f"data{i}.csv" for i in range(1, ep_trial_num + 1)]

# 各ファイルを読み込み、各カラムの平均を取る
"""
average_values = []
for file in files:
    data = np.genfromtxt(file, delimiter=',')
    average_values.append(np.mean(data, axis=0))
"""

ep_average_values = []
for file in ep_files:
    data = np.genfromtxt(file, delimiter=',')
    ep_average_values.append(np.mean(data, axis=0))

# 全試行にわたる各カラムの平均を計算
#overall_average = np.mean(average_values, axis=0)

# グラフの作成
plt.figure(figsize=(10, 6))

for i in range(len(ep_files)):
    plt.plot(range(1, 6), ep_average_values[i], label=ep_files[i])


# 全試行の平均をプロット
#plt.plot(range(1, 11), overall_average, label="Overall Average", linewidth=3, color='black')

plt.xlabel("Columns")
plt.ylabel("Average")
plt.ylim(0,450000)
#plt.yscale('log')  # 対数スケールに設定
plt.title("Average values of each column for different files")
plt.legend()
plt.show()
