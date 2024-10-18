import pandas as pd
import numpy as np
from scipy.stats import zscore
from sklearn.linear_model import LinearRegression

# 示例数据
# A和B是时间序列数据
np.random.seed(0)
dates = pd.date_range('2020-01-01', periods=1000)
A = pd.Series(np.random.randn(1000), index=dates)
B = pd.Series(np.random.randn(1000), index=dates)


# 计算Z分数的函数
def ts_zscore(series, window=500):
    """计算时间序列的Z分数，基于过去window天的数据"""
    return (series - series.rolling(window=window).mean()) / series.rolling(window=window).std()


# 计算时间序列回归的函数
def ts_regression(A_z, B_z, window=500):
    """对时间序列A和B进行线性回归"""
    # 将A和B的Z分数对齐
    A_z = A_z.dropna()
    B_z = B_z.dropna()
    common_index = A_z.index.intersection(B_z.index)
    A_z, B_z = A_z.loc[common_index], B_z.loc[common_index]

    # 回归模型
    model = LinearRegression()

    # 用滚动窗口执行线性回归
    regression_results = []
    for i in range(window, len(common_index)):
        X = A_z[i - window:i].values.reshape(-1, 1)
        y = B_z[i - window:i].values
        model.fit(X, y)
        regression_results.append(model.coef_[0])

    return pd.Series(regression_results, index=common_index[window:])


# 计算A和B的Z分数
A_z = ts_zscore(A, 500)
B_z = ts_zscore(B, 500)

# 对标准化后的A和B执行回归分析
regression_result = ts_regression(A_z, B_z, 500)

# 输出前几个结果
print(regression_result)
