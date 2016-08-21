# -*- coding:utf-8 -*-

from flask import Flask, render_template


def print_settings(config):
    print '========================================================'
    print 'SETTINGS for SVNViewer APPLICATION'
    print '========================================================'
    for key, value in config:
        print '%s=%s' % (key, value)
    print '========================================================'


def not_found(error):
    return render_template('404.html'), 404


def server_error(error):
    err_msg = str(error)
    return render_template('500.html', err_msg=err_msg), 500


def create_app(config_filepath='resource/config.cfg'):
    app = Flask(__name__)

    app.config.from_pyfile(config_filepath, silent=True)
    print_settings(app.config.iteritems())

    # 로그 초기화
    from app.config.logger import Log
    Log.init()

    # 뷰 함수 모듈은 어플리케이션 객체 생성하고 블루프린트 등록전에
    # 뷰 함수가 있는 모듈을 임포트해야 해당 뷰 함수들을 인식할 수 있음
    from app.controller import *

    # 블루프린트 등록
    from app.blueprint import blueprint_app
    app.register_blueprint(blueprint_app)


    # 공통으로 적용할 HTTP 404과 500 에러 핸들러 설정
    app.error_handler_spec[None][404] = not_found
    app.error_handler_spec[None][500] = server_error

    return app
