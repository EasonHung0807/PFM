# coding=utf-8
from django.shortcuts import render
from months.models import *
from django.http import HttpResponse
import datetime,time
from function import fun #方法集合

# Create your views here.
#新增短期固定成本level1
def NewShortCost(request):
    cash_type_list = fun.getAllcash_type()
    thisdate = fun.getThisdate(request)
    if request.method == 'POST':
        resp_name = request.POST['name']
        resp_cost = request.POST['cost']
        resp_cash_type = request.POST['cash_type']
        resp_start_date = request.POST['start_date']
        resp_end_date = request.POST['end_date']
        resp_memo = request.POST['memo']
        resp_total_cost = request.POST['total_cost']
        resp_total_num = request.POST['total_num']
        resp_first_cost = request.POST['first_cost']
        resp_created_at = datetime.datetime.now()  # 擷取現在時間
        resp_modify_at = datetime.datetime.now()  # 擷取現在時間
        fixed_short_cost.objects.create(name=resp_name,
                                 cost=resp_cost,
                                 cash_type=resp_cash_type,
                                 start_date=resp_start_date,
                                 end_date=resp_end_date,
                                 memo=resp_memo,
                                 total_cost=resp_total_cost,
                                 first_cost=resp_first_cost,
                                 total_num=resp_total_num,
                                 created_at=resp_created_at,
                                 modify_at=resp_modify_at)
        return render(request, 'newshortcost.html', {'message': '新增成功!!'
            , 'cash_type_list': cash_type_list
             ,'thisdate': thisdate
             ,'thispage': 'newshortcost'
                                                     })
    else:
        return render(request,'newshortcost.html', {'cash_type_list': cash_type_list
             ,'thisdate': thisdate
             ,'thispage': 'newshortcost'
                                                    })

#新增月份資料
def NewMonth(request):
    cash_type_list = fun.getAllcash_type()
    thisdate = fun.getThisdate(request)
    message=''
    thisother_income = {}
    thisother_cost = {}
    #return HttpResponse(thisdate) TODO
    data_dict={'salary':0,'bonus':0,'phone_cost':0,'parent_cost':0,'common_cost':0,'invest_grow':0,'invest_money':0}
    if request.method == 'POST':
        #新增月份資料
        if 'btn_premonth' in request.POST:
            thismonth = months.objects.filter(YM__lt=thisdate).latest('id')
            data_dict['salary'] = thismonth.salary
            data_dict['bonus'] = thismonth.bonus
            data_dict['phone_cost'] = thismonth.phone_cost
            data_dict['parent_cost'] = thismonth.parent_cost
            data_dict['common_cost'] = thismonth.common_cost
            data_dict['invest_grow'] = thismonth.invest_grow
            data_dict['invest_money'] = thismonth.invest_money
            search_thisdate = thismonth.YM

            #取得當月其他收入
            try:
                thisother_income = other_income.objects.filter(YM=search_thisdate)
            except other_income.DoesNotExist:
                thisother_income={}
            #取得當月其他支出
            try:
                thisother_cost = other_cost.objects.filter(YM=search_thisdate)
            except other_cost.DoesNotExist:
                thisother_cost={}
            message = '已讀取前月資訊'
        elif 'salary' in request.POST:
            resp_salary = 0 if request.POST['salary'] is None else request.POST['salary']
            resp_bonus = 0 if request.POST['bonus'] is None else request.POST['bonus']
            resp_phone_cost = 0 if request.POST['phone_cost'] is None else request.POST['phone_cost']
            resp_parent_cost = 0 if request.POST['parent_cost'] is None else request.POST['parent_cost']
            resp_common_cost = 0 if request.POST['common_cost'] is None else request.POST['common_cost']
            resp_invest_grow = 0 if request.POST['invest_grow'] is None else request.POST['invest_grow']
            resp_invest_money = 0 if request.POST['invest_money'] is None else request.POST['invest_money']
            #其他收入陣列
            resp_other_income_name=[]
            resp_other_income=[]
            resp_nmonthcash_type_income=[]
            if 'other_income_name' in request.POST:
                resp_other_income_name = request.POST.getlist('other_income_name')
                resp_other_income = request.POST.getlist('other_income')
            #其他支出陣列
            resp_other_cost_name = []
            resp_other_cost = []
            resp_nmonthcash_type_cost = []
            if 'other_cost_name' in request.POST:
                resp_other_cost_name = request.POST.getlist('other_cost_name')
                resp_other_cost = request.POST.getlist('other_cost')
                resp_nmonthcash_type_cost = request.POST.getlist('nmonthcash_type_cost')

            now = fun.getNow()
            resp_created_at = now  # 擷取現在時間
            resp_modify_at = now  # 擷取現在時間

            #計算總投資餘額
            try:
                total_invest = int(months.objects.latest('id').total_invest) + int(resp_invest_money)
            except months.DoesNotExist:
                total_invest = resp_invest_money
            #計算本月餘額-收入
            balance = int(resp_salary) + int(resp_bonus)
            for other_income1 in resp_other_income:
                balance = int(balance) + int(other_income1)
            #計算本月餘額-支出
            balance = int(balance) - int(resp_phone_cost) - int(resp_parent_cost) - int(resp_common_cost) - int(resp_invest_grow) - int(resp_invest_money)
            for other_cost1 in resp_other_cost:
                balance = int(balance) - int(other_cost1)

            try:
                months.objects.get(YM=thisdate)
                message='當月資料已存在'
            except months.DoesNotExist:
                #新增月份資料
                months.objects.create(YM=thisdate,
                                     salary=resp_salary,
                                     bonus=resp_bonus,
                                     parent_cost=resp_parent_cost,
                                     common_cost=resp_common_cost,
                                     phone_cost=resp_phone_cost,
                                     invest_money=resp_invest_money,
                                     invest_grow=resp_invest_grow,
                                     total_invest=total_invest,
                                     balance=balance, # 未扣短期固定花費&信用卡分期餘額
                                     balance1 = balance,
                                     balance2 = 0,
                                     total_balance = 0,
                                     created_at=resp_created_at,
                                     modify_at=resp_modify_at)
                #新增其他支出
                for index,other_cost1 in enumerate(resp_other_cost_name):
                    other_cost.objects.create(YM=thisdate,
                                     name=resp_other_cost_name[index],
                                     cost=resp_other_cost[index],
                                     cash_type=resp_nmonthcash_type_cost[index],
                                     created_at=resp_created_at,
                                     modify_at=resp_modify_at)
                #新增其他收入
                for index,other_income1 in enumerate(resp_other_income_name):
                    other_income.objects.create(YM=thisdate,
                                     name=resp_other_income_name[index],
                                     cost=resp_other_income[index],
                                     created_at=resp_created_at,
                                     modify_at=resp_modify_at)
                message='新增成功!!'
        return render(request, 'newmonth.html', {'message': message
                                                 ,'thisdate': thisdate
                                                 ,'thispage': 'newmonth'
                                                 ,'thisother_income': thisother_income
                                                 ,'thisother_cost': thisother_cost
                                                 ,'data_dict': data_dict
                                                 ,'cash_type_list': cash_type_list})
    else:
        return render(request,'newmonth.html', {'thisdate': thisdate
                                                ,'thispage': 'newmonth'
                                                 ,'thisother_income': thisother_income
                                                 ,'thisother_cost': thisother_cost
                                                ,'data_dict': data_dict
                                            ,'cash_type_list': cash_type_list})

