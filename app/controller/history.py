# -*- coding: utf-8 -*-

from flask import render_template, request, session, g, url_for, redirect, jsonify

from wtforms import Form, StringField, SelectField, IntegerField, BooleanField, validators

from app.config.blueprint import blueprint_app
from app.config.database import query_db


@blueprint_app.route('/svn/repository', methods=['GET', 'POST'])
def svn_repository():
    """SVN Repository CRUD"""

    form = RepositoryForm(request.form)
    if request.method == 'POST' and form.validate():
        # Repository 추가



        return jsonify()

    # products=query_db(g.db, """
    #     SELECT id, name
    #       FROM CODE
    #      WHERE type = 'PRODUCT'
    # """)

    return render_template('svn/repository.html', form=form)


@blueprint_app.route('/svn/repository_form')
def svn_repository_form():
    return render_template('svn/repository_form.html')


@blueprint_app.route('/svn/history')
def svn_history():
    return render_template('svn/history')


class RepositoryForm(Form):
    product = SelectField('Product', choices=[('A', 'A'), ('B', 'B'), ('C', 'C')])
    repository_url = StringField('Repository URL', validators=[validators.DataRequired(u'필수 입력입니다.')])
    base_revision = IntegerField('Base Revision', validators=[validators.DataRequired(u'필수 입력입니다.')])
    description = StringField('Description')
    active = BooleanField('Active')
