# -*- coding:utf-8 -*-

import os
from sqlite3 import dbapi2 as sqlite3


def connect_db():
    """데이터베이스 커넥션 생성"""
    print os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                        'resource/database/app.db')
    return sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                        'resource/database/app.db'))


def query_db(db, query, args=(), one=False):
    cur = db.execute(query, args)
    rv = [
        dict((cur.description[idx][0], value) for idx, value in enumerate(row)) for row in cur.fetchall()
        ]
    return (rv[0] if rv else None) if one else rv
