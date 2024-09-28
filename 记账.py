"""注意!!!!!!"""
print("注意!!!!!!!\n用完一定要按0")
from datetime import datetime
from pathlib import Path
import json
wallet = Path("C:/Users/kevin/Desktop/git_记账/钱包.json")#获取钱包路径
#py_dict = {'amount':493.41+148.94}#初始化
#dic = json.dumps(py_dict)
#wallet.write_text(dic)
today_date=datetime.today().date()#获取日期
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")#获取时间
update_path = Path("C:/Users/kevin/Desktop/git_记账/更新记录.json")#创建路径对象
json_list = update_path.read_text(encoding='UTF-8')
py_list = json.loads(json_list)#获得py时间列表
py_list.append(current_time)#更新时间列表
json_list = json.dumps(py_list)#转换成已更新的json列表

print(current_time)#打印当前时间
str_date=today_date.strftime("%Y/%m/%d")#获取日期字符串
json_dict = wallet.read_text(encoding='UTF-8')#获取json字典
py_dict = json.loads(json_dict)#转换成python字典
py_dict['amount'] = py_dict.get("amount","字典有误")#获取余额
if py_dict.get(str_date)==None:
    py_dict[str_date]={}#用日期创建一个key,value为支出字典
def c_amount():#一个查询函数
    am=py_dict['amount']
    print(f"余额为{am:.2f}元")
    return am
def record():#一个写入函数
    json_dict = json.dumps(py_dict,ensure_ascii=False)
    wallet.write_text(json_dict,encoding='UTF-8')



while True:#主循环
    print("--------记账--------")
    print(f"                ------上次更新时间为{py_list[-2]}")
    print("写入并退出 请按'0'")
    print("支出 请按'1'")
    print("收入 请按'2'")
    print("查看余额 请按'3'")

    choice=input("请输入:")
    if choice=='0':
        break
    if choice=='1':
        expend_th=input("支出项目:")
        try:
            expend_m=float(input("支出金额:"))
            py_dict["amount"]=py_dict['amount']-expend_m
            py_dict[str_date][expend_th]=-expend_m###支出存储为负数
            record()
            c_amount()
        except ValueError:
            print("输入数字!")
    if choice=='2':
        income_th = input("收入来源:")
        try:
            income_m=float(input("收入金额:"))
            py_dict["amount"]=py_dict['amount']+income_m
            py_dict[str_date][income_th]=income_m
            record()
            c_amount()
        except ValueError:
            print("输入数字!!")    
    if choice=='3':
        c_amount()



update_path.write_text(json_list)    