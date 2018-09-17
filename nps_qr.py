from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, IntegerField, validators

nps_qr = Flask(__name__)
nps_qr.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:Swingline5!@localhost:5432/nps_qr'
nps_qr.secret_key = b'testkey5!'
db = SQLAlchemy(nps_qr)
db.create_all()
app_name = "NPS QR"


"""

MODELS -->  Needs to be moved to its own file/folder eventually
"""
class User(db.Model):
    __tablename__ = 'nps_user'

    user_id = db.Column(db.Integer, primary_key=True)
    email= db.Column(db.String)
    f_name  = db.Column(db.String)
    l_name = db.Column(db.String)

    def __init__(self, user_id, email, f_name, l_name):
        self.user_id = user_id
        self.email = email
        self.f_name = f_name
        self.l_name - l_name

class Unit(db.Model):
    __tablename__ = 'unit'

    unit_sn = db.Column(db.Integer, primary_key=True)
    sales_order= db.Column(db.Integer)
    model  = db.Column(db.String)
    date_code = db.Column(db.String)
    comm_type = db.Column(db.Integer)
    qa_tech = db.Column(db.Integer)
    mc_sn = db.Column(db.String)
    bl_ver = db.Column(db.String)
    fw_ver = db.Column(db.String)

    def __init__(self, unit_sn, sales_order, model, date_code, comm_type, user_id, mc_sn, bl_ver, fw_ver):
        self.unit_sn = unit_sn
        self.sales_order = sales_order
        self.model = model
        self.date_code = date_code
        self.comm_type = comm_type
        self.qa_tech = qa_tech
        self.mc_sn = mc_sn
        self.bl_ver = bl_ver
        self.fw_ver = fw_ver


class Project(db.Model):
    __tablename__ = 'project'

    sales_order= db.Column(db.Integer, primary_key=True)
    so_desc  = db.Column(db.String)
    so_date = db.Column(db.Date)
    exp_ship = db.Column(db.Date)
    nps_contact = db.Column(db.Integer)
    ship_city = db.Column(db.String)
    ship_state = db.Column(db.String)
    ship_addy = db.Column(db.String)
    ship_zip = db.Column(db.String)
    ship_date =  db.Column(db.Date)
    ship_inspector = db.Column(db.String)
    ship_country = db.Column(db.String)
    customer = db.Column(db.String)
    ship_inspect_date =  db.Column(db.Date)
    ship_style = db.Column(db.String)



    def __init__(self, sales_order, so_desc, so_date, exp_ship, nps_contact,
                ship_city,ship_state, ship_addy, ship_zip, ship_date,
                ship_inspector, ship_country, customer, ship_inspect_date):
        self.sales_order = sales_order
        self.so_desc = so_desc
        self.so_date = so_date
        self.exp_ship = exp_ship
        self.nps_contact = nps_contact
        self.ship_city= ship_city
        self.ship_state = ship_state
        self.ship_addy = ship_addy
        self.ship_zip = ship_zip
        self.ship_date = ship_date
        self.ship_inspector = ship_inspector
        self.ship_country = ship_country
        self.customer = customer
        self.ship_inspect_date = ship_inspect_date
        self.ship_style = ship_style


class Nch(db.Model):
    __tablename__ = 'nch'

    unit_sn = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.Integer)
    http_url  = db.Column(db.String)
    config_network = db.Column(db.String)
    wifi_pass = db.Column(db.Integer)
    web_pass = db.Column(db.Integer)
    eth0_mac = db.Column(db.String)
    eth1_mac = db.Column(db.String)
    br0_mac = db.Column(db.String)
    wlan0_mac = db.Column(db.String)
    usb_network = db.Column(db.String)
    nch_ver = db.Column(db.String)

    def __init__(self, unit_sn, hostname, http_url, config_network, wifi_pass, web_pass, eth0_mac, eth1_mac, bl_ver, fw_ver):
        self.unit_sn = unit_sn
        self.hostname = hostname
        self.http_url = http_url
        self.config_network = config_network
        self.wifi_pass = wifi_pass
        self.web_pass = web_pass
        self.eth0_mac = eth0_mac
        self.eth1_mac = eth1_mac
        self.bl_ver = bl_ver
        self.fw_ver = fw_ver

class Six_low(db.Model):
    __tablename__ = 'six_low'

    unit_sn = db.Column(db.Integer, primary_key=True)
    six_ch = db.Column(db.Integer)
    six_mac  = db.Column(db.String)

    def __init__(self, unit_sn, six_ch, six_mac):
        self.unit_sn = unit_sn
        self.six_ch = six_ch
        self.six_mac = six_mac

