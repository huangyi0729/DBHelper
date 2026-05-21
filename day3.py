#自己定义一个列表，运用pop等方法看看效果
"""
l=[4,8,'a',[7,3]]
l.append(9)
print(l)
l1=[]
l1.extend(l)
l1.insert(4,'a')
print(l1)
l1.remove(4)
print(l1)
l1.pop()
print(l1)
l.clear()
print(l)
print(l1.index('a'))
print(l1.count('a'))
l1.reverse()
print(l1)
l=l1.copy()
print(l)
l2=[1,2,4,5,2,5]
l2.sort()
print(l2)
l2.remove(2)
l2.insert(1,6)
print(l2)
"""

#创建一个空列表，循环输入三个名字，用append进行添加。把列表翻转输出，统计列表里第二个元素出现的次数
"""
l=[]
while True:
    name = input("请输入姓名：")
    l.append(name)
    print("是否输入y/n")
    t=input()
    if t=='n':
        break
print(l)
l.reverse()
print(l)
for a in l:
    if l.index(a)==1:
        print(l.count(a))
"""

#熟悉字典用法
"""
l1=[1,2,3,4,5,6,7]
l2=['a','b','c','d','e','f','g']
d=dict(zip(l1,l2))
print(d)
print(d.items())
print(d.keys())
print(d.values())
print(d.get(6))
d[8]='h'
d[0]='A'
print(d)
del d[2]
print(d)
"""


#用字典重写一遍成绩等级
"""
print("请输入学生姓名和成绩（格式：姓名 成绩）")
data = input().split()
if len(data) != 2:
    print("输入格式错误，必须输入姓名和成绩（用空格分隔）")
else:
    name, score_str = data[0], data[1]
    try:
        score = float(score_str)
        if 0 <= score <= 100:
            # 存储到字典中
            student['name'] = name
            student['score'] = score

            # 根据分数判定等级
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

            # 从字典中读取姓名并输出
            print(f"{student['name']}的成绩为{grade}")
        else:
            print("数据不合法：成绩应在0~100之间")
    except ValueError:
        print("数据不合法：成绩必须是数字")
"""

#字典存储学生信息，包括学号、姓名、性别、联系方式。取某个学号的学生的联系方式
"""
xuehao = [1,2,3,4]
names = ['lihua','linxue','hujian','xiaoming']
sex = ['male','female','male','male']
phone = [159,163,182,191]

students = {}
for i in range(len(xuehao)):
    students[xuehao[i]] = {
        '姓名': names[i],
        '性别': sex[i],
        '联系方式': phone[i]
    }
students[5] = {'姓名': 'lily','性别': 'female','联系方式': 159}  # 添加一组数据

print("所有学生信息：")
for stu_id, info in students.items():
    print(f"{stu_id}   {info['姓名']}   {info['性别']}   {info['联系方式']}")

# 按学号查询联系方式
try:
    t = int(input("\n请输入学号查询联系方式："))
    info = students.get(t)
    if info:
        print(f"联系方式：{info['联系方式']}")
    else:
        print("学号不存在")
except ValueError:
    print("请输入数字学号")

# 删除指定学号的学生信息
del students[3]
print(students)

students.pop(5, None)
print(students)

students.popitem()
print(students)

# 更新指定学生的数据
try:
    t1 = int(input("\n请输入要修改的学号："))
    if t1 in students:
        print("请输入修改后的学生信息：")
        new_name = input("新姓名：")
        new_sex = input("新性别：")
        new_phone = input("新联系方式：")
        students[t1]['姓名'] = new_name
        students[t1]['性别'] = new_sex
        students[t1]['联系方式'] = new_phone
        print("更新成功！")
    else:
        print("学号不存在")
except ValueError:
    print("请输入数字学号")

print("\n更新后的字典：", students)

#按性别筛选
search_sex = input("\n请输入要筛选的性别（male/female）：")
print(f"\n性别为 {search_sex} 的学生如下：")
found = False
for stu_id, info in students.items():
    if info['性别'] == search_sex:
        print(f"学号：{stu_id}  姓名：{info['姓名']}  联系方式：{info['联系方式']}")
        found = True
if not found:
    print("没有找到该性别的学生。")
"""
#学生信息管理系统
def xitong():
    print("学生管理系统")
    print("1.查看指定或全体学生信息\n2.添加学生信息\n3.删除学生信息\n4.更新学生信息\n5.按性别筛选\n6.退出系统")
    print("你的选择是：")
    num=int(input())
    if num==1:
        look()
    elif num==2:
        add()
    elif num==3:
        delete()
    elif num==4:
        upd()
    elif num==5:
        sex()
    elif num==6:
        print("退出系统")
    else:
        print("选择错误")
def look():
    print("1.输入学号查询联系方式\n2.输入学号查指定学生信息\n3.一键查看所有学生信息")
    choice=int(input())
    if choice==1:
        try:
            t = int(input("\n请输入学号查询联系方式："))
            info = students.get(t)
            if info:
                print(f"联系方式：{info['联系方式']}")
            else:
                print("学号不存在")
        except ValueError:
            print("请输入数字学号")
    elif choice==2:
        id=int(input("\n请输入学号查询学生信息："))
        print(students.get(id))
    elif choice==3:
        print("所有学生信息：")
        for stu_id, info in students.items():
            print(f"{stu_id}   {info['姓名']}   {info['性别']}   {info['联系方式']}")
    else:
        print("选择错误")
    xitong()
def add():
    while True:
        try:
            t1 = int(input("请输入要添加的学号："))
            print("请输入要添加的学生信息：")
            new_name = input("新姓名：")
            new_sex = input("新性别：")
            new_phone = input("新联系方式：")
            students[t1]={'姓名': new_name,'性别': new_sex,'联系方式': new_phone}
            print("添加成功！")
            for stu_id, info in students.items():
                print(f"{stu_id}   {info['姓名']}   {info['性别']}   {info['联系方式']}")
        except ValueError:
            print("请输入数字学号")
        print("是否继续添加y/n")
        answer=input()
        if answer=='n':
            break
    xitong()
def delete():
    print("请输入要删除的学号：")
    t2=int(input())
    del students[t2]
    print("删除成功")
    for stu_id, info in students.items():
        print(f"{stu_id}   {info['姓名']}   {info['性别']}   {info['联系方式']}")
    xitong()
def upd():
    while True:
        try:
            t1 = int(input("请输入要修改的学号："))
            if t1 in students:
                print("请输入修改后的学生信息：")
                new_name = input("新姓名：")
                new_sex = input("新性别：")
                new_phone = input("新联系方式：")
                students[t1]['姓名'] = new_name
                students[t1]['性别'] = new_sex
                students[t1]['联系方式'] = new_phone
                print("更新成功！")
                for stu_id, info in students.items():
                    print(f"{stu_id}   {info['姓名']}   {info['性别']}   {info['联系方式']}")
            else:
                print("学号不存在")
        except ValueError:
            print("请输入数字学号")
        print("是否继续更新y/n")
        answer = input()
        if answer == 'n':
            break
    xitong()
def sex():
    search_sex = input("\n请输入要筛选的性别（male/female）：")
    print(f"\n性别为 {search_sex} 的学生如下：")
    found = False
    for stu_id, info in students.items():
        if info['性别'] == search_sex:
            print(f"学号：{stu_id}  姓名：{info['姓名']}  联系方式：{info['联系方式']}")
            found = True
    if not found:
        print("没有找到该性别的学生。")
    xitong()
students=dict()
xitong()

