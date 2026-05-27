# class ShortInputException(Exception):
#     def __init__(self,length,atleast):
#         Exception.__init__(self)
#         self.length=length
#         self.atleast=atleast
# try:
#     s=input("请输入：")
#     if len(s)<3:
#         raise ShortInputException(len(s),3)
# except EOFError:
#     print("你输入了一个结束标记EOF")
# except ShortInputException as x:
#     print("ShortInputException:长度是%d,至少应该是%d"%(x.length,x.atleast))
# else:
#     print("无异常发生")
# y=[]
# while True:
#     x=input("Please input:")
#     try:
#         x = int(x)
#         y.append(x)
#         print("You have input {0}".format(x))
#         print("是否继续输入y/n")
#         choice=input()
#         if choice=='n':
#             result=','.join(str(num) for num in y)
#             print(f"all you have input:{result}")
#             break
#         elif choice=='y':
#             continue
#     except Exception as e:
#         print("Error.")
# class EmptyInputError(Exception):
#     """自定义异常：输入为空"""
#     pass
#
# class OutOfRangeError(Exception):
#     """自定义异常：成绩超出范围"""
#     pass
#
# while True:
#     try:
#         grade_str = input("请输入学生成绩：").strip()
#         if not grade_str:
#             raise EmptyInputError("输入不能为空")
#         grade = float(grade_str)
#         if grade < 0 or grade > 100:
#             raise OutOfRangeError("成绩超出正常范围（0-100）")
#     except EmptyInputError as e:
#         print(e)
#         continue
#     except ValueError:
#         print("请输入数字，请重新输入")
#         continue
#     except OutOfRangeError as e:
#         print(e)
#         continue
#     else:
        # print(f"学生成绩为:{grade}")
        # break
#四种导入模块
#from '模块名' import '功能'（导入整体）
#import '模块名'
#from '模块名' import *(导入全部）
#import '模块名' as '别名'

# from newcode import add
# print(add(4,6))
# import newcode
# print(newcode.add(7,9))
# from newcode import *
# print(add(0,8))
# import newcode as nc`
# print(nc.add(5,8))

# from timecode import *
# def main():
#     showtime()
#     yanzhengma()
# main()

#import json
#准备一个Python字典对象
#user_data={"name":"李四","age":30,"skills":["Python","Java"]}
#序列化 字典->JSON字符串
#ensure_ascii=False才能显示中文
#indent=1表示缩进1个空格
#json_str=json.dumps(user_data,ensure_ascii=False,indent=1)
#print("转换后的JSON字符串:\n",json_str)
#反序列化 JSON字符串->Python字典
# parsed_dict=json.loads(json_str)
# print("\n提取姓名:",parsed_dict["name"])
# print("\n提取技能列表:",parsed_dict["skills"])

json_data={
"company": "Alibaba",
"employees": [{"name": "Alice", "position": "Engineer", "salary": 10000},
              {"name": "Bob", "position": "Manager", "salary": 15000}],
"location": "Hangzhou"}
import json
json_str=json.dumps(json_data,ensure_ascii=False,indent=1)
#print(json_str)
parsed_dict=json.loads(json_str)
print("提取公司名称:",parsed_dict["company"])
print("提取公司所在地:",parsed_dict["location"])
count=0
x=[]
y=[]
for a in parsed_dict["employees"]:
    x.append(a["name"])
    y.append(a["position"])
    count+=a["salary"]
print("职员姓名：工作")
employee=dict(zip(x,y))
for name,position in employee.items():
    print(f"{name}:{position}")
print("所有员工的平均工资")
print(count/(len(parsed_dict["employees"])))