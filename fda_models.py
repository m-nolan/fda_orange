from peewee import *

database = SqliteDatabase('.\fda_orange.db')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Exclusivity(BaseModel):
    appl_no = IntegerField(column_name='Appl_No', null=True)
    appl_type = TextField(column_name='Appl_Type', null=True)
    exclusivity_code = TextField(column_name='Exclusivity_Code', null=True)
    exclusivity_date = TextField(column_name='Exclusivity_Date', null=True)
    product_no = IntegerField(column_name='Product_No', null=True)
    index = IntegerField(index=True, null=True)

    class Meta:
        table_name = 'exclusivity'
        primary_key = False

class Patent(BaseModel):
    appl_no = IntegerField(column_name='Appl_No', null=True)
    appl_type = TextField(column_name='Appl_Type', null=True)
    delist_flag = TextField(column_name='Delist_Flag', null=True)
    drug_product_flag = TextField(column_name='Drug_Product_Flag', null=True)
    drug_substance_flag = TextField(column_name='Drug_Substance_Flag', null=True)
    patent_expire_date_text = TextField(column_name='Patent_Expire_Date_Text', null=True)
    patent_no = TextField(column_name='Patent_No', null=True)
    patent_use_code = TextField(column_name='Patent_Use_Code', null=True)
    product_no = IntegerField(column_name='Product_No', null=True)
    submission_date = TextField(column_name='Submission_Date', null=True)
    index = IntegerField(index=True, null=True)

    class Meta:
        table_name = 'patent'
        primary_key = False

class Products(BaseModel):
    appl_no = IntegerField(column_name='Appl_No', null=True)
    appl_type = TextField(column_name='Appl_Type', null=True)
    applicant = TextField(column_name='Applicant', null=True)
    applicant_full_name = TextField(column_name='Applicant_Full_Name', null=True)
    approval_date = TextField(column_name='Approval_Date', null=True)
    delivery_format = TextField(column_name='Delivery_Format', null=True)
    ingredient = TextField(column_name='Ingredient', null=True)
    product_no = IntegerField(column_name='Product_No', null=True)
    rld = TextField(column_name='RLD', null=True)
    rs = TextField(column_name='RS', null=True)
    route = TextField(column_name='Route', null=True)
    strength = TextField(column_name='Strength', null=True)
    te_code = TextField(column_name='TE_Code', null=True)
    trade_name = TextField(column_name='Trade_Name', null=True)
    type = TextField(column_name='Type', null=True)
    index = IntegerField(index=True, null=True)

    class Meta:
        table_name = 'products'
        primary_key = False

