# import os
# def visitDir2(path):
#     if not os.path.isdir(path):
#         print('Error:"',path,'"is not a directory or does not exist.')
#         return
#     list_dirs=os.walk(path)#os.walk返回一个元组，包括3个元素：所有路径名、所有目录列表与文件列表
#     for root,dirs,files in list_dirs:#遍历该元组的目录和文件信息
#         for d in dirs:
#             print(os.path.join(root,d))#获取完整路径
#         for f in files:
#             print(os.path.join(root,f))#获取相对路径
# print(os.getcwd())#查看当前目录
# visitDir2(r"C:\Users\dell\PycharmProjects\PythonProject5\暑假实训")

#编写程序，统计指定文件夹大小及文件和子文件夹数量
import os

def get_folder(folder_path):
    #路径不存在或者不是文件夹
    if not os.path.exists(folder_path):
        return None,None,None,"路径不存在"
    if not os.path.isdir(folder_path):
        return None,None,None,"不是文件夹"

    total_size = 0
    file_count = 0
    folder_count = 0

    # os.walk 遍历所有子文件夹和文件
    for root, dirs, files in os.walk(folder_path):
        # 统计当前目录下的文件数
        file_count += len(files)
        # 统计当前目录下的子目录数
        folder_count += len(dirs)
        # 累加文件大小
        for file in files:
            file_path = os.path.join(root, file)
            try:
                total_size += os.path.getsize(file_path)
            except OSError:
                # 忽略无法访问的文件（如权限问题）
                pass
    return total_size, file_count, folder_count, None


def format_size(size_bytes):
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 ** 2:
        return f"{size_bytes / 1024:.2f} KB"
    elif size_bytes < 1024 ** 3:
        return f"{size_bytes / (1024 ** 2):.2f} MB"
    elif size_bytes < 1024 ** 4:
        return f"{size_bytes / (1024 ** 3):.2f} GB"
    else:
        return f"{size_bytes / (1024 ** 4):.2f} TB"


def main():
    folder = input("请输入要统计的文件夹路径: ").strip()
    size, file_cnt, folder_cnt, err = get_folder(folder)
    if err:
        print(f"错误: {err}")
        return
    print(f"\n文件夹: {folder}")
    print(f"总大小: {format_size(size)} ({size} 字节)")
    print(f"文件数量: {file_cnt}")
    print(f"子文件夹数量: {folder_cnt}")


if __name__ == "__main__":
    main()