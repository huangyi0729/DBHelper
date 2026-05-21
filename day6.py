# import requests
#发送get请求，获取响应对象
# response=requests.get("https://httpbin.org/get")
#解析响应对象中的信息
# print("状态码:",response.status_code)
# print("响应头:",response.headers)
# print("响应内容:",response.text)

#导入库&定义URL
# import requests
# url="https://httpbin.org/get"
#定义字典格式的参数
# payload={
#     "name":"张三","age":25,"city":"Beijing"
# }
# 发送请求并解析结果
# res=requests.get(url,params=payload)
# print("最终请求URL:",res.url)
# print("响应内容:",res.json())

# import requests
# resp=requests.get("https://httpbin.org/get")
# 获取原始文本vs解析为字典
# print("类型(text):",type(resp.text))
# 直接转为字典
# data=resp.json()
# print("类型(json):",type(data))

# import requests
#200状态正常400请求语法错误或参数有误404服务器无法找到请求的资源500服务器内部发生未知错误
# resp=requests.get("https://httpbin.org/status/200")
#直接打印状态码
# print("状态码:",resp.status_code)
#自动检测异常
# try:
#     resp.raise_for_status()
# except requests.HTTPError as e:
#     print("请求出错:",e)

# import requests
# try:
    # 目标URL响应延迟2秒
    # r=requests.get("https://httpbin.org/delay/2",timeout=5)
    # 检查HTTP状态码
    # r.raise_for_status()
    # print("请求成功")
# except requests.exceptions.Timeout:
#     print("请求超时,请检查网络或重试")
# except requests.exceptions.RequestException as e:
#     print("未知错误",e)

# import requests
# try:
#     r1 = requests.get("https://httpbin.org/ip")
#     print("状态码:", r1.status_code)
#     data=r1.json()
#     print("响应内容(json):", data)
#     print("我的公网IP地址为:",data['origin'])
#     print("请求成功")
# except requests.exceptions.Timeout:
#     print("请求超时")
# except requests.exceptions.ConnectionError as e:
#     print("连接错误")

#定义一个类
# class Student:
#     school="新余学院"
#     def study(self):
#         print(f"{self.name}正在学习")
#创建对象
# student1=Student()
# student2=Student()
# student1.name,student2.name="李华","小明"
# print(student1.school)
# student1.study()

# class Student:
#     def set_name(self,name):
#         self.name=name
#     def get_name(self):
#         return self.name
# s=Student()
# s.set_name("李四")
# print(s.get_name())
# class Car:
#     color="白色"
#     def run(self):
#         print(f"一辆{self.color}的车正在行驶")
#
# car1=Car()
# car1.run()
# car2=Car()
# car2.color="红色"
# car2.run()

# class Student:
#     school="新余学院"
#     stu_class="23计科1班"
#     def __init__(self,name,sex):
#         self.name=name
#         self.sex=sex
# s1=Student("张三","男")
# s2=Student("李四","女")
# print(s1.name,s1.sex,s1.school,s1.stu_class)
# print(s2.name,s2.sex,s2.school,s2.stu_class)
# print(Student.school,Student.stu_class)
# Student.school="江西理工大学"
# print(s1.school,s2.school)

# class Rectangle:
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
#     def get_area(self):
#         area=self.width * self.height
#         return area
#     def get_perimeter(self):
#         perimeter=(self.width + self.height)*2
#         return perimeter
#     @classmethod
#     def create_square(cls,side):
#         return cls(side,side)
#
# juxing=Rectangle(5,3)
# print(f"矩形面积:{juxing.get_area()},周长:{juxing.get_perimeter()}")
# zhengfangxing = Rectangle.create_square(4)
# print(f"正方形面积:{zhengfangxing.get_area()},周长:{zhengfangxing.get_perimeter()}")

# class Ferson:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
#     def get_age(self):
#         return self.age
#     def set_age(self,age):
#         if 0< age<150:
#             self.__age=age
#         else:
#             print("年龄不合法!")
# p=Ferson("张三",27)
# p.set_age(177)

# class Shape:
#     def get_area(self):
#         return 0
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#     def get_area(self):
#         return self.side * self.side
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def get_area(self):
#         return 3.14 * self.radius * self.radius
#
# def calculate_total_area(shapes):
#     total = 0
#     for shape in shapes:
#         total += shape.get_area()
#     return total
#
# square = Square(4)
# circle = Circle(2)
#
# shape_list = [square, circle]
# total_area = calculate_total_area(shape_list)
# print(f"总面积：{total_area:.2f}")
#
# class BankAccount:
#     def __init__(self, account_id: str, name: str, initial_balance: float, password: str):
#         self.account_id = account_id
#         self.name = name
#         self.__balance = initial_balance
#         self.__password = password
#
#     def _verify_password(self, input_pwd: str) -> bool:
#         return self.__password == input_pwd
#
#     def show_balance(self, password: str) -> float:
#         if self._verify_password(password):
#             print(f"账户 {self.account_id} - {self.name} 当前余额: {self.__balance:.2f}")
#             return self.__balance
#         else:
#             print("密码错误，无法查看余额！")
#             return None
#
#     def deposit(self, amount: float) -> bool:
#         if amount <= 0:
#             print("存款金额必须为正数！")
#             return False
#         self.__balance += amount
#         print(f"存款成功！存入 {amount:.2f}，当前余额: {self.__balance:.2f}")
#         return True
#
#     def withdraw(self, amount: float, password: str) -> bool:
#         if not self._verify_password(password):
#             print("密码错误，无法取款！")
#             return False
#         if amount <= 0:
#             print("取款金额必须为正数！")
#             return False
#         if amount > self.__balance:
#             print("余额不足，取款失败！")
#             return False
#         self.__balance -= amount
#         print(f"取款成功！取出 {amount:.2f}，剩余余额: {self.__balance:.2f}")
#         return True
#
#     def change_password(self, old_password: str, new_password: str) -> bool:
#         if not self._verify_password(old_password):
#             print("旧密码错误，修改失败！")
#             return False
#         if len(new_password) < 6:
#             print("新密码长度至少为6位！")
#             return False
#         self.__password = new_password
#         print("密码修改成功！")
#         return True
# def create_a_account():
#     ac_id=input("账户号:")
#     ac_name=input("账户名:")
#     ac_password=input("密码设置为:")
#     user=BankAccount(ac_id,ac_name,ac_password,balance=0)
#     print(f"账户 {self.account_id} - {self.name} 密码: {ac_password}当前余额: {self.__balance:.2f}")
#
# create_a_account()
