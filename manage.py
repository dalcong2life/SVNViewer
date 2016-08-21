#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from contextlib import closing

from flask_script import Manager, Server
from app import create_app
from app.config.database import connect_db

reload(sys)
sys.setdefaultencoding('utf8')

app = create_app()
manager = Manager(app)

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG = app.config['DEBUG'] == 'True'


@manager.command
def run():
    app.run(host='0.0.0.0', port=80, debug=DEBUG)


@manager.command
def migrate():
    """데이터베이스 변경 사항을 반영한다.
    python manage.py migrate
    """
    with closing(connect_db()) as db:
        with app.open_resource(os.path.join(PROJECT_DIR, 'schema.sql')) as f:
            db.cursor().executescript(f.read())
        db.commit()


# Flask 개발용 서버
server = Server(host='0.0.0.0', port=8000)
manager.add_command('runserver', server)

if __name__ == "__main__":
    manager.run()
