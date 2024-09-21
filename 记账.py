from datetime import datetime
from pathlib import Path
import json
wallet = Path("V:/camera/文档/钱包.json")#获取钱包路径
#py_dict = {'amount':394.74}初始化
#dic = json.dumps(py_dict)
#wallet.write_text(dic)
today_date=datetime.today().date()#获取日期
json_dict = wallet.read_text()#获取json字典
py_dict = json.loads(json_dict)#转换成python字典
amount = py_dict.get("amount","字典有误")#获取余额
#with open("C:/Users/Kevin/Desktop/账本.txt","a",encoding="UTF-8") as f:
    #f.write(f"\n------{today_date}------\n")
QUIT = False
while QUIT == False:
    expend_th = input("支出项目:")
    if expend_th == "q":
        break
    try:    
        expend_m = float(input("支出金额:"))
        py_dict[expend_th]=expend_m
        amount -= expend_m
        py_dict["amount"]=amount

    except ValueError:
        print("金额必须为数字")
    finally:
        print(f"余额为{amount}")
        
json_dict = json.dumps(py_dict,ensure_ascii=False)
wallet.write_text(json_dict)
    