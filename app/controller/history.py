# -*- coding: utf-8 -*-

from flask import render_template, request, session, g, url_for, redirect, jsonify

from wtforms import Form
from wtforms import StringField, SelectField, IntegerField, BooleanField, PasswordField
from wtforms.validators import DataRequired
from wtforms.widgets import Input, CheckboxInput

from app.config.blueprint import blueprint_app
from app.config.database import query_db


# URL 설계
## /svn/repos
## /svn/repos/<int: pk>


@blueprint_app.route('/svn/repository', methods=['GET', 'POST'])
def svn_repository():
    """SVN Repository CRUD"""

    form = RepositoryForm(request.form)

    print(form.validate())

    print form.product.data, form.base_url.data, form.path_url.data

    if request.method == 'POST' and form.validate():
        # SVN Repository를 DB에 추가

        g.db.execute("""
                    INSERT INTO SVN_INFO (
                      s_base_url, s_path_url, s_start_revision, s_userid, s_user_pwd, active, product_id,
                      desc, create_userid, create_date, modify_date
                    )
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, [

        ])

        return redirect(url_for('app.svn_repository'))


    return render_template('svn/repository.html', form=form)


@blueprint_app.route('/svn/repository_form')
def svn_repository_form():
    return render_template('svn/repository_form.html')


@blueprint_app.route('/svn/history')
def svn_history():
    return render_template('svn/history')


class RepositoryForm(Form):
    """SVN Repository 폼"""
    product = SelectField('Product')
    base_url = StringField('Base URL', validators=[DataRequired(u'필수 입력 필드입니다.')])
    path_url = StringField('Path URL', validators=[DataRequired(u'필수 입력 필드입니다.')])
    base_rev = IntegerField('Base Revision', validators=[DataRequired(u'필수 입력입니다.')],
                            widget=Input(input_type='number'))
    svn_id = StringField('SVN ID', validators=[DataRequired(u'필수 입력 필드입니다.')])
    svn_pwd = PasswordField('SVN Password', validators=[DataRequired(u'필수 입력 필드입니다.')])
    desc = StringField('Description')
    active = BooleanField('Active')
