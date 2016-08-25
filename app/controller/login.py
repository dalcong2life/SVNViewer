# -*- coding: utf-8 -*-
from datetime import datetime

from flask import render_template, request, session, g, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash

from wtforms import Form, StringField, PasswordField, validators

from app.config.utils import to_str, to_unicode
from app.config.database import DBManager, query_db
from app.config.blueprint import blueprint_app
from app.config.logger import Log


@blueprint_app.before_request
def before_request():
    """요청 시 데이터베이스 커넥션을 맺는다."""
    g.db = DBManager.connect_db()
    g.user = None

    if 'username' in session:
        g.user = session['username']


@blueprint_app.teardown_request
def teardown_request(exception):
    """응답 후 데이터베이스 커넥션을 닫는다."""
    if hasattr(g, 'db'):
        g.db.close()


@blueprint_app.route('/')
def index():
    if g.user:
        return redirect(url_for('app.svn_repository'))

    return redirect(url_for('app.login'))


@blueprint_app.route('/register', methods=['GET', 'POST'])
def register():
    if g.user:
        return redirect(url_for('app.svn_repository'))

    form = RegisterForm(request.form)

    error = None
    if request.method == 'POST' and form.validate():
        try:
            form_email = form.email.data
            form_username = form.username.data
            form_password = form.password.data

            Log.info('Email: %s' % form_email)
            Log.info('User name: %s' % form_username)

            db_user = query_db(g.db, """
                SELECT *
                  FROM USER
                 WHERE email = ?
            """, [form_email], one=True)

            if db_user:
                error = u'이미 동일한 이메일로 등록된 사용자가 있습니다.'
            else:
                g.db.execute("""
                    INSERT INTO USER (email, username, pw_hash, create_date, modify_date)
                     VALUES (?, ?, ?, ?, ?)
                """, [form_email, form_username,
                      generate_password_hash(form_password),
                      datetime.now(), datetime.now()])

                g.db.commit()

                return redirect(url_for('app.login', email=form_email))
        except Exception as e:
            Log.debug('사용자 등록 실패!!')
            Log.debug(str(e))
            raise e

    return render_template('login/register.html', form=form, error=error)


@blueprint_app.route('/login', methods=['GET', 'POST'])
def login():
    """로그인 페이지 응답 또는 로그인 처리"""
    redirect_email = request.args.get('email', '')

    form = LoginForm(request.form)

    error = None
    if request.method == 'POST' and form.validate():

        form_email = form.email.data
        form_password = form.password.data

        try:
            db_user = query_db(g.db, """
                SELECT *
                  FROM USER
                 WHERE email = ?
            """, [form_email], one=True)

            if db_user is None or not check_password_hash(db_user['pw_hash'], form_password):
                error = u'유효하지 않는 사용자입니다.'
            else:
                session['user_info'] = db_user
                return redirect(url_for('app.svn_repository'))
        except Exception as e:
            Log.info(str(e))
            raise e

    return render_template('login/login.html',
                           form=form,
                           redirect_email=redirect_email,
                           error=error)


class LoginForm(Form):
    """로그인 폼"""
    email = StringField('Email', validators=[validators.DataRequired(to_unicode('이메일을 입력하세요.')),
                                             validators.Email(to_unicode('이메일 형식으로 입력하세요.'))])
    password = PasswordField('Password', validators=[validators.DataRequired(to_unicode('비밀번호를 입력하세요.'))])


class RegisterForm(Form):
    """사용자 등록 폼"""
    email = StringField('Email', validators=[validators.DataRequired(to_unicode('이메일을 입력하세요.')),
                                             validators.Email(to_unicode('이메일 형식으로 입력하세요.'))])
    username = StringField('User name', validators=[validators.DataRequired(to_unicode('사용자명을 입력하세요.')),
                                                    validators.Length(min=2, max=10,
                                                                      message=to_unicode('2자리 이상 10자리 이하로 입력하세요.'))])
    password = PasswordField('New Password', validators=[validators.DataRequired(to_unicode('비밀번호를 입력하세요.')),
                                                         validators.Length(min=4, max=50, message=to_unicode(
                                                             '4자리 이상 50자리 이하로 입력하세요.')),
                                                         validators.EqualTo('retry_password',
                                                                            message=to_unicode('비밀번호가 일치하지 않습니다.'))])
    retry_password = PasswordField('Confirm Password')