#修改月份資料
def mMonth(request):
    thisdate = fun.getThisdate(request)
    message=''
    cash_type_list = fun.getAllcash_type()
    if 'salary' in request.POST:
        resp_salary = 0 if request.POST['salary'] is None else request.POST['salary']
        resp_bonus = 0 if request.POST['bonus'] is None else request.POST['bonus']
        resp_phone_cost = 0 if request.POST['phone_cost'] is None else request.POST['phone_cost']
        resp_parent_cost = 0 if request.POST['parent_cost'] is None else request.POST['parent_cost']
        resp_common_cost = 0 if request.POST['common_cost'] is None else request.POST['common_cost']
        resp_invest_grow = 0 if request.POST['invest_grow'] is None else request.POST['invest_grow']
        resp_invest_money = 0 if request.POST['invest_money'] is None else request.POST['invest_money']
        #其他收入陣列
        resp_other_income_name=[]
        resp_other_income=[]
        resp_nmonthcash_type_income=[]
        if 'other_income_name' in request.POST:
            resp_other_income_name = request.POST.getlist('other_income_name')
            resp_other_income = request.POST.getlist('other_income')
        #其他支出陣列
        resp_other_cost_name = []
        resp_other_cost = []
        resp_nmonthcash_type_cost = []
        if 'other_cost_name' in request.POST:
            resp_other_cost_name = request.POST.getlist('other_cost_name')
            resp_other_cost = request.POST.getlist('other_cost')
            resp_nmonthcash_type_cost = request.POST.getlist('nmonthcash_type_cost')

        now = fun.getNow()
        resp_created_at = now  # 擷取現在時間
        resp_modify_at = now  # 擷取現在時間

        #計算總投資餘額
        try:
            total_invest = int(months.objects.filter(YM__lt=thisdate).latest('id').total_invest) + int(resp_invest_money)
        except months.DoesNotExist:
            total_invest = resp_invest_money
        #計算本月餘額-收入
        balance = int(resp_salary) + int(resp_bonus)
        for other_income1 in resp_other_income:
            balance = int(balance) + int(other_income1)
        #計算本月餘額-支出
        balance = int(balance) - int(resp_phone_cost) - int(resp_parent_cost) - int(resp_common_cost) - int(resp_invest_grow) - int(resp_invest_money)
        for other_cost1 in resp_other_cost:
            balance = int(balance) - int(other_cost1)

        update_dict ={
            "salary": resp_salary,
            "bonus": resp_bonus,
            "parent_cost": resp_parent_cost,
            "common_cost": resp_common_cost,
            "phone_cost": resp_phone_cost,
            "invest_money": resp_invest_money,
            "invest_grow": resp_invest_grow,
            "total_invest": total_invest,
            "balance": balance,
            "balance1": balance,
            "balance2": 0,
            "total_balance": 0,
            "modify_at": now
        }
        if 'btn_monthmsubmit' in request.POST:
            months.objects.filter(YM=thisdate).update(**update_dict)
            #新增其他支出
            other_cost.objects.filter(YM=thisdate).delete()
            for index,other_cost1 in enumerate(resp_other_cost_name):
                other_cost.objects.create(YM=thisdate,
                                 name=resp_other_cost_name[index],
                                 cost=resp_other_cost[index],
                                 cash_type=resp_nmonthcash_type_cost[index],
                                 created_at=resp_created_at,
                                 modify_at=resp_modify_at)
            #新增其他收入
            other_income.objects.filter(YM=thisdate).delete()
            for index,other_income1 in enumerate(resp_other_income_name):
                other_income.objects.create(YM=thisdate,
                                 name=resp_other_income_name[index],
                                 cost=resp_other_income[index],
                                 created_at=resp_created_at,
                                 modify_at=resp_modify_at)
            message='修改成功'
        elif 'btn_monthmsubmit1' in request.POST:
            months.objects.filter(YM__gte=thisdate).update(**update_dict)
            lastdate = months.objects.filter(YM__gte=thisdate).latest('id').YM
            #新增其他支出
            other_cost.objects.filter(YM__gte=thisdate).delete()
            #新增其他收入
            other_income.objects.filter(YM__gte=thisdate).delete()
            thisdate1 = thisdate
            lastdate = datetime.datetime.strptime(lastdate.split('/')[0]+lastdate.split('/')[1], "%Y%m")
            thisdate1d = datetime.datetime.strptime(thisdate1.split('/')[0]+thisdate1.split('/')[1], "%Y%m")
            while thisdate1d.date()<=lastdate.date():
                for index,other_cost1 in enumerate(resp_other_cost_name):
                    other_cost.objects.create(YM=thisdate1,
                                     name=resp_other_cost_name[index],
                                     cost=resp_other_cost[index],
                                     cash_type=resp_nmonthcash_type_cost[index],
                                     created_at=resp_created_at,
                                     modify_at=resp_modify_at)
                for index,other_income1 in enumerate(resp_other_income_name):
                    other_income.objects.create(YM=thisdate1,
                                     name=resp_other_income_name[index],
                                     cost=resp_other_income[index],
                                     created_at=resp_created_at,
                                     modify_at=resp_modify_at)
                thisdate1 = fun.PreNextMonth1(thisdate1,'next')
                thisdate1d = datetime.datetime.strptime(thisdate1.split('/')[0]+thisdate1.split('/')[1], "%Y%m")
            message='修改成功'

    #取得當月其他收入
    try:
        thisother_income = other_income.objects.filter(YM=thisdate)
    except months.DoesNotExist:
        thisother_income={}
    #取得當月其他支出
    try:
        thisother_cost = other_cost.objects.filter(YM=thisdate)
    except months.DoesNotExist:
        thisother_cost={}
    try:
        month = months.objects.get(YM=thisdate)
        return render(request,'mmonth.html', {'message':message
                                                ,'thisdate': thisdate
                                                ,'month':month
                                                ,'cash_type_list':cash_type_list
                                                ,'thisother_income':thisother_income
                                                ,'thisother_cost':thisother_cost
                                                ,'thispage':'mmonth'})
    except months.DoesNotExist:
        return render(request,
                      'indexnomonth.html', {'message': ''
                                     ,'thisdate': thisdate
                                     ,'thispage': 'mmonth'
                                     })

