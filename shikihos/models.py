from django.db import models

# Create your models here.
class Shikiho(models.Model):
    year = models.IntegerField(null=True)
    quarter = models.IntegerField(null=True)
    code = models.IntegerField(null=True)
    comp_name = models.TextField(null=True)
    url = models.TextField(null=True)
    feature = models.TextField(null=True)
    topic = models.TextField(null=True)
    outlook = models.TextField(null=True)
    next_sales = models.IntegerField(null=True)
    next_operationg_income = models.IntegerField(null=True)
    next_ordinary_income = models.IntegerField(null=True)
    next_net_income = models.IntegerField(null=True)
    next_net_income_per_share = models.TextField(null=True)
    next_dividend = models.TextField(null=True)
    prev_sales = models.IntegerField(null=True)
    prev_operating_income = models.IntegerField(null=True)
    prev_ordinary_income = models.IntegerField(null=True)
    prev_net_income = models.IntegerField(null=True)
    prev_net_income_per_share = models.TextField(null=True)
    prev_dividend = models.TextField(null=True)
    operationg_cf = models.IntegerField(null=True)
    prev_operating_cf = models.IntegerField(null=True)
    investment_cf = models.IntegerField(null=True)
    prev_investment_cf = models.IntegerField(null=True)
    financing_cf = models.IntegerField(null=True)
    prev_financing_cf = models.IntegerField(null=True)
    cash = models.IntegerField(null=True)
    prev_cash = models.IntegerField(null=True)
    total_assets = models.IntegerField(null=True)
    owned_capital = models.IntegerField(null=True)
    owned_capital_ratio = models.TextField(null=True)
    capital = models.IntegerField(null=True)
    retained_earnings = models.IntegerField(null=True)
    interest_bearing_debt = models.IntegerField(null=True)
    establishment = models.TextField(null=True)
    stock_listing = models.TextField(null=True)
    settlement = models.TextField(null=True)
    type_of_business = models.TextField(null=True)
    supplier = models.TextField(null=True)
    num_of_employee = models.TextField(null=True)
    head_office = models.TextField(null=True)
    compare_company = models.TextField(null=True)
    certificate = models.TextField(null=True)
    sales_contact = models.TextField(null=True)
    consolidated = models.TextField(null=True)
    consolidated_business = models.TextField(null=True)
    bank = models.TextField(null=True)