"""

FORMS -->  Needs to be moved to its own file/folder eventually
"""

class New_Unit_Form(Form):
    unit_sn = IntegerField('Unit Serial Number')
    sales_order = IntegerField('Sales Order Number')
    model = StringField('Model')


"""

VIEWS -->  Break out into separate files
"""
# Homepage
@nps_qr.route('/')
def home():
    return "Welcome to the Thunderdome, bitch."

# Create a new user
@nps_qr.route('/new_user', methods=['GET', 'POST'])
def new_user():
    form = New_User_Form(request.form)
    if request.method == 'POST':
        unit = Unit(form.unit_sn.data, form.sales_order.data,
                    form.model.data)
        db.session.add(unit)
        db.session.commit()
        return redirect(url_for('units'))
    return render_template('new_unit.html', form=form)

@nps_qr.route('/users')
def users():
    units=User.query.all()
    return render_template('units.html', units=units)

# Update existing unit
@nps_qr.route('/edit_unit', methods=['GET', 'POST'])
def edit_unit():
    edit_form = New_Unit_Form(request.form)
    unit = str(Unit.query.get(unit_sn))
    # if request.method =='POST':
    return render_template('edit_unit.html', unit=unit)


# Create a new unit
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

@nps_qr.route('/units')
def units():
    units=Unit.query.all()
    return jsonify(units)
    # return jsonify(render_template('units.html', units=units))

"""
# Update existing unit
@nps_qr.route('/edit_unit', methods=['GET', 'POST'])
def edit_unit():
    edit_form = New_Unit_Form(request.form)
    unit = str(Unit.query.get(unit_sn))
    # if request.method =='POST':
    return render_template('edit_unit.html', unit=unit)
"""

@nps_qr.route('/projects')
def projects():
    projects=Project.query.all()
    return render_template('projects.html', projects=projects)

@nps_qr.route('/comms')
def comms():
    comms = Communication.query.all()
    return render_template('comms.html', comms=comms)


class UnitSearch(Form):
    unit_sn = IntegerField('Unit SN')

@nps_qr.route('/unit_search', methods=['GET', 'POST'])
def unit_search():
    search_form = UnitSearch(request.form)
    if request.method == 'POST':
        unit_sn_search_value = search_form.unit_sn.data
        units_found = Unit.query.filter_by(unit_sn=unit_sn_search_value).all()
        return render_template('unit_search_results.html', unit_sn_search_value =  unit_sn_search_value, units_found = units_found)
    return render_template('unit_search.html', search_form = search_form)

# Need to figure out how to change route after 'POST'ing the search user_id_search_value
"""
@fitfort.route('/ex_search_results')
def ex_search_results():
    test = ex_search(ex_id_search_value)
    return test
    #return render_template('ex_search_results.html', exs_found=exs_found, ex_id_search_value=ex_id_search_value)

"""
"""
@.route('/new_facility', methods=['GET', 'POST'])
def new_facility():
    form = Facility_Form(request.form)
    if request.method == 'POST':
        facility = Facility(form.fac_id.data, form.fac_name.data,
                    form.fac_addy.data, form.fac_zip.data,
                    form.fac_city.data, form.fac_state.data, form.fac_country.data)
        db.session.add(facility)
        db.session.commit()
        return redirect(url_for('facilities'))
    return render_template('new_facility.html', form=form)

class New_Unit(Form):
    unit_id = IntegerField ('Unit_ID', [validators.Length(min=4, max=25)])
    sales_order = IntegerField('Sales Order'', [validators.Length(min=6, max=35)])
    model = StringField('Model'   ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
"""

