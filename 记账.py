from datetime import datetime
from pathlib import Path
import json
wallet = Path("C:/Users/kevin/Desktop/git_记账/钱包.json")#获取钱包路径
py_dict = {'amount':319.34+788.36}#初始化
dic = json.dumps(py_dict)
wallet.write_text(dic)
today_date=datetime.today().date()#获取日期
str_date=today_date.strftime("%Y/%m/%d")
json_dict = wallet.read_text()#获取json字典
py_dict = json.loads(json_dict)#转换成python字典
amount = py_dict.get("amount","字典有误")#获取余额
if py_dict.get(str_date)==None:
    py_dict[str_date]={}

while True:
    print("--------记账--------")
    print("退出 请按'0'")
    print("支出 请按'1'")
    choice=input("请输入:")
    if choice=='0':
        break
    if choice=='1':
        expend_th=input("支出项目:")
        try:
            expend_m=float(input("支出金额:"))
            py_dict["amount"]=amount-expend_m
            py_dict[str_date][expend_th]=expend_m
            print(f"余额为{amount}元")
        except ValueError:
            print("输入数字md")
json_dict = json.dumps(py_dict,ensure_ascii=False)
wallet.write_text(json_dict)
    