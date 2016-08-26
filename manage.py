#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from contextlib import closing

from flask_script import Manager, Server, prompt, prompt_pass
from app import create_app

from app.config.database import DBManager

reload(sys)
sys.setdefaultencoding('utf8')

app = create_app()
manager = Manager(app)

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


@manager.command
def run():
    app.run(host='0.0.0.0', port=80, debug=app.config['DEBUG'])


@manager.command
def migrate():
    """데이터베이스 변경 사항을 반영한다.

    $ python manage.py migrate
    """
    with closing(DBManager.connect_db()) as db:
        with app.open_resource(os.path.join(PROJECT_DIR, 'schema.sql')) as f:
            db.cursor().executescript(f.read())
        db.commit()


@manager.command
def createsuperuser():
    """Super 관리자 생성
    """
    while True:
        user_email = prompt("Super user email")
        if '@' in user_email:
            break

        print "잘못된 이메일입니다."

    user_name = prompt("Super user name", default=user_email.split('@')[0])

    while True:
        user_password = prompt_pass("Enter your password")

        if (len(user_password) > 6):
            user_confirm_password = prompt_pass("Enter confirm your password")

            if user_password == user_confirm_password:
                break
            else:
                print '입력한 패스워가 잘못되었습니다.'
        else:
            print "패스워드는 최소 6자리 이상이여야 합니다."

    # 슈퍼 관리자 추가
    from datetime import datetime
    from werkzeug.security import generate_password_hash
    db = DBManager.connect_db()
    try:
        db.execute(
            """INSERT INTO USER (email, username, pw_hash, create_date, modify_date, role)
               VALUES (?, ?, ?, ?, ?, ?)
            """, [user_email, user_name, generate_password_hash(user_password),
                  datetime.now(), datetime.now(), 3])
        db.commit()
        print 'Created new superuser!'
    finally:
        db.close()


# Flask 개발용 서버
server = Server(host='0.0.0.0', port=8000)
manager.add_command('runserver', server)

if __name__ == "__main__":
    manager.run()
