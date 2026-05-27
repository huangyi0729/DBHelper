import requests
import re

API_KEY = "1fc8ed2a66ce929fec188ef6320b50fb"
city="新余"
if not city:
    print("请输入正确的城市（必须是中文城市名）")
url = "https://restapi.amap.com/v3/weather/weatherInfo"
params_base={"city":city,"key":API_KEY,"extensions":"base","output":"json"}
response = requests.get(url,params=params_base)
data_base=response.json()
print(data_base)

def todayweather():
    if data_base['status']=='1':
        if data_base['lives']:
            weather=data_base['lives'][0]
            print("当前天气")
            print(f"城市:{weather['city']}")
            print(f"天气:{weather['weather']}")
            print(f"温度:{weather['temperature']}℃")
            print(f"风向:{weather['winddirection']}风")
            print(f"湿度:{weather['humidity']}%")
            print(f"更新时间:{weather['reporttime']}")


params_all={"city":city,"key":API_KEY,"extensions":"all","output":"json"}


def predictweather():
    res_all = requests.get(url, params=params_all, timeout=10)
    data_all = res_all.json()
    if data_all['status'] == '1':
        forecasts = data_all.get('forecasts')
        if forecasts:
            forecast = forecasts[0]
            city_name = forecast['city']
            report_time = forecast['reporttime']
            casts = forecast.get('casts', [])
            print(f"\n未来天气预报 - {city_name}")
            print(f"数据发布时间: {report_time}\n")
            for day in casts:
                print(f"日期: {day['date']} 星期{day['week']}")
                print(f"  白天天气: {day['dayweather']}，温度 {day['daytemp']}℃")
                print(f"  夜晚天气: {day['nightweather']}，温度 {day['nighttemp']}℃")
                print(f"  风向: 白天 {day['daywind']}风，风力 {day['daypower']}级")
                print(f"        夜晚 {day['nightwind']}风，风力 {day['nightpower']}级")
                print("-" * 30)
        else:
            print("未找到天气预报数据")
    else:
        print(f"获取天气预报失败: {data_all.get('info', '未知错误')}")

def main():
    try:
        print("欢迎进入天气系统")
        print("请选择功能\n1.查看今日天气预报\n2.查看今天及后面三天的天气预报")
        choice = int(input())
        if choice == 1:
            todayweather()
        elif choice == 2:
            predictweather()
        else:
            print("没有该功能，退出系统")
    except ValueError:
        print("请输入数字")
main()