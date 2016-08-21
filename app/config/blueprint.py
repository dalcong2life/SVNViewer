# -*- coding:utf-8 -*-

from flask import Blueprint
from app.config.logger import Log

blueprint_app = Blueprint('app', __name__,
                template_folder='templates', static_folder='static')

Log.info('static folder : %s' % blueprint_app.static_folder)
Log.info('template folder : %s' % blueprint_app.template_folder)
