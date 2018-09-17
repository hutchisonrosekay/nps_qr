# Add libraries here

class New_Project_Form(Form):
    sales_order = IntegerField('Sales Order Number')
    customer_name = StringField('Customer Name')
    so_desc = StringField('SO Description')
    so_date = DateField('SO Creation Date')
    exp_ship_date = DateField('Expected Ship Date')
    nps_sales_contact = StringField('NPS Sales Contact')
    ship_addy = StringField('Ship to Address')
    ship_city = StringField('Ship to City')
    ship_state = StringField('Ship to State')
    ship_country = StringField('Shipt to Country')
    ship_zip = StringField('Ship to Zip')
    inspect_date = DateField('Inspection Date')
    inspect_tech = StringField('Shipment Inspector')
    act_ship_date = DateField('Actual ship date')
    ship_style = StringField('Shipment Style')

class Update_Project_Form(Form):
    sales_order = IntegerField('Sales Order Number')
    customer_name = StringField('Customer Name')
    so_desc = StringField('SO Description')
    so_date = DateField('SO Creation Date')
    exp_ship_date = DateField('Expected Ship Date')
    nps_sales_contact = StringField('NPS Sales Contact')
    ship_addy = StringField('Ship to Address')
    ship_city = StringField('Ship to City')
    ship_state = StringField('Ship to State')
    ship_country = StringField('Shipt to Country')
    ship_zip = StringField('Ship to Zip')
    inspect_date = DateField('Inspection Date')
    inspect_tech = StringField('Shipment Inspector')
    act_ship_date = DateField('Actual ship date')
    ship_style = StringField('Shipment Style')

class New_Unit__Form(Form):
    unit_sn = IntegerField('Unit Serial Number')
    date_made = DateField('Date Made')
    model = StringField('Model')
    comm_type = IntegerField('Communication Type')
    qa_inspector = StringField('Quality Assurance Inspector')
    sales_order = IntegerField('Sales Order Number')
    mc_sn = StringField('Master Controller Serial Number')

class Update_Unit__Form(Form):
    unit_sn = IntegerField('Unit Serial Number')
    date_made = DateField('Date Made')
    model = StringField('Model')
    comm_type = IntegerField('Communication Type')
    qa_inspector = StringField('Quality Assurance Inspector')
    sales_order = IntegerField('Sales Order Number')
    mc_sn = StringField('Master Controller Serial Number')

class New_Comm_Form_Six(Form):
        unit_sn = IntegerField('Unit Serial Number')
        comm_type = IntegerField()
        wifi_mac = StringField('Sales Order Number')
        wifi_ch = IntegerField('Model')

class Update_Comm_Form_Six(Form):
        unit_sn = IntegerField('Unit Serial Number')
        comm_type = IntegerField()
        wifi_mac = StringField('Sales Order Number')
        wifi_ch = IntegerField('Model')

class New_Comm_Form_NCH(Form):
        unit_sn = IntegerField('Unit Serial Number')
        comm_type = IntegerField()
        nch_sn = IntegerField('Sales Order Number')
        nch_ip = StringField('Model')
        nch_ver = StringField('NCH Version')
        nch_netmask = StringField('NCH Netmask Address')
        bss_ver = StringField('BACnet System Version')
        bs_ver = StringField('BACnet Version')
        ethernet_mac = StringField('Ethernet Mac Address')

class Update_Comm_Form_NCH(Form):
        unit_sn = IntegerField('Unit Serial Number')
        comm_type = IntegerField()
        nch_sn = IntegerField('Sales Order Number')
        nch_ip = StringField('Model')
        nch_ver = StringField('NCH Version')
        nch_netmask = StringField('NCH Netmask Address')
        bss_ver = StringField('BACnet System Version')
        bs_ver = StringField('BACnet Version')
        ethernet_mac = StringField('Ethernet Mac Address')
