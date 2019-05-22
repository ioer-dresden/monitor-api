# -*- coding: utf-8 -*-
from flask import render_template, jsonify
from flask_login import LoginManager, login_required

from app import app
from app.admin import admin
from app.admin.services.OgcFactory import OgcFactory
from app.user.models.Forms import *
from app.user.models.User import *

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
    #local_path = 'G:\\mapsrv_daten\\detailviewer\\wfs_mapfiles'
    wfs = OgcFactory()
    return jsonify(wfs.create_service("wfs").createAllServices())

@admin.route('/wcs',methods=['POST'])
@login_required
def wcs_service():
    #local_path = 'G:\\mapsrv_daten\\detailviewer\\wcs_mapfiles'
    wcs = OgcFactory()
    return jsonify(wcs.create_service("wcs").createAllServices())

@admin.route('/wms',methods=['POST'])
@login_required
def wms_service():
    #local_path = 'G:\\mapsrv_daten\\detailviewer\\wms_mapfiles'
    wms = OgcFactory()
    return jsonify(wms.create_service("wms").createAllServices())
