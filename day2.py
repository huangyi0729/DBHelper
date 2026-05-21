#question1
"""
l=list(enumerate('abcd',start=1))
print(l)
"""
#输入元素能找到索引
"""
fruits = ['apple', 'banana', 'organge']
print("请输入水果名称：")
t=input()
found = False
for index, fruit in enumerate(fruits, start=1):
    if fruit == t:
        print(f"找到了！'{t}' 的索引是 {index}")
        found = True
        break
if not found:
    print("列表中没有该元素")
"""

#question2
#输入1~5，输出它们的平方，用map函数
"""
def pingfang(num):
    return num**2
l=list(map(pingfang,range(1,6)))
print(l)
"""

#question3
#用filter函数筛选奇数
"""
l=list(range(1,11))
def check_jiou(num):
    if num%2==0:
        return False
    else:
        return True
l1=list(filter(check_jiou,l))
print(l1)
"""

#question4
#筛选正数，并把正数乘2
"""
l=[-2,-9,1,8,7,9,-4]
def check_zhengfu(num):
    if num>0:
        return True
    else:
        return False
l1=list(filter(check_zhengfu,l))
print(l1)
def cheng(num):
    return num*2
l2=list(map(cheng,l1))
print(l2)
"""

#question5
#统计学生合格人数，把学生姓名和成绩一一对应
"""
s = ['lihua', 'linxue', 'xiaoming']
g = ['59', '88', '75']
l = list(zip(s, g))
print(l)
n1 = sum(1 for num in g if int(num) >= 60)
print(f"合格的人数为{n1}")

def exam(name):
    for student, grade in l:
        if student == name:
            print(f"{student}的成绩是{grade}")
            if int(grade) >= 60:
                print("合格")
            else:
                print("不合格")
            return
    # 循环结束没找到
    print("未找到该学生信息")

print("请输入学生姓名：")
name = input()
exam(name)
"""


#question 6
#输出每个人的语数英三科成绩，计算每个人的总分和平均分，平均分>85优秀，<60不合格
"""
chinese = [95, 99, 79]
math = [45, 76, 98]
english = [78, 65, 76]
students = ['lihua', 'linxue', 'xiaoming']
grade = list(zip(students, chinese, math, english))

print("各科成绩")
print(grade)

def xitong():
    # 计算总分和平均分
    al = []  # 总分
    ave = []  # 平均分
    for student, yu, shu, ying in grade:
        z = yu + shu + ying
        a = z / 3
        al.append(z)
        ave.append(a)

    grade1 = list(zip(students, al, ave))
    print("个人的总分与平均分")
    grade2 = [(name, round(a, 2), round(av, 2)) for name, a, av in grade1]
    print(grade2)

    # 个人等级评价
    print("个人等级评价：")
    for s, a, av in grade1:
        if av >= 85:
            print(f"{s}为优秀学生")
        elif av < 60:
            print(f"{s}为不合格学生")
        else:
            print(f"{s}为合格学生")

    max_chinese = max(chinese)
    idx_c = chinese.index(max_chinese)
    student_c = students[idx_c]

    max_math = max(math)
    idx_m = math.index(max_math)
    student_m = students[idx_m]

    max_english = max(english)
    idx_e = english.index(max_english)
    student_e = students[idx_e]
    print("每科最高分：")
    print(f"语文最高分：{max_chinese} 分，学生：{student_c}")
    print(f"数学最高分：{max_math} 分，学生：{student_m}")
    print(f"英语最高分：{max_english} 分，学生：{student_e}")
xitong()
"""


#question7
# 学生信息全部输入，要求能多次输入
"""
students = []
chinese = []
math = []
english = []

def input_students():
    #循环接收用户输入的学生姓名及三科成绩
    print("开始输入学生信息（输入空姓名结束）：")
    while True:
        name = input("请输入学生姓名：").strip()
        if name == "":
            print("输入结束。")
            break
        try:
            c = float(input(f"请输入{name}的语文成绩："))
            m = float(input(f"请输入{name}的数学成绩："))
            e = float(input(f"请输入{name}的英语成绩："))
        except ValueError:
            print("成绩必须为数字，请重新输入该学生信息。")
            continue
        students.append(name)
        chinese.append(c)
        math.append(m)
        english.append(e)
        print(f"学生 {name} 已添加。\n")

def xitong():
    #统计并输出每个学生的总分、平均分、等级，以及各科最高分
    if not students:
        print("没有学生数据，请先输入学生信息。")
        return

    # 构建成绩元组列表
    grade = list(zip(students, chinese, math, english))
    print("\n各科成绩（姓名，语文，数学，英语）：")
    print(grade)

    # 计算总分和平均分
    al = []   # 总分
    ave = []  # 平均分
    for student, yu, shu, ying in grade:
        z = yu + shu + ying
        a = z / 3
        al.append(z)
        ave.append(a)

    grade1 = list(zip(students, al, ave))
    print("\n个人的总分与平均分（保留两位小数）：")
    grade2 = [(name, round(a, 2), round(av, 2)) for name, a, av in grade1]
    print(grade2)

    # 个人等级评价
    print("\n个人等级评价：")
    for s, a, av in grade1:
        if av >= 85:
            print(f"{s} 为优秀学生")
        elif av < 60:
            print(f"{s} 为不合格学生")
        else:
            print(f"{s} 为合格学生")

    # 每科最高分及对应学生
    max_chinese = max(chinese)
    idx_c = chinese.index(max_chinese)
    student_c = students[idx_c]

    max_math = max(math)
    idx_m = math.index(max_math)
    student_m = students[idx_m]

    max_english = max(english)
    idx_e = english.index(max_english)
    student_e = students[idx_e]

    print("\n每科最高分：")
    print(f"语文最高分：{max_chinese} 分，学生：{student_c}")
    print(f"数学最高分：{max_math} 分，学生：{student_m}")
    print(f"英语最高分：{max_english} 分，学生：{student_e}")

# 主程序
input_students()
xitong()
"""

