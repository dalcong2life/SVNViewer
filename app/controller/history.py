# -*- coding: utf-8 -*-

from flask import render_template, request, session, g, url_for, redirect, jsonify

from app.config.blueprint import blueprint_app
from app.config.database import query_db


@blueprint_app.route('/svn/repository', methods=['GET', 'POST'])
def svn_repository():
    """SVN Repository CRUD"""

    if request.method == 'POST':
        # Repository 추가



        return jsonify()

    return render_template('svn/repository.html', products=query_db(g.db, """
        SELECT id, name
          FROM CODE
         WHERE type = 'PRODUCT'
    """))


@blueprint_app.route('/svn/repository_form')
def svn_repository_form():
    return render_template('svn/repository_form.html')


@blueprint_app.route('/svn/history')
def svn_history():
    return render_template('svn/history')
