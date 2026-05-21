students = {}

# 查看功能
def look():
    print("1.输入学号查询联系方式")
    print("2.输入学号查指定学生信息")
    print("3.一键查看所有学生信息")
    try:
        choice = int(input())
    except ValueError:
        print("请输入数字")
        return

    if choice == 1:
        try:
            t = int(input("请输入学号查询联系方式："))
            info = students.get(t)
            if info:
                print(f"联系方式：{info['联系方式']}")
            else:
                print("学号不存在")
        except ValueError:
            print("请输入数字学号")
    elif choice == 2:
        try:
            sid = int(input("请输入学号查询学生信息："))
            result = students.get(sid, "学号不存在")
            print(result)
        except ValueError:
            print("请输入数字学号")
    elif choice == 3:
        if not students:
            print("暂无学生信息")
            return
        print("所有学生信息：")
        for sid, info in students.items():
            print(f"{sid}   {info['姓名']}   {info['性别']}   {info['联系方式']}")
    else:
        print("选择错误")

# 添加功能
def add():
    while True:
        try:
            sid = int(input("请输入要添加的学号："))
            if sid in students:
                print("学号已存在，无法重复添加")
                continue
            new_name = input("姓名：")
            new_sex = input("性别：")
            new_phone = input("联系方式：")
            students[sid] = {'姓名': new_name, '性别': new_sex, '联系方式': new_phone}
            print("添加成功！")
        except ValueError:
            print("学号必须是数字")
        ans = input("是否继续添加？(y/n)：").lower()
        if ans != 'y':
            break

# 删除功能
def delete():
    try:
        sid = int(input("请输入要删除的学号："))
        if sid in students:
            del students[sid]
            print("删除成功")
        else:
            print("学号不存在")
    except ValueError:
        print("请输入数字学号")

# 更新功能
def update():
    while True:
        try:
            sid = int(input("请输入要修改的学号："))
            if sid in students:
                new_name = input("新姓名：")
                new_sex = input("新性别：")
                new_phone = input("新联系方式：")
                students[sid]['姓名'] = new_name
                students[sid]['性别'] = new_sex
                students[sid]['联系方式'] = new_phone
                print("更新成功！")
            else:
                print("学号不存在")
        except ValueError:
            print("请输入数字学号")
        ans = input("是否继续更新？(y/n)：").lower()
        if ans != 'y':
            break

# 性别筛选功能
def sex_filter():
    search_sex = input("请输入要筛选的性别（male/female）：")
    print(f"性别为 {search_sex} 的学生如下：")
    found = False
    for sid, info in students.items():
        if info['性别'] == search_sex:
            print(f"学号：{sid}  姓名：{info['姓名']}  联系方式：{info['联系方式']}")
            found = True
    if not found:
        print("没有找到该性别的学生。")