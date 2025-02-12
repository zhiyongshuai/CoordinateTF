import matplotlib.pyplot as plt

# 创建一些数据
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# 创建一个图形
plt.plot(x, y, label='y = x^2')

# 添加标题和标签
# plt.title("简单的 matplotlib 图")
# plt.xlabel("X 轴")
# plt.ylabel("Y 轴")

# 添加图例
plt.legend()

# 显示图形
plt.show()