#投資資產明細
def InvestDetail(request):
    thisdate = fun.getThisdate(request)
    message=''
    invest_type_list = fun.getAllinvest_type()
    invest_type_dict={}
    for invest_type1 in invest_type_list:
        invest_type_dict[invest_type1.name] = invest_type1.cname
    #取得投資資產明細
    try:
        invest_list = invest.objects.all().order_by('-id')
    except months.DoesNotExist:
        invest_list={}
    #找出投資資產最後一筆的總投入金額, 總餘額
    total = fun.getLastinvest_total(thisdate)
    rest = fun.getLastinvest_rest(total)

    if request.method == 'POST':
        #新增投資明細
        if 'cash' in request.POST:
            resp_insertdate = request.POST['insertdate']
            resp_invest_type = request.POST['invest_type']
            resp_cash = request.POST['cash']
            resp_memo = request.POST['memo']
            now = fun.getNow()
            resp_created_at = now  # 擷取現在時間
            resp_modify_at = now  # 擷取現在時間
            #計篹總餘額
            invest_type1 = invest_type_list.get(name=resp_invest_type)
            if invest_type1.pn =='p':
                rest = int(rest) + int(resp_cash)
            else:
                rest = int(rest) - int(resp_cash)
            #新增投資明細資料
            invest.objects.create(datetime=resp_insertdate,
                                 invest_type=resp_invest_type,
                                 cash=resp_cash,
                                 memo=resp_memo,
                                 created_at=resp_created_at,
                                 modify_at=resp_modify_at)
            message='新增成功!'

    return render(request,'invest_detail.html', {'message':message
                                            ,'thisdate': thisdate
                                            ,'thispage': 'investdetail'
                                            ,'insertdate':fun.getDate()
                                            ,'invest_list':invest_list
                                            ,'invest_type_dict':invest_type_dict
                                             ,'total':total
                                             ,'rest':rest
                                            ,'invest_type_list': invest_type_list})

