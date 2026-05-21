#%Y年份(2026)%m月份(01-12)%d日期(01-31)%M分钟%S秒%A星期几(Sunday)%B月份(May)
from datetime import datetime
import random
import string
def showtime():
    now = datetime.now()
    fmt1 = now.strftime("%Y年%m月%d日 %H:%M:%S")
    fmt2 = now.strftime("%A,%B %d,%Y")
    print(f"时间为：{fmt1}")
    #print(fmt2)

def yanzhengma():
    xs=string.digits + string.ascii_uppercase
    cc=list(random.choice(xs) for i in range(6))
    print(f"验证码为：{''.join(cc)}")
