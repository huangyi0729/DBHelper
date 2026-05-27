#question1
#输入一个三位数，输出该数各位上的数字
"""
n=int(input())
if n >=100 and n<=999:
    h=n//100
    t=(n//10)%10
    u=n%10
    print("百位数：")
    print(h)
    print("十位数：")
    print(t)
    print("个位数：")
    print(u)
else:
    print("请输入一个三位整数：")
"""


#question2
#输入两条直角边，求斜边
"""
print("请输入第一条直角边：")
a=float(input())
print("请输入第二条直角边：")
b=float(input())
if a>=0 and b>=0:
    c=pow(a,2)+pow(b,2)
    result=pow(c,0.5)
else:
    print("不能形成三角形")
print("斜边长：")
print(result)
"""


#question1'
#输入一个数，逆序输出，如输入123，最终输出321
"""
print("请输入一个数：")
n1=input()
n11=n1[::-1]
n11=int(n11)
print("逆序输出后，结果为：")
print(n11)
"""


#question3
#任意输入三个英文单词，然后输出它们在字典里的排序
"""
print("请输入第一个单词")
w1=input()
print("请输入第二个单词")
w2=input()
print("请输入第三个单词")
w3=input()
words=[w1,w2,w3]
result=sorted(words)
print(result)
"""


#question3'
#用比较的方式再写一遍问题3
"""
print("请输入第一个单词")
w1=input()
print("请输入第二个单词")
w2=input()
print("请输入第三个单词")
w3=input()
if w1<=w2 and w1<=w3:
    first=w1
    if w2<=w3:
        second=w2
        third=w3
    else:
        second=w3
        third=w2
elif w2<=w1 and w2<=w3:
    first=w2
    if w1<=w3:
        second=w1
        third=w3
    else:
        second=w3
        third=w1
else:
    first=w3
    if w1<=w2:
        second=w1
        third=w2
    else:
        second=w2
        third=w1
print(first,second,third)
"""


#question4
#根据ord和chr来写一个判断字母大小写的函数
"""
def check_letter_case(character):
    if len(character) != 1:
        return "请输入单个字符"
    # 获取字符的 ASCII 码
    ascii_code = ord(character)
    # 大写字母 A-Z 的 ASCII 码范围 65-90
    if 65 <= ascii_code <= 90:
        return "大写字母"
    # 小写字母 a-z 的 ASCII 码范围 97-122
    elif 97 <= ascii_code <= 122:
        return "小写字母"
    else:
        return "非字母"

if __name__ == "__main__":
    test_chars = ['A', 'z', '3', '@']
    for ch in test_chars:
        print(f"'{ch}' -> {check_letter_case(ch)}")
"""


#question4'
#把单词里面的字母大写变小写，小写变大写
"""
def swap_case(word):
    result = []
    for ch in word:
        ascii_code = ord(ch)
        # 大写字母 A-Z (65-90)
        if 65 <= ascii_code <= 90:
            result.append(chr(ascii_code + 32))
        # 小写字母 a-z (97-122)
        elif 97 <= ascii_code <= 122:
            result.append(chr(ascii_code - 32))
        else:
            # 非字母保持不变
            result.append(ch)
    return ''.join(result)

if __name__ == "__main__":
    test_word = input("请输入一个单词: ")
    swapped = swap_case(test_word)
    print(f"转换结果: {swapped}")
"""

#question5
#自己编写一个能实现加减乘除的简易计算器
"""
print("输入运算的第一个数")
num1=float(input())
print("输入你想进行的运算符号")
y=input()
print("输入运算的第二个数")
num2=float(input())
result=0
if y=='+':
    result=num1+num2
elif y=='-':
    result=num1-num2
elif y=='*':
    result=num1*num2
elif y=='/':
    if num2 != 0:
        result=num1/num2
    else:
        print("除数不能为0")
else:
    print("不符合加减乘除运算")
print(f"{result:.2f}")
"""


def calculator():
    """一个支持循环使用的简单计算器"""
    print("=== 简易运算器 ===")
    print("支持运算: + (加), - (减), * (乘), / (除)")
    while True:
        print("\n" + "-" * 30)
        # 获取第一个数字
        try:
            num1 = float(input("请输入第一个数字: "))
        except ValueError:
            print("输入无效，请输入数字")
            continue
        # 获取运算符
        op = input("请输入运算符 (+, -, *, /): ").strip()
        if op not in ('+', '-', '*', '/'):
            print("无效运算符，请使用 +、-、* 或 /")
            continue
        # 获取第二个数字
        try:
            num2 = float(input("请输入第二个数字: "))
        except ValueError:
            print("输入无效，请输入数字")
            continue
        # 计算并显示结果
        if op == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif op == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif op == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif op == '/':
            if num2 == 0:
                print("除数不能为零")
                continue
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        # 询问是否继续
        again = input("\n是否继续计算？(y/n): ").strip().lower()
        if again == 'n':
            print("感谢使用，再见！")
            break


# 运行计算器
if __name__ == "__main__":
    calculator()