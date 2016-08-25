# -*- coding:utf-8 -*-

from flask import Blueprint

blueprint_app = Blueprint('app', __name__,
                          template_folder='..\\templates', static_folder='..\\static')
