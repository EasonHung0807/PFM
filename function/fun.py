# coding=utf-8
__author__ = 'Eason'
import time, datetime
from months.models import *

#取得目前時間
def getNow():
    return datetime.datetime.now()

#取得年月份 yyyy/mm
def getYearMonth():
    return time.strftime('%Y/%m')

#取得日期 yyyy/mm/dd
def getDate():
    return time.strftime('%Y/%m/%d')

#取得現金提領&所有信用卡類別
def getAllcash_type():
    return cash_type.objects.all()

#取得所有投資資產類別
def getAllinvest_type():
    return invest_type.objects.all()

#取得投資資產最後一筆總投入金額
def getLastinvest_total(thisdate):
    try:
        num = months.objects.filter(YM=thisdate).latest('id').total_invest
    except months.DoesNotExist:
        num = 0
    return num

#取得投資資產最後一筆總餘額
def getLastinvest_rest(total):
    num = 0 #if初始要改?
    try:
        invest_list = invest.objects.all()
        for invest1 in invest_list:
            if invest1.invest_type =='p':
                num = int(total) + int(invest1.cash)
            else:
                num = int(total) - int(invest1.cash)
    except invest.DoesNotExist:
        num = 0
    return num

#取得月份明細最後一筆總現金
def getLastmonthly_CashTotal(thisdate):
    try:
        num = monthly.objects.filter(YM=thisdate).latest('id').total_cash
    except monthly.DoesNotExist:
        num = 0
    return num

#取得月份明細最後一筆總信用卡
def getLastmonthly_CreditTotal(thisdate):
    try:
        num = monthly.objects.filter(YM=thisdate).latest('id').total_credit
    except monthly.DoesNotExist:
        num = 0
    return num

#取得當月信用卡總結
def getThisMonthCreditSummery(thisdate,fixed_short_cost_list):
    cash_type_list = cash_type.objects.all()
    cash_type_dict={}
    for cash_type1 in cash_type_list:
        cash_type_dict[cash_type1.name] = 0
    #先計算月份明細資料
    try:
        monthly_list = monthly.objects.filter(YM=thisdate)
        for monthly1 in monthly_list:
            if monthly1.cash_type!='cash':
                cash_type_dict[monthly1.cash_type] = int(cash_type_dict[monthly1.cash_type]) + int(monthly1.credit)
    except monthly.DoesNotExist:
        monthly_list = {}
    #再計算短期固定花費&信用卡分期
    for fixed_short_cost1 in fixed_short_cost_list:
        if fixed_short_cost1.start_date == thisdate:
            if fixed_short_cost1.first_cost is None:
                cash_type_dict[fixed_short_cost1.cash_type] = int(cash_type_dict[fixed_short_cost1.cash_type]) + int(fixed_short_cost1.cost)
            else:
                cash_type_dict[fixed_short_cost1.cash_type] = int(cash_type_dict[fixed_short_cost1.cash_type]) + int(fixed_short_cost1.first_cost)
        else:
            cash_type_dict[fixed_short_cost1.cash_type] = int(cash_type_dict[fixed_short_cost1.cash_type]) + int(fixed_short_cost1.cost)

    return cash_type_dict

#取得上一個月
def PreYM(thisdate):
    year = thisdate.split('/')[0]
    month = thisdate.split('/')[1]
    if month=='01':
        year = int(year) - 1
        month = '12'
    elif int(month)<11:
        month = '0'+str(int(month)-1)
    else:
        month = int(month)-1
    return str(year)+'/'+str(month)

#上下月控制
def PreNextMonth(request):
    thisdate = request.POST['thisdate']
    year = thisdate.split('/')[0]
    month = thisdate.split('/')[1]
    atr = request.POST['atr']
    if atr=='pre':
        if month=='01':
            year = int(year) - 1
            month = '12'
        elif int(month)<11:
            month = '0'+str(int(month)-1)
        else:
            month = int(month)-1
    else:
        if month=='12':
            year = int(year) + 1
            month = '01'
        elif int(month)<9:
            month = '0'+str(int(month)+1)
        else:
            month = int(month)+1
    #201509不能再往前
    if year=='2015' and month=='08':
        month = '09'
    return str(year)+'/'+str(month)

