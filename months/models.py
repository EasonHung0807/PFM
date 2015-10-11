# coding=utf-8
from django.db import models


# Create your models here.
# 月份資料
class months(models.Model):
    YM = models.TextField(blank=True, null=True)  # 年月
    salary = models.TextField(blank=True, null=True)  # 薪資
    bonus = models.TextField(blank=True, null=True)  # 獎金
    parent_cost = models.TextField(blank=True, null=True)  # 孝親費
    phone_cost = models.TextField(blank=True, null=True)  # 通信費
    common_cost = models.TextField(blank=True, null=True)  # 零用金
    invest_money = models.TextField(blank=True, null=True)  # 投資成本
    invest_grow = models.TextField(blank=True, null=True)  # 自我成長(買書 補習等自我投資)
    balance = models.TextField(blank=True, null=True)  # 本月餘額(本月收入-本月支出)(不包括月份明細、信用卡支出))
    balance1 = models.TextField(blank=True, null=True)  # 本月餘額(本月收入-本月支出(不包括信用卡支出))
    balance2 = models.TextField(blank=True, null=True)  # 本月餘額(本月收入-本月支出
    total_balance = models.TextField(blank=True, null=True)  # 總存款結餘(本月餘額-前月總存款結餘)
    total_invest = models.TextField(blank=True, null=True)  # 總投資成本
    created_at = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    modify_at = models.DateTimeField(blank=True, null=True,auto_now=True)

# 月份明細
class monthly(models.Model):
    YM = models.TextField(blank=True, null=True)  # 年月
    cash = models.TextField(blank=True, null=True)  # 現金提領
    total_cash = models.TextField(blank=True, null=True)  # 總現金提領
    credit = models.TextField(blank=True, null=True)  # 信用卡
    total_credit = models.TextField(blank=True, null=True)  # 總信用卡
    cash_type = models.TextField(blank=True, null=True)  # 信用卡銀行
    memo = models.TextField(blank=True, null=True)  # 備註
    datetime = models.TextField(blank=True, null=True)  # 新增日期
    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)


# 信用卡銀行
class cash_type(models.Model):
    name = models.TextField()  # 名稱
    cname = models.TextField()  # 中文名稱
    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)


# 其他收入
class other_income(models.Model):
    YM = models.TextField()  # 年月
    name = models.TextField()  # 名稱
    cost = models.TextField()  # 費用
    memo = models.TextField()  # 備註
    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)


# 短期固定成本
class fixed_short_cost(models.Model):
    name = models.TextField(blank=True, null=True)  # 名稱
    cost = models.TextField(blank=True, null=True)  # 費用
    total_cost = models.TextField(blank=True, null=True)  # 總費用
    cash_type = models.TextField(blank=True, null=True)  # 信用卡銀行
    start_date = models.TextField(blank=True, null=True)  # 起始日
    end_date = models.TextField(blank=True, null=True)  # 到期日
    memo = models.TextField(blank=True, null=True)  # 備註
    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)
    total_num =  models.TextField(blank=True, null=True)  # 總期數
    first_cost =  models.TextField(blank=True, null=True)  # 首月費用 分期若除不進可能首月錢會多一點

# 短期固定成本_每月資料
class fixed_short_cost1(models.Model):
    YM = models.TextField(blank=True, null=True)  # 年月
    name = models.TextField(blank=True, null=True)  # 名稱
    cost = models.TextField(blank=True, null=True)  # 費用
    short_costid = models.TextField(blank=True, null=True)  # 短期固定成本id
    memo = models.TextField(blank=True, null=True)  # 備註
    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)
    rent_cost = models.TextField(blank=True, null=True)  # 剩餘費用
    rent_num =  models.TextField(blank=True, null=True)  # 未到期期數

# 其他成本
class other_cost(models.Model):
    YM = models.TextField()  # 年月
    name = models.TextField()  # 名稱
    cost = models.TextField()  # 費用
    cash_type = models.TextField()  # 信用卡銀行
    memo = models.TextField()  # 備註
    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

#投資資產總結
class invest(models.Model):
    datetime = models.TextField(blank=True, null=True)  # 日期
    invest_type = models.TextField(blank=True, null=True)  # 類別
    cash = models.TextField(blank=True, null=True)  # 費用
    memo = models.TextField(blank=True, null=True)  # 備註
    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

#投資資產項目
class invest_type(models.Model):
    name = models.TextField(blank=True, null=True)  # 名稱
    cname = models.TextField(blank=True, null=True)  # 中文名稱
    pn = models.TextField(blank=True, null=True)  # 正負
    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)
