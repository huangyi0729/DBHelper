import os
# 关闭 oneDNN 提示信息
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
# 设置日志级别，只显示 WARNING 和 ERROR
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
from PIL import Image

# 加载并训练 MNIST 手写数字模型
# MNIST 数据集：28x28 灰度图，标签 0~9
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# 归一化到 [0,1]
x_train, x_test = x_train / 255.0, x_test / 255.0

# 构建与原始结构类似的简单全连接网络
model = models.Sequential([
    layers.Input(shape=(28, 28)),   # 输入 28x28
    layers.Flatten(),               # 展平为 784
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(10, activation='softmax')  # 10 个数字类别
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

# 训练10轮
history = model.fit(x_train, y_train, epochs=10, validation_split=0.2, shuffle=True)

# 在测试集上评估
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f"MNIST 测试集准确率：{test_acc:.4f}")

#外部图片预处理函数
def preprocess_image(image_path, target_size=(28, 28)):
    img = Image.open(image_path).convert('L')      # 转为灰度图
    img = img.resize(target_size, Image.Resampling.LANCZOS)  # 调整至 28x28
    img_array = np.array(img)                      # 形状 (28, 28)
    # 归一化到 [0,1]
    img_array = img_array / 255.0
    # 模型输入需要形状 (1, 28, 28) 即 batch 维度
    img_array = img_array.reshape(1, 28, 28)
    return img_array

# 识别指定图片中的数字
image_path = r"C:\Users\dell\Desktop\cdf9c8a1017f98225d2dc6f16bb3f690.jpg"
try:
    input_image = preprocess_image(image_path)
    prediction = model.predict(input_image, verbose=0)
    predicted_digit = np.argmax(prediction[0])   # 概率最大的类别
    print(f"\n识别结果：图片中的数字是 {predicted_digit}")
except Exception as e:
    print(f"图片读取或处理失败：{e}")