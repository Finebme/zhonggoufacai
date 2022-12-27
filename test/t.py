import os
import tushare as ts
tu_token = '3b10a950807b74742478c1d7e0e17970a822e639bbf9940b5c3b3995'
pro = ts.pro_api(tu_token)


def get_stock_basic():
    data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    print(data)

#描述：获取各大交易所交易日历数据,默认提取的是上交所
def get_trade_calender():
    df = pro.query('trade_cal', start_date='20180101', end_date='20181231')
    print(df)

#描述：历史名称变更记录
def get_name_list():
    df = pro.namechange(ts_code='600848.SH', fields='ts_code,name,start_date,end_date,change_reason')
    print(df)

#获取可以北上购买的股票
def get_hs_exchange():
    # 获取沪股通成分
    da = pro.hs_const(hs_type='SH')
    # 获取深股通成分
    df = pro.hs_const(hs_type='SZ')

    print(da)
    print(df)

#描述：获取上市公司基础信息，单次提取4500条，可以根据交易所分批提取
def get_company_basic_info():
    df = pro.stock_company(exchange='SZSE', fields='ts_code,chairman,manager,secretary,reg_capital,setup_date,province')
    print(df)

def get_path():
    print(__file__)
    return __file__

if __name__ == "__main__":
    print('start')
    #print(os.path.dirname(os.path.realpath(get_path())))
    get_company_basic_info()

