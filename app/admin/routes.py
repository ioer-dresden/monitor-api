# -*- coding: utf-8 -*-
from flask import render_template, jsonify
from flask_login import LoginManager, login_required
from app.admin import admin
from app import app
from app.user.models.Users import *
from app.admin.services.Wfs import Wfs
from app.admin.services.Wcs import Wcs
from app.admin.services.Wms import Wms
from app.user.models.Forms import *

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized():
    form = RegisterForm(form_type="inline")
    return render_template('user/signup.html', form=form)

@admin.route('/')
@login_required
def admin_page():
    return render_template("admin/index.html")

@admin.route('/wfs',methods=['GET', 'POST'])
@login_required
def wfs_service():
    #wfs = Wfs('G:\\mapsrv_daten\\detailviewer\\wfs_mapfiles')
    wfs = Wfs()
    return jsonify(wfs.createAllServices())

@admin.route('/wcs',methods=['POST'])
@login_required
def wcs_service():
    #wcs = Wcs('G:\\mapsrv_daten\\detailviewer\\wcs_mapfiles')
    wcs = Wcs()
    return jsonify(wcs.createAllServices())

@admin.route('/wms',methods=['POST'])
@login_required
def wms_service():
    #wms = Wms('G:\\mapsrv_daten\\detailviewer\\wms_mapfiles')
    wms = Wms()
    return jsonify(wms.createAllServices())

