# -*- coding:utf-8 -*-

from sqlite3 import dbapi2 as sqlite3


class DBManager(object):
    """Database Manager
    """
    __db_url = None

    @staticmethod
    def init(db_url):
        DBManager.__db_url = db_url

    @staticmethod
    def connect_db():
        """데이터베이스 커넥션 생성"""
        return sqlite3.connect(DBManager.__db_url)


def query_db(db, query, args=(), one=False):
    cur = db.execute(query, args)
    rv = [
        dict((cur.description[idx][0], value) for idx, value in enumerate(row)) for row in cur.fetchall()
        ]
    return (rv[0] if rv else None) if one else rv
