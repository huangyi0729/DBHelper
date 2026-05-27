import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras import Input
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
#加载数据
(x_train,y_train),(x_test,y_test)=fashion_mnist.load_data()
x_train=x_train.reshape(-1,28,28,1).astype('float32')/255.0
x_test=x_test.reshape(-1,28,28,1).astype('float32')/255.0
y_train=to_categorical(y_train,10)
y_test=to_categorical(y_test,10)
#构建模型
model = Sequential([
    Input(shape=(28, 28, 1)),#第一层卷积
    Conv2D(32, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),#第一层池化
    Conv2D(64, (3, 3), activation='relu'),#第二层卷积
    MaxPooling2D((2, 2)),#第二层池化
    Flatten(),#展平层
    Dense(128, activation='relu'),#全连接层
    Dropout(0.2),
    Dense(10, activation='softmax')#输出层
])
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
#打印模型摘要
model.summary()
#训练模型
history=model.fit(x_train,y_train,epochs=5,validation_split=0.2,shuffle=True)
test_loss,test_acc=model.evaluate(x_test,y_test,verbose=2)
print(f"测试准确率：{test_acc:.4f}")
#预测模型
predictions=model.predict(x_test[:5])
top5_labels = tf.argmax(predictions[:5], axis=1).numpy()
print(top5_labels)