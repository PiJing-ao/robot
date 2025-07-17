import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 设置时间节点：2024年8月到2025年6月，每周一次
weeks = pd.date_range(start="2024-08-01", end="2025-06-15", freq='W')
num_weeks = len(weeks)

# 分界时间点：2025年2月1日
split_point = pd.Timestamp("2025-02-01")
split_index = weeks.get_loc(weeks[weeks >= split_point][0])

# 划分前后阶段
before_weeks = weeks[:split_index]
after_weeks = weeks[split_index:]
np.random.seed(42)

# 使用前成绩（均值约104，略波动）
before_scores = np.random.normal(loc=104, scale=2.5, size=len(before_weeks))
before_scores = np.round(before_scores, 1)

# 使用后成绩（稳步上升，最后一个月平均为125.5）
initial_score = before_scores[-1]
last_month_weeks = after_weeks[-4:]
target_avg_last_month = 125.5
final_scores = np.linspace(initial_score, target_avg_last_month + 1, len(after_weeks))  # +1 便于控制最后均值
fluctuation = np.random.normal(0, 1.5, size=len(after_weeks))
after_scores = np.round(final_scores + fluctuation, 1)

# 调整最后一个月的平均为125.5
last_month_indices = after_df_idx = np.array([i for i, w in enumerate(after_weeks) if w in last_month_weeks])
current_last_month_avg = np.mean(after_scores[last_month_indices])
adjustment = 125.5 - current_last_month_avg
after_scores[last_month_indices] += adjustment
after_scores = np.round(after_scores, 1)

# 构造 DataFrame
before_df = pd.DataFrame({
    "Week": before_weeks,
    "Score": before_scores
})
after_df = pd.DataFrame({
    "Week": after_weeks,
    "Score": after_scores
})

# 绘图
plt.figure(figsize=(12, 6))
plt.plot(before_df["Week"], before_df["Score"], label="Before Using AI Teachers", marker='o', color='steelblue')
plt.plot(after_df["Week"], after_df["Score"], label="After Using AI Teachers", marker='o', color='goldenrod')

# 分界线：2025年2月1日
plt.axvline(x=split_point, color='red', linestyle='--', label='Start Using (Feb 2025)')

plt.title("Student English Score Improvement (Aug 2024 - Jun 2025)")
plt.xlabel("Week")
plt.ylabel("English Score")
plt.legend()
plt.grid(True)
plt.tight_layout()

# 保存图表
img_path = "score_trend_targeted_avg.png"
plt.savefig(img_path)
plt.show()
