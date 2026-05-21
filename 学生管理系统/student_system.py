from functions import look, add, delete, update, sex_filter

def system():
    while True:
        print("\n学生管理系统")
        print("1.查看指定或全体学生信息")
        print("2.添加学生信息")
        print("3.删除学生信息")
        print("4.更新学生信息")
        print("5.按性别筛选")
        print("6.退出系统")
        try:
            num = int(input("你的选择是："))
        except ValueError:
            print("请输入数字！")
            continue

        if num == 1:
            look()
        elif num == 2:
            add()
        elif num == 3:
            delete()
        elif num == 4:
            update()
        elif num == 5:
            sex_filter()
        elif num == 6:
            print("退出系统")
            break
        else:
            print("选择错误")

if __name__ == "__main__":
    system()