#定义一个字符串，练习字符串的常用方法
"""
r='jgyshjg'
print(r.find('jg',0,5))#返回子字符串在母字符串第一次出现的位置
print(r.rfind('g',0,5))#返回子字符串在母字符串最后一次出现的位置
print(r.index('gy',0,5))#返回子字符串在母字符串第一次出现的下标
print(r.rindex('gy',0,5))#返回子字符串在母字符串最后一次出现的下标
print(r.count('jg'))#子字符串在母字符串中出现的次数
"""

"""
#查找每一个字符的第一次出现
text="东边来个小朋友叫小松，手里拿着一根葱"
print("每个字符第一次出现的位置")
for index,ch in enumerate(text):
    if index==text.index(ch):
        print((index,ch),end='')
#统计每一个字符的出现次数
print("\n每个字符的出现次数")
for _,ch in enumerate(text):
    print(f"{ch}:{text.count(str(ch))}")
"""

"""
txy='fgcg?jhgxf'
#以指定字符为分隔符，把原字符串分隔成多个字符串，并返回包含分割结果的列表
print(txy.split('g'))#以'g'为分隔符（原字符串里要出现分隔符）
print(txy.rsplit('g'))
#以指定字符串为分隔符将原字符串分隔成三部分（分隔符前字符串，分隔符，分隔符后字符串）
#如果指定的分隔符不在原字符串中，则返回原字符串和两个空字符串
print(txy.partition('g'))
print(txy.rpartition('g'))
"""
"""
words=('ghv','gg','h','b')
text='ggfcjhyus'
for word in words:
    if word in text:
        text=text.replace(word,'***')
print(text)
#maketrans() and translate
table=''.maketrans('abcdef123','uvwxyz@#$')
s="python is good!"
print(s.translate(table))
"""
#lower()所有大写变小写,title()每一个单词的首字母都大写,upper()所有小写换大写,capitalize()字符串的首字母大写，其余小写,swapcase()小写换大写，大写换小写
"""
test='hello world!I like python.this is a nice day.right?'
print("小写版本")
print(test.lower())
print("大写版本")
print(test.upper())
biaodian = "!.?"
cleaned=test
#把符号替换为空格
for t in biaodian:
    if t in test:
        cleaned = cleaned.replace(t, ' ')
print(cleaned)
# 按空格分割
words = cleaned.split()
word_count = len(words)
print("英文单词个数：", word_count)
print("单词列表：", words)
print()
k = int(input("请输入 k（整数）: "))
k = k % 26
# 准备原始字母表和移位后的字母表
lower_original = "abcdefghijklmnopqrstuvwxyz"
upper_original = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_shifted = lower_original[k:] + lower_original[:k]
upper_shifted = upper_original[k:] + upper_original[:k]
# 使用 str.maketrans 制作映射表
trans_table = str.maketrans(lower_original + upper_original,lower_shifted + upper_shifted)
# 进行加密
encrypted_text = test.translate(trans_table)
print(f"加密结果（移位 {k} 位）：", encrypted_text)
"""
"""
text=""
def main():
    while True:
        print("请输入字符串：")
        text = input()
        print(f"您输入的字符串为：{text}")
        print("请选择你想要的功能")
        print("1.所有字母变大写\n2.所有字母变小写\n3.统计其中英文单词的个数\n4.对文本进行加密（每个字母替换为后面n个）\n5.退出系统")
        try:
            num = int(input("我选择："))
        except ValueError:
            print("请输入数字！")
            continue
        if num == 1:
            print(text.upper())
        elif num == 2:
            print(text.lower())
        elif num == 3:
            tongjigeshu(text)
        elif num == 4:
            jiami(text)
        elif num == 5:
            print("感谢您的使用，即将退出系统")
            break
        else:
            print("没有该功能")
            break


def tongjigeshu(test):
    biaodian = ".,!?;:()\"'"
    cleaned=test
    for t in biaodian:
        if t in test:
            cleaned=cleaned.replace(t,' ')
    words = cleaned.split()
    word_count = len(words)
    print("英文单词个数：", word_count)
    print("单词列表：", words)
    main()

def jiami(test):
    print("请输入您想要后移的位数")
    n=int(input())
    n=n%26
    lower_original = "abcdefghijklmnopqrstuvwxyz"
    upper_original = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_shifted = lower_original[n:] + lower_original[:n]
    upper_shifted = upper_original[n:] + upper_original[:n]
    trans_table = str.maketrans(lower_original + upper_original, lower_shifted + upper_shifted)
    encrypted_text = test.translate(trans_table)
    print(f"加密结果（移位 {n} 位）：", encrypted_text)
    main()
main()
"""
"""
x='aabbccddeeeffg'
print(x.strip('af'))
print(x.strip('gaf'))
print(x.strip('gbaef'))
#str.strip(x)从两端开始扫描，扫描到第一个不属于x的元素就停
"""
#text="""姓名：张三
#年龄：39
#性别男
#职业  学生
#籍贯：   地球"""
"""
infomation=text.split('\n')
print(infomation)
for item in infomation:
    print(item[:2],item[2:].strip('： '),sep=':')
"""
"""
p='Hello world!'
print(p.center(20))
print(p.center(20,'='))
print(p.ljust(20,'='))
print(p.rjust(20,'='))
"""
"""
#随机密码生成原理
import string
print(string.digits)
print(string.punctuation)
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
characters=string.digits + string.ascii_letters
import random
x=list(random.choice(string.punctuation))
y=list(random.choice(characters) for i in range(3))
result=x+y
print(''.join(result))
"""
"""
#读取和写入文本文件
s='Hello world\n文本文件的读取方法\n文本文件的写入方法\n'
with open('sample.txt','w',encoding='utf-8') as fp:
    fp.write(s)
with open('sample.txt', encoding='utf-8') as fp:
    print(fp.read())
#读取并显示文本文件的前11个字符
with open('sample.txt','r',encoding='utf-8') as f:
    s=f.read(11)
print('s=',s)
print('字符串s的长度（字符个数）=',len(s))
#读取并显示文本文件的所有行
with open('sample.txt',encoding='utf-8') as fp:
    for line in fp:
        print(line)
#追加文件内容
a='Today is a good day.'
with open('sample.txt','a',encoding='utf-8') as fp:
    fp.write(a)
with open('sample.txt','r',encoding='utf-8') as fp:
    print(fp.read())
"""
"""
l=list()
for i in range(10):
    l.append(i)
l.reverse()
with open('data.txt','w') as fp:
    for j in l:
        fp.write(str(j))
        fp.write('\n')
# 读取 data.txt 中的所有整数
with open('data.txt', 'r', encoding='utf-8') as f:
    numbers = []
    for line in f:
        line = line.strip()          # 去除行首尾空白（包括换行符）
        if line:                     # 跳过空行
            numbers.append(line)
# 升序排序
numbers.sort()
# 写入 data_new.txt
with open('data_new.txt', 'w', encoding='utf-8') as f:
    for num in numbers:
        f.write(num)
        f.write('\n')
with open('data_new.txt','r',encoding='utf-8') as f:
    print(f.read())
print("排序完成，结果已保存到 data_new.txt")
"""

