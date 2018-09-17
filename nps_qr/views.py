from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, IntegerField, validators

"""
@nps_qr.route('/new_unit', methods=['GET', 'POST'])
def new_unit():
    form = New_Unit_Form(request.form)
    if request.method == 'POST':
        unit = Unit(form.unit_sn.data, form.sales_order.data,
                    form.model.data)
        db.session.add(unit)
        db.session.commit()
        return redirect(url_for('units'))
    return render_template('new_unit.html', form=form)
"""

@nps_qr.route('/')
def home():
    return 'Welcome to the Nextek Power System.  This is the home page.'

@nps_qr.route('/new_unit')
def new_unit():
    return 'New unit form'

@nps_qr.route('/unit/<unit#>')
def project_view():
    return 'Unit View (Traveler Tag)'

@nps_qr.route('/new_project')
def new_project():
    return 'New project form'

@nps_qr.route('/project/<project#>')
def project_view():
    return 'Unit View (Traveler Tag)'