#月份明細
def MonthDetail(request):
    message=''
    thisdate = fun.getThisdate(request)
    #若無本月資料，直接結束並顯示頁面
    try:
        cash_type_list = fun.getAllcash_type()
        cash_type_dict={}
        for cash_type1 in cash_type_list:
            cash_type_dict[cash_type1.name] = cash_type1.cname
        #取得當月月份明細
        try:
            monthly_list = monthly.objects.filter(YM=thisdate).order_by('-id')
        except months.DoesNotExist:
            monthly_list={}
        #先取得總現金, 總信用卡
        total_cash = fun.getLastmonthly_CashTotal(thisdate)
        total_credit = fun.getLastmonthly_CreditTotal(thisdate)
        if request.method == 'POST':
            #新增投資明細
            if 'money' in request.POST:
                resp_insertdate = request.POST['insertdate']
                resp_cash_type = request.POST['cash_type']
                resp_money = request.POST['money']
                resp_memo = request.POST['memo']
                now = fun.getNow()
                resp_created_at = now  # 擷取現在時間
                resp_modify_at = now  # 擷取現在時間
                #計算類型&總和
                if resp_cash_type=='cash':
                    cash = resp_money
                    credit = 0
                    total_cash = int(total_cash) + int(cash)
                else:
                    cash = 0
                    credit = resp_money
                    total_credit = int(total_credit) + int(credit)
                #新增月份明細資料
                monthly.objects.create(datetime=resp_insertdate,
                                     cash_type=resp_cash_type,
                                     cash=cash,
                                     credit=credit,
                                     total_credit=total_credit,
                                     total_cash=total_cash,
                                     memo=resp_memo,
                                     YM=thisdate,
                                     created_at=resp_created_at,
                                     modify_at=resp_modify_at)
                message='新增成功!'
        thismonths = months.objects.filter(YM=thisdate)
        common_cost = thismonths.latest('id').common_cost #取得本月零用金
        rcommon_cost = int(common_cost)- int(total_cash) - int(total_credit) #計算零用金餘額

        #更新月份餘額
        balance1 = thismonths.latest('id').balance
        if rcommon_cost < 0:
           balance1 = int(balance1) + int(rcommon_cost)
           thismonths.update(balance1=balance1)

        return render(request,'month_detail.html', {'message':message
                                                ,'thisdate': thisdate
                                                ,'insertdate':fun.getDate()
                                                ,'cash_type_list':cash_type_list
                                                ,'cash_type_dict':cash_type_dict
                                                ,'monthly_list':monthly_list
                                                ,'total_cash':total_cash
                                                ,'total_credit':total_credit
                                                ,'common_cost':common_cost
                                                ,'rcommon_cost':rcommon_cost
                                                ,'thispage': 'monthdetail'})
    except months.DoesNotExist:
        return render(request,
                      'indexnomonth.html', {'message': ''
                                     ,'thisdate': thisdate
                                     ,'thispage': 'monthdetail'
                                     })