#上下月控制
def PreNextMonth1(thisdate,atr):
    year = thisdate.split('/')[0]
    month = thisdate.split('/')[1]
    if atr=='pre':
        if month=='01':
            year = int(year) - 1
            month = '12'
        elif int(month)<11:
            month = '0'+str(int(month)-1)
        else:
            month = int(month)-1
    else:
        if month=='12':
            year = int(year) + 1
            month = '01'
        elif int(month)<9:
            month = '0'+str(int(month)+1)
        else:
            month = int(month)+1
    #201509不能再往前
    if year=='2015' and month=='08':
        month = '09'
    return str(year)+'/'+str(month)

#取得當月短期固定成本
def getShortCost(thisdate):
    resp_created_at = datetime.datetime.now()  # 擷取現在時間
    resp_modify_at = datetime.datetime.now()  # 擷取現在時間
    try:
        fixed_short_cost_list = fixed_short_cost.objects.filter(start_date__lte=thisdate,end_date__gte=thisdate) #取得當月短期固定成本
        for thefixed_short_cost in fixed_short_cost_list:
            try:
                fixed_short_cost_thism = fixed_short_cost1.objects.filter(YM=thisdate,short_costid = thefixed_short_cost.id).latest('id')
                thefixed_short_cost.cost = fixed_short_cost_thism.cost
                thefixed_short_cost.rent_cost =fixed_short_cost_thism.rent_cost
                thefixed_short_cost.rent_num =fixed_short_cost_thism.rent_num
            except fixed_short_cost1.DoesNotExist:
                if thisdate==thefixed_short_cost.start_date:
                    cost = thefixed_short_cost.first_cost
                else:
                    cost = thefixed_short_cost.cost
                this_num = getMonthDIffRange(thisdate,thefixed_short_cost.start_date)
                rent_num = int(thefixed_short_cost.total_num) - int(this_num)
                rent_cost = int(thefixed_short_cost.total_cost) - ((int(this_num) - 1) * int(cost)) - int(thefixed_short_cost.first_cost)
                fixed_short_cost1.objects.create(YM=thisdate,
                                 name=thefixed_short_cost.name,
                                 cost=cost,
                                 short_costid=thefixed_short_cost.id,
                                 memo=thefixed_short_cost.memo,
                                 rent_cost=rent_cost,
                                 rent_num=rent_num,
                                 created_at=resp_created_at,
                                 modify_at=resp_modify_at)
                thefixed_short_cost.cost = cost
                thefixed_short_cost.rent_cost =rent_cost
                thefixed_short_cost.rent_num =rent_num
    except months.DoesNotExist:
        fixed_short_cost_list={}
    return fixed_short_cost_list

def getMonthDIffRange(thisdate,startdate):
    tyear = thisdate.split('/')[0]
    tmonth = thisdate.split('/')[1]
    syear = startdate.split('/')[0]
    smonth = startdate.split('/')[1]
    if tyear == syear:
        return int(tmonth) - int(smonth) + 1 #若年份相同  直接月份相減即為差異
    elif (int(tmonth) - int(smonth)) > 0:
        return (int(tyear) - int(syear))*12 + int(tmonth) - int(smonth) + 1 #年份不同且相差大於12
    else:
        return (int(tyear) - int(syear) - 1)*12 + 12 - int(smonth) + int(tmonth) + 1 #若年份不同但相差小於12

def getThisdate(request):
    if request.session.get('thisdate', False)==False:
        thisdate =getYearMonth() #目前時間
        request.session['thisdate'] = thisdate
    else:
        thisdate = request.session.get('thisdate')
    #上/下一個月控制
    if 'atr' in request.POST:
        thisdate = PreNextMonth(request)
        request.session['thisdate'] = thisdate
    return thisdate