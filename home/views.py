# coding=utf-8
from django.shortcuts import render
from months.models import *
from django.forms.models import model_to_dict
from django.http import HttpResponse
import datetime, time
from function import fun #方法集合

# Create your views here.
def Home(request):
    thisdate = fun.getThisdate(request)
    try:
        thismonth = months.objects.get(YM=thisdate)
        #找出投資資產最後一筆的總投入金額, 總餘額
        invest_total = fun.getLastinvest_total(thisdate)
        invest_rest = fun.getLastinvest_rest(invest_total)

        cash_type_list = fun.getAllcash_type()

        cash_type_dict={}
        for cash_type1 in cash_type_list:
            cash_type_dict[cash_type1.name] = cash_type1.cname

        total_cost=0 #總月繳金額
        total_tcost=0 #總分期金額
        total_rcost=0 #總未到期本金

        #取得當月短期固定成本
        fixed_short_cost_list = fun.getShortCost(thisdate)
        for thefixed_short_cost in fixed_short_cost_list:
            total_cost = total_cost + int(thefixed_short_cost.cost)
            total_tcost = total_tcost + int(thefixed_short_cost.total_cost)
            total_rcost = total_rcost + int(thefixed_short_cost.rent_cost)
        #取得當月其他收入
        try:
            thisother_income = other_income.objects.filter(YM=thisdate)
        except other_income.DoesNotExist:
            thisother_income={}
        #取得當月其他支出
        try:
            thisother_cost = other_cost.objects.filter(YM=thisdate)
        except other_cost.DoesNotExist:
            thisother_cost={}
        #取得信用卡總結
        credit_total_dict = fun.getThisMonthCreditSummery(thisdate,fixed_short_cost_list)
        #計算零用金餘額
        total_cash = fun.getLastmonthly_CashTotal(thisdate)
        total_credit = fun.getLastmonthly_CreditTotal(thisdate)
        rcommon_cost = int(thismonth.common_cost)- int(total_cash) - int(total_credit) #計算零用金餘額
        #更新月份餘額balance2與本月結餘
        thismonths = months.objects.filter(YM=thisdate)
        #更新月份餘額
        balance2 = thismonths.latest('id').balance2
        balance2 = int(thismonths.latest('id').balance1) - int(total_cost)
        thismonths.update(balance2=balance2)
        #更新本月結餘
        total_balance = thismonths.latest('id').total_balance
        predate = fun.PreYM(thisdate)
        try:
            pretotal_balance = months.objects.get(YM=predate).total_balance
        except months.DoesNotExist:
            pretotal_balance = 0
        total_balance = int(balance2) + int(pretotal_balance)
        thismonths.update(total_balance=total_balance)
        #總可用金 (零用金可用餘額+本月總存款結餘)
        if rcommon_cost > 0:
            thismonth_balance = int(total_balance) + int(rcommon_cost)
        else:
            thismonth_balance = total_balance
        #資產總結
        alltotal = int(invest_rest) + int(thismonth_balance) - int(total_rcost)

        return render(request,
                      'index.html', {'message': ''
                                     ,'fixed_short_cost_list': fixed_short_cost_list
                                     ,'cash_type_dict': cash_type_dict
                                     ,'total_cost': total_cost
                                     ,'total_tcost': total_tcost
                                     ,'total_rcost': total_rcost
                                     ,'thisdate': thisdate
                                     ,'thismonth': thismonth
                                     ,'thisother_income': thisother_income
                                     ,'thisother_cost': thisother_cost
                                     ,'invest_total': invest_total
                                     ,'invest_rest': invest_rest
                                     ,'cash_type_list_nocash': cash_type_list.exclude(name='cash')
                                     ,'credit_total_dict': credit_total_dict
                                     ,'rcommon_cost': rcommon_cost
                                     ,'balance2': balance2
                                     ,'total_balance': total_balance
                                     ,'thismonth_balance': thismonth_balance
                                     ,'alltotal': alltotal
                                     ,'thispage': ''
                                     })
    except months.DoesNotExist:
        return render(request,
                      'indexnomonth.html', {'message': ''
                                     ,'thisdate': thisdate
                                     ,'thispage': ''
                                     })