"""
import os
#读取当前目录
x1=os.getcwd()
print(f"当前目录为：{x1}")
#显示当前目录下的所有文件
x2=os.listdir(x1)
print(f"当前目录下的文件有：{x2}")
result = [fname for fname in x2 if os.path.isfile(fname) and fname.endswith('.txt')]
print("当前目录下后缀为.txt的文件有：")
print(result)
"""

#编写程序，用户自己输入一个目录和文件名，搜索该目录（以及其子目录下是否存在该文件，存在则输出文件路径
import os

def find_directory_and_search(dir_name, filename):
    """
    在当前目录下查找名为 dir_name 的目录，
    如果找到，则在该目录及其子目录中搜索 filename
    """
    current_dir = os.getcwd()
    target_dir = os.path.join(current_dir, dir_name)

    # 检查是否存在该名称的目录
    if not os.path.isdir(target_dir):
        print(f"错误：在当前目录下未找到名为 '{dir_name}' 的目录")
        return []

    # 在目标目录下递归搜索文件
    found_paths = []
    for root, dirs, files in os.walk(target_dir):
        if filename in files:
            found_paths.append(os.path.join(root, filename))
    return found_paths

def main():
    dir_name = input("请输入目录名（例如 data）：").strip()
    if not dir_name:
        print("目录名不能为空")
        return

    file_name = input("请输入要搜索的文件名：").strip()
    if not file_name:
        print("文件名不能为空")
        return

    results = find_directory_and_search(dir_name, file_name)

    if results:
        print(f"\n找到以下文件（共 {len(results)} 个）：")
        for path in results:
            print(path)
    else:
        print(f"未找到文件 '{file_name}'")


if __name__ == '__main__':
    main()