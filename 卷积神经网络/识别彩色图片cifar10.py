import os
import warnings
#屏蔽所有 Python 警告（包括弃用、用户警告）
warnings.filterwarnings('ignore')
# 屏蔽 TensorFlow C++ 后端日志
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'   # 3 = 只显示致命错误
#屏蔽 TensorFlow Python 日志（如 GPU 不可用警告）
import tensorflow as tf
tf.get_logger().setLevel('ERROR')
#屏蔽 absl 日志（TensorFlow 依赖的日志库）
import absl.logging
absl.logging.set_verbosity(absl.logging.ERROR)
import tensorflow as tf
from tensorflow.keras import layers, models, Sequential
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 随机种子保证可复现
tf.random.set_seed(42)
np.random.seed(42)

# 加载 CIFAR-10 数据集
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
print(f"训练集形状: {x_train.shape}")   # (50000, 32, 32, 3)
print(f"测试集形状: {x_test.shape}")    # (10000, 32, 32, 3)

# 数据预处理（归一化 + 独热编码）
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# 构建 CNN 模型
model = Sequential([
    # 第一组卷积层
    layers.Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(32, 32, 3)),
    layers.Conv2D(32, (3, 3), activation='relu', padding='same'),
    layers.MaxPooling2D((2, 2)),
    layers.Dropout(0.25),

    # 第二组卷积层
    layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
    layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
    layers.MaxPooling2D((2, 2)),
    layers.Dropout(0.25),

    # 第三组卷积层
    layers.Conv2D(128, (3, 3), activation='relu', padding='same'),
    layers.Conv2D(128, (3, 3), activation='relu', padding='same'),
    layers.MaxPooling2D((2, 2)),
    layers.Dropout(0.25),

    # 全连接层
    layers.Flatten(),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax')
])

model.summary()

# 编译模型
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 训练模型（不使用数据增强，直接使用原始数据）
batch_size = 64
epochs = 30

history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    validation_data=(x_test, y_test),
                    verbose=1)

# 评估模型
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
print(f"\n测试集准确率: {test_acc:.4f}")

# 绘制训练曲线
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='训练损失')
plt.plot(history.history['val_loss'], label='验证损失')
plt.title('损失曲线')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='训练准确率')
plt.plot(history.history['val_accuracy'], label='验证准确率')
plt.title('准确率曲线')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

plt.tight_layout()
plt.show()

# 随机抽样预测并可视化
class_names = ['飞机', '汽车', '鸟', '猫', '鹿',
               '狗', '青蛙', '马', '船', '卡车']

num_samples = 9
indices = np.random.choice(len(x_test), num_samples, replace=False)
sample_images = x_test[indices]
sample_labels = np.argmax(y_test[indices], axis=1)

predictions = model.predict(sample_images)
predicted_labels = np.argmax(predictions, axis=1)

plt.figure(figsize=(10, 10))
for i in range(num_samples):
    plt.subplot(3, 3, i+1)
    plt.imshow(sample_images[i])
    true_label = class_names[sample_labels[i]]
    pred_label = class_names[predicted_labels[i]]
    color = 'green' if true_label == pred_label else 'red'
    plt.title(f'真: {true_label}\n预: {pred_label}', color=color)
    plt.axis('off')
plt.tight_layout()
plt.show()