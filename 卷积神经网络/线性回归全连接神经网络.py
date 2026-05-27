import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.datasets import boston_housing
from tensorflow.keras.layers import Dense,Input
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows 系统常用黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题
import numpy as np

# 加载数据
(x_train, y_train), (x_test, y_test) = boston_housing.load_data()

print(f"训练集特征形状: {x_train.shape}, 目标值形状: {y_train.shape}")
print(f"测试集特征形状: {x_test.shape}, 目标值形状: {y_test.shape}")

#标准化
def standardize(x_train, x_test):
    mean = np.mean(x_train, axis=0)
    std = np.std(x_train, axis=0)
    # 防止除零
    std[std == 0] = 1.0
    x_train_scaled = (x_train - mean) / std
    x_test_scaled = (x_test - mean) / std
    return x_train_scaled, x_test_scaled

x_train, x_test = standardize(x_train, x_test)

# 目标值不需要标准化（但对结果无影响），仅重塑为二维
y_train = y_train.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)

# 构建线性回归模型
model = Sequential([
    Input(shape=(13,)),
    Dense(1, activation='linear')
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])
model.summary()

#  训练模型
history = model.fit(x_train, y_train,
                    epochs=50,
                    batch_size=32,
                    validation_split=0.2,
                    verbose=1)

#  绘制训练曲线
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Loss over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Mean Squared Error')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['mae'], label='Training MAE')
plt.plot(history.history['val_mae'], label='Validation MAE')
plt.title('Mean Absolute Error over Epochs')
plt.xlabel('Epochs')
plt.ylabel('MAE (千美元)')
plt.legend()
plt.tight_layout()
plt.show()

# 评估模型
test_loss, test_mae = model.evaluate(x_test, y_test, verbose=0)
print(f"\n测试集均方误差 (MSE): {test_loss:.4f}")
print(f"测试集平均绝对误差 (MAE): {test_mae:.4f} 千美元")
print(f"换算成美元的平均绝对误差约为: {test_mae * 1000:.2f} 美元")

# 预测演示
predictions = model.predict(x_test[:5], verbose=0)
pred_values = predictions.flatten()
true_values = y_test[:5].flatten()

print("\n前5个测试样本的预测值与真实值对比：")
for i in range(5):
    print(f"样本{i+1}: 预测 = {pred_values[i]:.2f} 千美元, 真实 = {true_values[i]:.2f} 千美元")