# Units
# Unit DB Define and __init__
# Unit forms
# Unit-related paths
"""
class Unit(db.Model):
    __tablename__ = 'unit'

    unit_sn = db.Column('unit_sn', db.Integer)
    date_code = db.Column('date_code', db.String())
    model = db.Column('model',db.String())
    comm_type = db.Column('comm_type', db.String())
    qa_user= db.Column('qa_user',db.String())
    sales_order= db.Column('sales_order', db.String())
    mc_sn  = db.Column('mc_sn', db.String())

    def __init__(self, unit_sn, date_code, model, comm_type, qa_user, sales_order, mc_sn):
        self.unit_sn = unit_sn
        self.date_code = date_code
        self.model = model
        self.comm_type = comm_type
        self.qa_user = qa_user
        self.sales_order = sales_order
        self.mc_sn = mc_sn


# Projects
# Project DB Define and __init__
# Project form
# Project-related paths

class Project(db.Model):
    __tablename__ = 'project'

    sales_order = db.Column('sales_order', db.Integer)
    so_desc = db.Column('so_desc', db.String())
    date = db.Column('date',db.String())
    exp_ship = db.Column('exp_ship', db.String())
    sales_rep   db.Column('sales_rep',db.String())
    ship_addy  = db.Column('ship_add', db.String())
    ship_city
    ship_state
    ship_country
    customer
    ship_inspect_date =
    ship_style =
    ship_zip
    act_ship
    ship_inspector

    sales_order= db.Column('sales_order', db.String())
    mc_sn  = db.Column('mc_sn', db.String())

    def __init__(self, unit_sn, date_code, model, comm_type, qa_user, sales_order, mc_sn):
        self.unit_sn = unit_sn
        self.date_code = date_code
        self.model = model
        self.comm_type = comm_type
        self.qa_user = qa_user
        self.sales_order = sales_order
        self.mc_sn = mc_sn

# Communications
# Comm DB Define and __init__
# Comm forms
# Comm-related paths

class Unit(db.Model):
    __tablename__ = 'unit'
    unit_sn = db.Column('UNIT_SN', db.Integer)
    date_code = db.Column('DATE_CODE', db.String())
    model = db.Column('MODEL',db.String())
    comm_type = db.Column(db.String())
    QA_USER = db.Column(db.String())
    SALES_ORDER= db.Column(db.String())
    MC_SN  = db.Column(db.String())

    def __init__(self, UNIT_SN, DATE_CODE, MODEL, COMM_TYPE, QA_USER, SALES_ORDER, MC_SN):
        self.UNIT_SN = UNIT_SN
        self.DATE_CODE = DATE_CODE
        self.MODEL = MODEL
        self.COMM_TYPE = COMM_TYPE
        self.QA_USER = QA_USER
        self.SALES_ORDER = SALES_ORDER
        self.MC_SN = MC_SN


class New_Unit_Form(FlaskForm):
    UNIT_SN = StringField('UNIT_SN', validators=[DataRequired()])
    DATE_CODE = StringField('DATE_CODE', validators=[DataRequired()])
    MODEL = StringField('MODEL', validators=[DataRequired()])
    COMM_TYPE = StringField('COMM_TYPE', validators=[DataRequired()])
    QA_USER = StringField('QA_USER', validators=[DataRequired()])
    SALES_ORDER= StringField('SALES_ORDER', validators=[DataRequired()])
    MC_SN  = StringField('MC_SN', validators=[DataRequired()])
    submit = SubmitField('Enter Unit')

    def add_new_unit(request):
        form = New_Unit_Form(request.POST)
        if request.method == 'POST' and form.validate():
            new_unit = Unit()
            new_unit.UNIT_SN = form.UNIT_SN.data
            new_unit.DATE_CODE = form.DATE_CODE.data
            new_unit.MODEL = form.MODEL.data
            new_unit.COMM_TYPE = form.COMM_TYPE.data
            new_unit.QA_USER = form.QA_USER.data
            new_unit.SALES_ORDER = form.SALES_ORDER.data
            new_unit.MC_SN = form.MC_SN.data
            new_unit.save()
            redirect('register')
            return render_response('unit.html', form=form)

# Home page
@nps_qr.route('/')
def home():
    # Redirect to dashboard if recognized user, redirect to login page if user isn't recognized
    return render_template('login.html', app_name=app_name)

# Login page
@nps_qr.route('/login')
def login():
    #sign up
    return render_template('login.html', app_name=app_name)

# Sign up page
@nps_qr.route('/signup')
def sign_up():
    return render_template('signup.html', app_name=app_name)

# User dashboard
@nps_qr.route('/dashboard/<username>')
def dashboard():
    return render_template('dashboard.html', app_name=app_name, username = username)

# Search menu
@nps_qr.route('/search')
def search():
    return render_template('search.html', app_name=app_name, username = username)

# Profile Page
@nps_qr.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', app_name = app_name, username=username)

# Used to test DB connection and Display
@nps_qr.route('/unit')
def unit():
    unit = Unit.query.all()
    return render_template('unit.html', unit = unit)

@nps_qr.route('/new_unit', methods=['POST'])
def new_unit():
    form=NEW_

# Used to test wtforms
@nps_qr.route('/form_test')
def form_test():
    form = New_Unit_Form()
    return render_template('formtest.html', form=form)



@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text




# Should be a list sorted based on expected ship date
@nps_qr.route('/project_schedule')
def project_schedule():
    return render_template('project_schedule.html')
"""

# If the app is called from cmd, run it
if __name__ == '__main__':
    nps_qr.run(debug=True)
