# Add libraries here

class Project(db.Model):
    __tablename__ = "project"

    sales_order= db.column(db.Integer, primary_key = True)
    customer_name = db.column(db.String)
    so_desc = db.column(db.String)
    so_date = db.column(db.Date)
    exp_ship_date = db.column(db.Date)
    nps_sales_contact = db.column(db.String)
    ship_addy = db.column(db.String)
    ship_city = db.column(db.String)
    ship_state = db.column(db.String)
    ship_country = db.column(db.String)
    ship_zip = db.column(db.String)
    inspect_date = db.column(db.Date)
    inspect_tech = db.column(db.String)
    act_ship_date = db.column(db.Date)
    ship_style = db.column(db.String)

class Unit(db.Model):
    __tablename__ = 'unit'

    unit_sn = db.Column(db.Integer, primary_key=True)
    sales_order= db.Column(db.Integer)
    model  = db.Column(db.String())

    def __init__(self, sales_order, model):
        self.unit_sn = unit_sn
        self.sales_order = sales_order
        self.model = model
