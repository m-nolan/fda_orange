from models import *

import datetime

from flask import Flask
from flask import g
from flask import redirect
from flask import request
from flask import session
from flask import url_for, abort, render_template, flash
from functools import wraps
from hashlib import md5

app = Flask(__name__)
app.config.from_object(__name__)

database = SqliteDatabase('.\fda_orange.db')

def create_tables():
    with database:
        database.create_tables([Exclusivity, Patent, Product])

@app.before_request
def before_request():
    g.db = database
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response

# application methods from peeweedb example app
def object_list(template_name, qr, var_name='object_list', **kwargs):
    kwargs.update(
        page=int(request.args.get('page', 1)),
        pages=qr.count() / 20 + 1)
    kwargs[var_name] = qr.paginate(kwargs['page'])
    return render_template(template_name, **kwargs)

def object_list(template_name, qr, var_name='object_list', **kwargs):
    kwargs.update(
        page=int(request.args.get('page', 1)),
        pages=qr.count() / 20 + 1)
    kwargs[var_name] = qr.paginate(kwargs['page'])
    return render_template(template_name, **kwargs)

def get_object_or_404(model, *expressions):
    try:
        return model.get(*expressions)
    except model.DoesNotExist:
        abort(404)

@app.route('/')
def homepage():
    # TODO: make session control to view different tables
    return exclusivity_table()
    # if session.table_idx == 0:
    #     exclusivity_table()
    # elif session.table_idx == 1:
    #     patent_table()
    # elif session.table_idx == 2:
    #     product_table()
    # else:
    #     raise ValueError(f'Table index out of range: {session.table_idx}, should be 0, 1, 2.')
    
@app.route('/exclusivity/')
def exclusivity_table():
    exclusivity = Exclusivity.select().order_by(Exclusivity.exclusivity_date.desc())
    return object_list('exclusivity.html', exclusivity, 'exclusivity_list')

@app.route('/patent/')
def patent_table():
    patent = Patent.select().order_by(Patent.submission_date.desc())
    return object_list('patent.html', patent, 'patent_list')

@app.route('/product/')
def product_table():
    product = Product.select().order_by(Product.approval_date.desc())
    return object_list('product.html', product, 'product_list')

if __name__ == "__main__":
    # session.table_idx = 0
    create_tables()
    app.run()