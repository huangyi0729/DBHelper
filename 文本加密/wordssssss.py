import os

# 全局变量，存储当前正在操作的文本
current_text = ""


def load_from_file():
    """从文件 data.txt 加载文本，如果文件不存在则返回 None"""
    if os.path.exists("../上课练习/data.txt"):
        with open("../上课练习/data.txt", "r", encoding="utf-8") as f:
            return f.read()
    else:
        return None


def save_to_file(text):
    """将文本保存到 data.txt"""
    with open("../上课练习/data.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("已保存到 data.txt")


def fenge():
    """统计当前文本中的英文单词个数"""
    global current_text
    biaodian = ".,!?;:()\"'"
    cleaned = current_text
    for t in biaodian:
        if t in current_text:
            cleaned = cleaned.replace(t, ' ')
    words = cleaned.split()
    word_count = len(words)
    print("英文单词个数：", word_count)
    print("单词列表：", words)


def jiami():
    """对当前文本进行凯撒加密，可选择是否保存"""
    global current_text
    print("请输入您想要后移的位数")
    n = int(input())
    n = n % 26
    lower_original = "abcdefghijklmnopqrstuvwxyz"
    upper_original = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_shifted = lower_original[n:] + lower_original[:n]
    upper_shifted = upper_original[n:] + upper_original[:n]
    trans_table = str.maketrans(lower_original + upper_original, lower_shifted + upper_shifted)
    encrypted_text = current_text.translate(trans_table)
    print(f"加密结果（移位 {n} 位）：", encrypted_text)

    # 询问是否保存
    save_choice = input("是否将加密后的文本保存到文件？(y/n): ").strip().lower()
    if save_choice == 'y':
        current_text = encrypted_text  # 更新当前文本为加密后的文本
        save_to_file(current_text)
        print("当前文本已更新为加密后的版本")
    else:
        print("未保存，当前文本保持不变")


def main():
    global current_text
    # 尝试从文件加载初始文本
    file_text = load_from_file()
    if file_text is not None:
        print("从 data.txt 加载已有文本：")
        print(file_text)
        current_text = file_text
    else:
        print("未找到 data.txt，请先输入初始文本：")
        current_text = input("请输入字符串：")
        # 可选择是否保存初始文本
        save_init = input("是否将初始文本保存到 data.txt？(y/n): ").strip().lower()
        if save_init == 'y':
            save_to_file(current_text)

    while True:
        print("\n当前文本：", current_text)
        print("请选择你想要的功能")
        print("1. 所有字母变大写")
        print("2. 所有字母变小写")
        print("3. 统计其中英文单词的个数")
        print("4. 对文本进行加密（每个字母替换为后面n个）")
        print("5. 退出系统")
        print("6. 保存当前文本到文件")

        try:
            num = int(input("我选择："))
        except ValueError:
            print("请输入数字！")
            continue

        if num == 1:
            print(current_text.upper())
        elif num == 2:
            print(current_text.lower())
        elif num == 3:
            fenge()
        elif num == 4:
            jiami()
        elif num == 5:
            print("感谢您的使用，即将退出系统")
            break
        elif num == 6:
            save_to_file(current_text)
        else:
            print("没有该功能，请重新选择")


if __name__ == "__main__":
    main()