#question8
#输入一个学生的成绩，输出对应的成绩等级
"""
students = []
print("请输入学生姓名和成绩（格式：姓名 成绩）")
data = input().split()

if len(data) != 2:
    print("输入格式错误，必须输入姓名和成绩（用空格分隔）")
else:
    name, score_str = data[0], data[1]
    try:
        score = float(score_str)
        # 判断成绩是否在 0~100 之间
        if 0 <= score <= 100:
            if score >= 90:
                grade = 'A'
            elif score >= 80:
                grade = 'B'
            elif score >= 70:
                grade = 'C'
            elif score >= 60:
                grade = 'D'
            else:
                grade = 'E'
            print(f"{name}的成绩为{grade}")
        else:
            print("数据不合法：成绩应在0~100之间")
    except ValueError:
        print("数据不合法：成绩必须是数字")
"""

#question9
"""
grade = []
def fenshu():
    while True:
        if len(grade) == 0:
            print("请输入第一个分数：")
        else:
            print("请输入下一个分数：")

        try:
            score = float(input())
            grade.append(score)
        except ValueError:
            print("输入无效，请输入数字！")
            continue

        # 询问是否继续
        while True:
            choice = input("是否继续输入？(y/n): ")
            if choice in ('y', 'n'):
                break
            print("请回复 y 或 n")

        if choice == 'n':
            print("输入结束")
            break

fenshu()
# 计算平均值（避免除零）
if len(grade) == 0:
    print("没有输入任何分数，无法计算平均值。")
else:
    average = sum(grade) / len(grade)
    print(f"平均分为：{average:.2f}")
"""

#question10
#输出1~100里所有的素数
"""
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
primes = [str(num) for num in range(101) if is_prime(num)]
print("100以内的素数有：")
print(primes)
l=max(primes)
print(f"100以内最大的素数为{l}")
"""
#question11
#求100以内能被7整除，不能被5整除的整数
"""
ns=[]
def suan(num):
    if num%7==0 and num%5!=0:
        ns.append(num)
for i in range(101):
    suan(i)
print(ns)
"""

#question12
#求3位水仙花数
"""
for num in range(100, 1000):
    a = num // 100          # 百位
    b = (num // 10) % 10    # 十位
    c = num % 10            # 个位
    if a**3 + b**3 + c**3 == num:
        print(num)
"""

#question13
#求n位水仙花数
"""
def find_shui(n):
    if n <= 0:
        print("位数 n 必须是正整数")
        return
    # 范围
    start = 10 ** (n - 1)
    end = 10 ** n - 1

    found = False
    for num in range(start, end + 1):
        # 计算各位数字的 n 次幂之和
        total = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            total += digit ** n
            temp //= 10
        if total == num:
            print(num)
            found = True

    if not found:
        print(f"不存在 {n} 位水仙花数")


# 用户输入
n = int(input("请输入位数："))
find_shui(n)
"""

"""
n=int(input("请输入位数:"))
for num in range(10**(n-1),10**n):
    if sum(map(lambda i:int(i)**n,str(num)))==num:
        print(num)
"""
#question14
#编写函数，生成一个含20个随机整数的列表，对其中偶数下标的元素降序排序，奇数下标的元素保持不变
import random
def process_list():
    #生成20个1~100之间的随机整数
    lst = [random.randint(1, 100) for _ in range(20)]
    print("原始列表：", lst)
    #提取偶数下标的元素
    even_index_elements = [lst[i] for i in range(0, len(lst), 2)]
    #对提取的元素进行降序排序
    even_index_elements.sort(reverse=True)
    #将排序后的元素放回原列表的偶数下标位置
    for i, val in zip(range(0, len(lst), 2), even_index_elements):
        lst[i] = val
    return lst

#输出结果
result = process_list()
print("处理后列表：", result)